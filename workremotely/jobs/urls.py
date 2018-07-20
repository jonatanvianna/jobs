from django.urls import path
from .views import create_job, list_jobs

urlpatterns = [
    path('list/', list_jobs, name='list-jobs'),
    path('create/', create_job, name='create-new-job'),
]
