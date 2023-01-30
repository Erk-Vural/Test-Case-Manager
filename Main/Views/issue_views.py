from django.http import HttpResponseRedirect
from django.shortcuts import render

from Main.Services import issue_service
from Main.forms import IssueForm
from Main.models import Issue


# Issue View

def issue_list_all(request):
    issues = issue_service.get_all()
    context = {
        'issues': issues
    }
    return render(request, "issue-list.html", context)


def issue_list(request, pk):
    issues = issue_service.get_by_release(pk)

    context = {
        'issues': issues
    }
    return render(request, "issue-list.html", context)


def issue_new(request):
    issue = Issue()
    if request.method == 'POST':
        form = IssueForm(request.POST)
        issue_service.save_form(form, issue)

    form = IssueForm()

    context = {
        'form': form
    }

    return render(request, 'issue-detail.html', context)


def issue_update(request, pk):
    issue = issue_service.get_by_id(pk)
    if request.method == 'POST':
        form = IssueForm(request.POST)
        issue = issue_service.save_form(form, issue)

    form = issue_service.fill_form(issue)

    context = {
        'form': form,
        'issue': issue
    }

    return render(request, "issue-detail.html", context)


def issue_delete(request, pk):
    release_id = issue_service.delete_by_id(pk)

    return HttpResponseRedirect("/issue/id/".replace('id', str(release_id)))
