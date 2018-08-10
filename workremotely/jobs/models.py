from django.db import models


class Job(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=255,
    )

    description = models.TextField(
        verbose_name='Description',
        max_length=5000,
    )

    company = models.CharField(
        verbose_name='Company',
        max_length=255,
    )

    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True,
    )
