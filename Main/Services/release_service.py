from Main.forms import ReleaseForm
from Main.models import Release


def save_form(form, release):
    if form.is_valid():
        release.version = form['version'].value()

        release.save()


def fill_form(release):
    form = ReleaseForm(initial={
        'version': release.version
    })

    return form


def delete_by_id(pk):
    release = get_by_id(pk)
    release.delete()


def get_all():
    releases = Release.objects.all()

    return releases


def get_by_id(pk):
    release = Release.objects.get(id=pk)
    return release
