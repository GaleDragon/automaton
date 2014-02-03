import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

import httplib2
from apiclient.discovery import build
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets

import atom.data
import gdata.gauth
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

from automaton.settings import SECRET_KEY

from .models import Credential


SCOPE = ["email","https://www.google.com/m8/feeds", "https://www.googleapis.com/auth/userinfo.profile"]

# Create your views here.
def init_auth(request):
    redirect = request.build_absolute_uri( reverse("auth_callback") )
    flow = flow_from_clientsecrets(
        'domain/google_api/client_secrets.json',
        SCOPE,
        redirect_uri=redirect)
    flow.params["state"] = xsrfutil.generate_token(SECRET_KEY, 7337)
    flow.params["hd"] = "boomtownroi.com"
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)

def callback_auth(request):
    redirect = request.build_absolute_uri( reverse("auth_callback") )
    flow = flow_from_clientsecrets(
        'domain/google_api/client_secrets.json',
        SCOPE,
        redirect_uri=redirect)
    if xsrfutil.validate_token(SECRET_KEY, request.REQUEST['state'], 7337):
        credentials = flow.step2_exchange( request.REQUEST )
        client = gdata.contacts.client.ContactsClient(domain="boomtownroi.com")
        auth2token = gdata.gauth.OAuth2Token(client_id=credentials.client_id,
                                             client_secret=credentials.client_secret,
                                             scope=SCOPE,
                                             access_token=credentials.access_token,
                                             refresh_token=credentials.refresh_token,
                                             user_agent=credentials.user_agent)
        auth2token.authorize(client)

        contact = client.GetContact('https://www.google.com/m8/feeds/contacts/default/full/')
        json_credentials = json.loads( credentials.to_json() )
        email = json_credentials["id_token"]['email']
        username = email.split("@")[0]
        password = SECRET_KEY
        new = User.objects.create_user(username, email=email, password=password)
        Credential(id=new, credential=credentials).save()
        user = authenticate( username=username, password=password )
        login(request, user)
        return HttpResponseRedirect( reverse("home") )

@login_required
def home(request):
    form = None
    return render(request, "home.html", {"runner-form": form})