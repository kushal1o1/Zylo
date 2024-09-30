import json
from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    
    return render(request, 'portfolio/chat_form.html')

def home(request):
    
    return render(request, 'portfolio/index.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required  
@csrf_exempt #To do: remove in production
def update_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse the JSON data from the request

        # Get the current logged-in user
        user = request.user

        # Get or create the UserInfo object for the current user
        user_info, created = UserInfo.objects.get_or_create(user=user)

        # Update fields dynamically if they exist in the request
        for field in ['name', 'bio', 'phone_number', 'facebook_link']:
            if field in data:
                setattr(user_info, field, data[field])  # Dynamically set the value

        user_info.save()  # Save the updated model instance

        return JsonResponse({'message': 'User info updated successfully!'})

    return JsonResponse({'message': 'Invalid request method!'}, status=400)