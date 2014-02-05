import os
import subprocess
from django.shortcuts import render
from runner.forms import TestSuiteInitForm
from django import http
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import TestRunner, TestProfile
from django.db.models import Max

# Create your views here.
@login_required
def runner_view(request):
    if request.method == "POST":
        form = TestSuiteInitForm(request.POST)
        if form.is_valid():
            args = [form.cleaned_data['url'], form.cleaned_data['user_email']]
            if form.cleaned_data['beta']:
                args += ["--beta", form.cleaned_data['wp_login'], form.cleaned_data['wp_password']]
            test_files = os.listdir("tests")
            open_processes = list()
            for test in test_files:
                if test[-3:] == ".py":
                    process = subprocess.Popen(['python', os.path.join("tests", test)]+args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    open_processes.append(process)
            suite = TestProfile(runner=request.user)
            suite.save()
            for p in open_processes:
                out, err = p.communicate()
                t = TestRunner(test_run=suite)
                if err:
                    t.success = False
                    t.message = err
                else:
                    if out:
                        t.message = out
                        # Add conditional logic later to account for actual test runs
                        t.success = True
                    else:
                        t.success = True
                        t.message = "Success."
                t.save()
            return http.HttpResponseRedirect( reverse("results", kwargs={"index": suite.pk} ) )
        else:
            return render(request, "runner.html", {"runner_form": form})
    else:
        form = TestSuiteInitForm()
        return render(request, "runner.html", {"runner_form": form})

@login_required
def results(request, index=None):
    if not index:
        return http.HttpResponseBadRequest()
    profile = TestProfile.objects.get(pk=index, runner=request.user)
    return render(request, "results.html", {"results":profile.testrunner_set})

