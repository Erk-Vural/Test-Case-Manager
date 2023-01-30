from django import forms

from .models import Release, Issue

status = [('ToDo', 'ToDo'),
          ('Ok', 'Ok'),
          ('Not Ok', 'Not Ok'),
          ('Review', 'Review'),
          ('In Progress', 'In Progress')]


def get_objects(object_type):
    if object_type == 1:
        releases = Release.objects.all()
        choices = []
        for release in releases:
            choices.append((release.id, release.version))
    elif object_type == 2:
        issues = Issue.objects.all()
        choices = []
        for issue in issues:
            choices.append((issue.id, issue.issue))

    return choices


class ReleaseForm(forms.Form):
    version = forms.CharField(label='Release Version', max_length=16)


class IssueForm(forms.Form):
    release = forms.ChoiceField(label="Release", widget=forms.Select(), choices=get_objects(1), required=True)
    project_name = forms.CharField(label="Project Name", max_length=30)
    issue = forms.CharField(label="Issue", max_length=30)
    designer_name = forms.CharField(label="Designer Name", max_length=30)
    executor_name = forms.CharField(label="Executor Name", max_length=30)
    design_date = forms.DateField(label="Design Date", widget=forms.TextInput(attrs={
        'class': 'datepicker',
    }))
    execution_date = forms.DateField(label="Execution Date", widget=forms.TextInput(attrs={
        'class': 'datepicker',
    }))


class CaseForm(forms.Form):
    obj_id = forms.IntegerField(required=False)
    issue = forms.ChoiceField(label="Issue", widget=forms.Select(), choices=get_objects(2), required=True)
    test_number = forms.IntegerField(label="Test Number", required=False, )
    title = forms.CharField(label="Title", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    summary = forms.CharField(label="Summary", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    steps = forms.CharField(label="Steps", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    expected_result = forms.CharField(label="Expected Result", widget=forms.Textarea(attrs={'class': 'form-control'}),
                                      required=False)
    actual_result = forms.CharField(label="Actual Result", widget=forms.Textarea(attrs={'class': 'form-control'}),
                                    required=False)
    status = forms.ChoiceField(label="Status", widget=forms.Select(), choices=status, required=False)
    notes = forms.CharField(label="Notes", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    logs = forms.CharField(label="Logs", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    database_records = forms.CharField(label="Database Records", widget=forms.Textarea(attrs={'class': 'form-control'}),
                                       required=False)
