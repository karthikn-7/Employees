from django.db import models

class TypingResponse(models.Model):
    
    WPM = models.IntegerField()
    UserName = models.CharField(max_length=100)
    TimeTaken = models.IntegerField()
    TypingText = models.TextField()
    AnswerText = models.TextField()
    Accuracy = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)