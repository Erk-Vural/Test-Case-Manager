from Main.forms import CaseForm
from Main.models import Case


def fill_form_all(cases):
    test_number = 1
    forms = []
    for case in cases:
        form = fill_form(case, test_number)
        forms.append(form)
        test_number += 1
    return forms


def fill_form(case, test_number):
    form = CaseForm(initial={
        'obj_id': case.id,
        'issue': case.issue,
        'test_number': test_number,
        'title': case.title,
        'summary': case.summary,
        'steps': case.steps,
        'status': case.status,
        'expected_result': case.expected_result,
        'actual_result': case.actual_result,
        'notes': case.notes,
        'logs': case.logs,
        'database_records': case.database_records
    })
    return form


def save_form_by_id(cases, form):
    for case in cases:
        print(form['title'].value())
        print(form['steps'].value())
        print(form['obj_id'].value())
        print(form['test_number'].value())
        print(case.id)
        save_form(form, case)


def save_form(form, case):
    if form.is_valid():
        case.issue_id = form['issue'].value()
        case.test_number = form['test_number'].value()
        case.title = form['title'].value()
        case.summary = form['summary'].value()
        case.steps = form['steps'].value()
        case.status = form['status'].value()
        case.expected_result = form['expected_result'].value()
        case.actual_result = form['actual_result'].value()
        case.notes = form['notes'].value()
        case.logs = form['logs'].value()
        case.database_records = form['database_records'].value()

        case.save()


def delete_by_id(pk):
    case = get_by_id(pk)
    issue_id = case.issue_id
    case.delete()

    return issue_id


def get_all():
    cases = Case.objects.all()

    return cases


def get_by_issue(pk):
    cases = Case.objects.filter(issue_id=pk)

    return cases


def get_by_id(pk):
    case = Case.objects.get(id=pk)
    return case
