from django.db import models

# Create your models here.

class Skill(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    text = models.TextField()
    correct_option = models.ForeignKey('Option', related_name='correct_question', on_delete=models.CASCADE)

    def __str__(self):
        return self.text



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Test(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_minutes = models.IntegerField(default=30)
    questions = models.ManyToManyField(Question)


    def __str__(self):
        return self.title
    


class TestAttempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.test.title
    
    
    def calculate_score(self):
        total_questions = self.test.questions.count()
        correct_answers = 0

        for question in self.test.questions.all():
            if self.selected_option_for_question(question) == question.correct_option:
                correct_answers += 1
        
        score = (correct_answers / total_questions) * 100
        self.score = score
        self.save()
    
    def selected_option_for_question(self, question):
        try:
            user_response = UserResponse.objects.get(test_attempt=self, question=question)
            return user_response.selected_option
        except UserResponse.DoesNotExist:
            return None
        
        
class UserResponse(models.Model):
    test_attempt = models.ForeignKey(TestAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


    






