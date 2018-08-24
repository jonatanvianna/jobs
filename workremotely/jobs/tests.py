from django.test import TestCase, Client
from django.urls import reverse
from .models import Job


class CreateJobTestCase(TestCase):
    def test_create_new_job(self):
        client = Client()
        response = client.post(
            reverse("create-job"),
            data={
                "title": "Ruby Developer",
                "description": "...some description...",
                "company": "Galaxy D",
                "email": "job@gd.com",
            },
            follow=True,
        )
        new_job = response.context["jobs"].values()[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_job["title"], "Ruby Developer")
        self.assertEqual(new_job["description"], "...some description...")
        self.assertEqual(new_job["company"], "Galaxy D")
        self.assertEqual(new_job["email"], "job@gd.com")


class ListJobsTestCase(TestCase):
    def test_list_all_jobs(self):
        self.client.post(
            reverse("create-job"),
            {
                "title": "Software Developer",
                "description": "...some description...",
                "company": "Azion Technologies",
                "email": "job@azion.com",
            },
        )

        self.client.post(
            reverse("create-job"),
            {
                "title": "Infrastructure Anlist",
                "description": "...some description...",
                "company": "Terra Networks",
                "email": "job@terra.com",
            },
        )

        response = self.client.get(reverse("list-jobs"))
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.context["jobs"].count(), 1)

    def test_empty_jobs_list(self):
        response = self.client.get(reverse("list-jobs"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["jobs"].count(), 0)


class UpdateJobTestCase(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            title="React Developer",
            description="...some description...",
            company="Galaxy D",
            email="job@gd.com",
        )

    def test_update(self):
        url = reverse("update-job", args=[self.job.id])
        data = {
            "title": "React/Redux Developer",
            "description": "...some new description...",
            "company": "New Company",
            "email": "new_job@gd.com",
        }

        response = self.client.post(url, data, follow=True)
        self.job.refresh_from_db()
        self.assertTrue(response.status_code == 200)
        self.assertEqual(self.job.title, data["title"])
        self.assertEqual(self.job.description, data["description"])
        self.assertEqual(self.job.company, data["company"])
        self.assertEqual(self.job.email, data["email"])


class DeleteJobTestCase(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            title="ABAP Developer",
            description="...some description...",
            company="SAP inc.",
            email="jobs@sap.com",
        )

    def test_delete_job(self):
        url = reverse("delete-job", args=[self.job.id])

        response_post = self.client.post(url, follow=True)
        self.assertEqual(response_post.status_code, 200)
        
        url_detail= reverse("delete-job", args=[self.job.id])
        response_get = self.client.get(url_detail)
        self.assertEqual(response_get.status_code, 404)
