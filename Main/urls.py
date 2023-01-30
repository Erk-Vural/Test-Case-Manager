from django.urls import path

from Main.Views.case_views import *
from Main.Views.issue_views import *
from Main.Views.release_views import *
from Main.views import home

urlpatterns = [
    path('', home, name='home'),

    # Release view urls.
    path('release/', release_list, name='release_list'),
    path('release/new', release_new, name='release-new'),
    path('release/update/<int:pk>/', release_update, name="release_update"),
    path('release/delete/<int:pk>/', release_delete, name="release_delete"),

    # Issue view urls.
    path('issue/', issue_list_all, name='issue_list_all'),
    path('issue/<int:pk>/', issue_list, name='issue_list'),
    path('issue/new', issue_new, name='issue_new'),
    path('issue/update/<int:pk>/', issue_update, name="issue_update"),
    path('issue/delete/<int:pk>/', issue_delete, name="issue_delete"),

    # Case view urls.
    path('case/', case_list_all, name='case_list_all'),
    path('case/manage/<int:pk>/', case_manage, name='case_manage'),
    path('case/new/<int:pk>/', case_new, name='case_new'),
    path('case/delete/<int:pk>/', case_delete, name="case_delete"),
    # temporary URLs will be replaced with case_manage
    path('case/<int:pk>/', case_list, name='case_list'),
    path('case/update/<int:pk>/', case_update, name="case_update"),

]
