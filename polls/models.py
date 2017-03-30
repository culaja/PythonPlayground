from django.db import models

class NoChoicesException(Exception): pass

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def get_wining_choice(self):
        orderedChoices = Choice.objects.order_by('-votes')
        if len(orderedChoices) == 0:
            raise NoChoicesException('No choices for given question!')
        wining_choice = orderedChoices[0]
        return wining_choice

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
