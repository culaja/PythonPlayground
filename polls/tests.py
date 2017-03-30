from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice
from .models import NoChoicesException

class QuestionMethodTests(TestCase):
    def test_client(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)

    def test_get_wining_choice_works(self):
        q = Question.objects.create(question_text='This is my text', pub_date=timezone.now())
        c = Choice.objects.create(question=q, choice_text='Simple text', votes=5)
        self.assertIs(q.get_wining_choice().votes, 5)

    def test_get_wining_choice_without_choices_throws_exception(self):
        q = Question.objects.create(question_text='This is my text', pub_date=timezone.now())
        self.assertRaises(NoChoicesException, q.get_wining_choice)

class QuestionDatabaseTests(TestCase):
    fixtures = ['polls_views_testdata.json']
    def test_something(self):
        c = Choice.objects.all()
        self.assertIs(len(c), 3)

    def test_index_page(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_question_list' in resp.context)
