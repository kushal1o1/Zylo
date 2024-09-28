from django.db import models



class ChatQuestion(models.Model):
    text = models.TextField(help_text="Enter the question text.")
    is_active = models.BooleanField(default=True, help_text="Indicates if the question is active.")
    
    def __str__(self):
        return self.text

class ChatSession(models.Model):
    answer = models.TextField(help_text="Store user's answer.")
    question = models.ForeignKey(ChatQuestion, on_delete=models.CASCADE, related_name='responses')
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the answer was recorded.")
    
    def __str__(self):
        return f"Answer to '{self.question.text}': {self.answer}"
