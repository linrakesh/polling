from django.db import models

# Create your models here.
class Question(models.Model):
    Image = 'BLANK'
    question_text = models.CharField(max_length=200)
    pub_date   = models.DateTimeField('date published')
    image = models.FileField(default=Image)

    
    def __str__(self):
        """Unicode representation of question."""
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class member(models.Model):
    admno = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    std = models.CharField(max_length=20)
    points = models.IntegerField(default=1)
    status =models.CharField(max_length=20)



class LoveLike(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    #user  = models.ForeignKey(User,on_delete=model.CASCADE)
