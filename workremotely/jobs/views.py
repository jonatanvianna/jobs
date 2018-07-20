from django.shortcuts import render
from .forms import JobForm
from .models import Job


def create_job(request):
    job_form = JobForm
    if request.method == 'POST':
        job_form = job_form(request.POST)
        if job_form.is_valid():
            job_form.save()
            job_form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': job_form})


def list_jobs(request):
    if request.method == 'GET':
        return render(request, 'jobs/list_jobs.html', {'jobs': Job.objects.all()})
