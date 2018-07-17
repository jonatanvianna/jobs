from django.test import TestCase, Client
from .models import Job


class CreateJobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(
            id=10,
            title='Python Backend Developer',
            description='Here is awesome job description',
            company='Galaxy D',
            email='job@gd.com'
            )

    def test_created_job(self):
        job = Job.objects.get(id=10)
        self.assertEqual(job.title, 'Python Backend Developer')

    def test_client(self):
        c = Client()
        response = c.post(
            '/jobs/create/',
            {'title': 'Ruby Developer', 'description': '...some description...',
             'company': 'Galaxy D', 'email': 'job@gd.com'})
        self.assertEqual(response.status_code, 200)
