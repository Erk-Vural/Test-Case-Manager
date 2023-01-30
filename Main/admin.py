from django.contrib import admin

from .models import Issue, Case, Release

# Register your models here.
admin.site.register(Issue)
admin.site.register(Case)
admin.site.register(Release)
