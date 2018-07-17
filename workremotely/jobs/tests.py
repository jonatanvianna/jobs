from django.test import TestCase, Client
from .models import Job


class CreateJobTestCase(TestCase):
    def test_create_new_job(self):
        client = Client()
        response = client.post(
            '/jobs/create/',
            {'title': 'Ruby Developer', 'description': '...some description...',
             'company': 'Galaxy D', 'email': 'job@gd.com'})

        self.assertEqual(response.status_code, 200)

        job = Job.objects.get(email='job@gd.com')
        self.assertEqual(job.title, 'Ruby Developer')
