from django.http import HttpResponseRedirect
from django.shortcuts import render

from Main.Services import case_service
from Main.forms import CaseForm
# Case Views
from Main.models import Case


def case_list_all(request):
    cases = case_service.get_all()

    context = {
        'cases': cases
    }
    return render(request, "case-list.html", context)


# This view combines list and update views.
def case_manage(request, pk):
    cases = case_service.get_by_issue(pk)
    forms = case_service.fill_form_all(cases)

    if request.method == 'POST':
        form = CaseForm(request.POST)
        case_service.save_form_by_id(cases, form)

    context = {
        'forms': forms,
        'form': CaseForm(),
        'cases': cases,
        'pk': pk,
    }
    return render(request, "case-manage.html", context)


def case_new(request, pk):
    case = Case()
    if request.method == 'POST':
        form = CaseForm(request.POST)
        case_service.save_form(form, case)

    form = CaseForm()

    context = {
        'form': form
    }

    return HttpResponseRedirect("/case/manage/pk/".replace('pk', str(pk)))


def case_delete(request, pk):
    issue_id = case_service.delete_by_id(pk)

    return HttpResponseRedirect("/case/manage/pk/".replace('pk', str(issue_id)))


# Temporary Views
def case_update(request, pk):
    case = case_service.get_by_id(pk)
    if request.method == 'POST':
        form = CaseForm(request.POST)
        case_service.save_form(form, case)

    form = case_service.fill_form(case)

    context = {
        'form': form,
        'case': case
    }
    return render(request, "case-detail.html", context)


def case_list(request, pk):
    cases = case_service.get_by_issue(pk)

    context = {
        'cases': cases
    }
    return render(request, "case-list.html", context)
