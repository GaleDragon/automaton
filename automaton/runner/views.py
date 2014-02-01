import os
from django.conf import settings
from django.shortcuts import render
from runner.forms import TestCaseForm, CustomUploadHandler
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
@login_required
@csrf_exempt
def runner_view(request):
    #request.upload_handlers.insert(0, CustomUploadHandler(upload_to=os.path.join(settings.MEDIA_ROOT, str(request.user), '%Y/%m/%d')) )
    return _delegated_runner_view(request)

@csrf_protect
def _delegated_runner_view(request):
    if request.method == "POST":
        form = TestCaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            instance = form.instance
            instance.runner = request.user
            form.instance = instance
            form.save()
            return HttpResponseRedirect( reverse("home") )
        else:
            return render(request, "runner.html", {"runner_form": form})
    else:
        form = TestCaseForm()
        return render(request, "runner.html", {"runner_form": form})
