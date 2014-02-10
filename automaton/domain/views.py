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
    '''
    Introduces OAuth2 with a Google backend. The purpose is to ensure that only @boomtownroi.com people can login.
    This view contains the setup to make the request to Google. Here the view to direct Google to after authentication
    is given by the reverse() method, which return the URL from the named string in urls.py.
    '''
    redirect = request.build_absolute_uri( reverse("auth_callback") )
    # The Flow object contains the configurations to make the request
    import os
    print os.getcwd()
    flow = flow_from_clientsecrets(
        'domain/google_api/client_secrets.json',
        SCOPE,
        redirect_uri=redirect)
    # The state parameter to verify that the request is not a Cross Site Request Forgery
    flow.params["state"] = xsrfutil.generate_token(SECRET_KEY, 7337)
    # The hosted domain to restrict access to BoomTown peeps
    flow.params["hd"] = "boomtownroi.com"
    # Builds to URL to redirect to
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)

def callback_auth(request):
    # Rebuilds a similar flow object to later authorize from Google's callback
    redirect = request.build_absolute_uri( reverse("auth_callback") )
    flow = flow_from_clientsecrets(
        'domain/google_api/client_secrets.json',
        SCOPE,
        redirect_uri=redirect)
    if xsrfutil.validate_token(SECRET_KEY, request.REQUEST['state'], 7337):
        # Another backend handshake with Google to resolve the request
        credentials = flow.step2_exchange( request.REQUEST )

        # At this point the credentials can be used to access anything in the given SCOPE

        # Here's me trying to get my Email Contacts
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

        # Creates a new User from the info in the credentials.
        # Since the password will not be used to login (since the OAuth takes care of that),
        # we can set it to the SECRET_KEY and keep it like that.
        #new = User.objects.create_user(username, email=email, password=password)
        #Credential(id=new, credential=credentials).save()
        user = authenticate( username=username, password=password )
        login(request, user)
        return HttpResponseRedirect( reverse("home") )

@login_required
def home(request):
    form = None
    return HttpResponseRedirect( reverse('start') )
