import os
import subprocess
from django.shortcuts import render
from runner.forms import TestSuiteInitForm
from django import http
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import TestRunner
from django.db.models import Max

# Create your views here.
@login_required
def runner_view(request):
    if request.method == "POST":
        form = TestSuiteInitForm(request.POST)
        if form.is_valid():
            test_files = os.listdir("tests")
            open_processes = list()
            for test in test_files:
                if test[-3:] == ".py":
                    process = subprocess.Popen(['python', test], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    open_processes.append(process)
            for p in open_processes:
                out, err = p.communicate()
                t = TestRunner(runner=request.user, done=True)
                last_run = TestRunner.objects.all().aggregate(Max('index'))["index__max"]
                t.index = last_run or 0 + 1
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
                t.save()
            return http.HttpResponseRedirect( reverse("results", args=("index", t.index) ) )
        else:
            return render(request, "runner.html", {"runner_form": form})
    else:
        form = TestSuiteInitForm()
        return render(request, "runner.html", {"runner_form": form})

@login_required
def results(request, index=None):
    if not index:
        return http.HttpResponseBadRequest()
    test_results = TestRunner.objects.filter(runner=request.user, index=index)
    return render(request, "results.html", {"results":test_results})

