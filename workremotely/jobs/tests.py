from django.test import TestCase, Client
from django.urls import reverse
from .models import Job


class CreateJobTestCase(TestCase):
    def test_create_new_job(self):
        client = Client()
        response = client.post(
            reverse('create-new-job'),
            {'title': 'Ruby Developer', 'description': '...some description...',
             'company': 'Galaxy D', 'email': 'job@gd.com'})

        self.assertEqual(response.status_code, 200)

        job = Job.objects.get(email='job@gd.com')
        self.assertEqual(job.title, 'Ruby Developer')
        self.assertEqual(job.description, '...some description...')
        self.assertEqual(job.company, 'Galaxy D')
        self.assertEqual(job.email, 'job@gd.com')
