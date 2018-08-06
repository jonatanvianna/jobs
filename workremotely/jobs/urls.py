from django.urls import path
from .views import create_job, list_jobs, detail_job, update_job

urlpatterns = [
    path('list/', list_jobs, name='list-jobs'),
    path('create/', create_job, name='create-job'),
    path('detail/<pk>/', detail_job, name='detail-job'),
    path('update/<pk>/', update_job, name='update-job'),
]
