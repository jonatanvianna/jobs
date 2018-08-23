from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import JobForm
from .models import Job


def create_job(request):
    job_form = JobForm
    if request.method == "POST":
        job_form = job_form(request.POST)
        if job_form.is_valid():
            job_form.save()
            messages.success(request, message="Job created successfully.")
            return redirect(reverse("list-jobs"))
    return render(request, "jobs/create_job.html", {"form": job_form})


def list_jobs(request):
    if request.method == "GET":
        return render(
            request, "jobs/list_jobs.html", {"jobs": Job.objects.all()}
        )


def detail_job(request, pk):
    job = Job.objects.get(pk=pk)
    context = {"job": job}
    return render(request, "jobs/detail_job.html", context)


def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    template_name = "jobs/update_job.html"
    context = {}

    if request.method == "GET":
        context["form"] = JobForm(instance=job)
        return render(request, template_name, context)

    if request.method == "POST":
        job_form = JobForm(request.POST, instance=job)
        context["form"] = job_form
        if job_form.is_valid():
            job_form.save()
            messages.success(request, message="Job updated successfully.")
            return redirect(reverse("list-jobs"))
        error_message = "Errors found. Please fill the form correctly."
        messages.error(request, message=error_message)
        return render(request, template_name, context)


def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "GET":
        template_name = "jobs/delete_modal.html"
        return render(request, template_name, {"job": job})
    elif request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect(reverse("list-jobs"))
    return redirect(reverse("list-jobs"))
