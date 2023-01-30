from Main.forms import IssueForm
from Main.models import Issue


def save_form(form, issue):
    if form.is_valid():
        issue.project_name = form['project_name'].value()
        issue.issue = form['issue'].value()
        issue.release_id = form['release'].value()
        issue.designer_name = form['designer_name'].value()
        issue.executor_name = form['executor_name'].value()
        issue.design_date = form['design_date'].value()
        issue.execution_date = form['execution_date'].value()

    issue.save()


def fill_form(issue):
    form = IssueForm(initial={
        'project_name': issue.project_name,
        'issue': issue.issue,
        'release': issue.release_id,
        'designer_name': issue.designer_name,
        'design_date': issue.design_date,
        'executor_name': issue.executor_name,
        'execution_date': issue.execution_date
    })

    return form


def delete_by_id(pk):
    issue = get_by_id(pk)
    release_id = issue.release_id
    issue.delete()

    return release_id


def get_all():
    issues = Issue.objects.all()

    return issues


def get_by_release(pk):
    issues = Issue.objects.filter(release_id=pk)
    return issues


def get_by_id(pk):
    issue = Issue.objects.get(id=pk)
    return issue
