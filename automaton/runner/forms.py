import tempfile
import os
from django import forms
from .models import TestRunner

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
__author__ = 'jeremymorgan'

from django.core.files.uploadhandler import FileUploadHandler

class CustomUploadHandler(FileUploadHandler):
    def __init__(self, request = None, upload_to = tempfile.gettempdir()):
        self.upload_to = upload_to
        FileUploadHandler.__init__(self, request)

    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        if not os.path.exists(self.upload_to):
            os.makedirs(self.upload_to)
        elif not os.path.isdir(self.upload_to):
            raise IOError("%s exists and is not a directory." % self.upload_to)

        outPath = os.path.join(self.upload_to, file_name)
        self.destination = open(outPath, 'wb+')

    def receive_data_chunk(self, raw_data, start):
        self.destination.write(raw_data)

    def file_complete(self, file_size):
        self.destination.close()

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestRunner
        exclude = ['runner','date_started']

    def __init__(self, *args, **kwargs):
        super(TestCaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.add_input(Submit('submit', 'Submit'))

class TestSuiteInitForm(forms.Form):
    def __init__(self, data=None, *args, **kwargs):
        super(TestSuiteInitForm, self).__init__(data, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.add_input(Submit('submit', 'Submit'))

    url = forms.URLField()
    user_email = forms.EmailField()
    beta = forms.ChoiceField(widget=forms.RadioSelect(), choices=((True, 'Site is in Beta'),(False, 'Site is not in Beta')), initial=False)
    wp_login = forms.CharField(required=False)
    wp_password = forms.CharField(required=False, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(TestSuiteInitForm, self).clean()
        production = bool( cleaned_data['beta'] == "False")
        print production
        login = cleaned_data['wp_login']
        password = cleaned_data['wp_password']
        print cleaned_data
        if (not production) and (login == "" or password == ""):
            raise forms.ValidationError("If the URL is a beta site then WordPress credentials are required.")
        return cleaned_data