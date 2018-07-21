from django.test import TestCase, Client
from django.urls import reverse
from .models import Job


class CreateJobTestCase(TestCase):
    def test_create_new_job(self):
        client = Client()
        response = client.post(
            reverse('create-new-job'),
            {'title': 'Ruby Developer',
             'description': '...some description...',
             'company': 'Galaxy D', 'email': 'job@gd.com'})

        self.assertEqual(response.status_code, 200)

        job = Job.objects.get(email='job@gd.com')
        self.assertEqual(job.title, 'Ruby Developer')
        self.assertEqual(job.description, '...some description...')
        self.assertEqual(job.company, 'Galaxy D')
        self.assertEqual(job.email, 'job@gd.com')


class ListJobsTestCase(TestCase):
    def test_list_all_jobs(self):
        title = 'Software Developer'
        description = '...some description...'
        company = 'Azion Technologies'
        email = 'job@azion.com'

        self.client.post(
            reverse('create-new-job'),
            {'title': title, 'description': description, 'company': company,
             'email': email})
        self.client.post(
            reverse('create-new-job'),
            {'title': title, 'description': description, 'company': company,
             'email': email})

        response = self.client.get(reverse('list-jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.context['jobs'].count(), 1)
        
    def test_empty_jobs_list(self):
        response = self.client.get(reverse('list-jobs'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['jobs'].count(), 0)
