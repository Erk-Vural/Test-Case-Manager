from django.http import HttpResponseRedirect
from django.shortcuts import render

from Main.Services import release_service
from Main.forms import ReleaseForm


from Main.models import Release


def release_list(request):
    releases = release_service.get_all()
    context = {
        'releases': releases,
    }
    return render(request, "release-list.html", context)


def release_new(request):
    release = Release()
    if request.method == 'POST':
        form = ReleaseForm(request.POST)
        release_service.save_form(form, release)
    form = ReleaseForm()

    context = {
        'form': form
    }

    return render(request, 'release-detail.html', context)


def release_update(request, pk):
    release = release_service.get_by_id(pk)
    if request.method == 'POST':
        form = ReleaseForm(request.POST)
        release_service.save_form(form, release)

    form = release_service.fill_form(release)

    context = {
        'form': form,
        'release': release
    }

    return render(request, "release-detail.html", context)


def release_delete(request, pk):
    release_service.delete_by_id(pk)

    return HttpResponseRedirect("/release/")
