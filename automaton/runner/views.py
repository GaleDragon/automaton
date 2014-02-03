from django.shortcuts import render
from runner.forms import TestSuiteInitForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def runner_view(request):
    if request.method == "POST":
        form = TestSuiteInitForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect( reverse("home") )
        else:
            return render(request, "runner.html", {"runner_form": form})
    else:
        form = TestSuiteInitForm()
        return render(request, "runner.html", {"runner_form": form})
