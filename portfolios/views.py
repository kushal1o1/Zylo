from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .models import ChatQuestion, ChatSession

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')


class ChatView(View):
    def get(self, request):
        # Get the first active question
        initial_question = ChatQuestion.objects.filter(is_active=True).first()
        return render(request, 'chat.html', {'question': initial_question})

    def post(self, request):
        user_answer = request.POST.get('answer')
        question_id = request.POST.get('question_id')

        # Save the user's answer
        ChatSession.objects.create(answer=user_answer)

        # Fetch the next question
        next_question = ChatQuestion.objects.filter(is_active=True).exclude(id=question_id).first()

        if next_question:
            return JsonResponse({
                'question': next_question.text,
                'question_id': next_question.id
            })
        else:
            return JsonResponse({'message': 'Thank you for your responses!'})
