import json
from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    
    return render(request, 'portfolio/chat_form.html')

def home(request):
    user_info = None
    if request.user.is_authenticated:
        user_info = UserInfo.objects.filter(user=request.user).first()

    return render(request, 'portfolio/index.html', {'user_info': user_info})


import json
from django.http import JsonResponse
from .models import UserInfo
@login_required  
@csrf_exempt #To do: remove in production
def update_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse the JSON data from the request
        # Get the current logged-in user
        user = request.user

        # Get or create the UserInfo object for the current user
        user_info, created = UserInfo.objects.get_or_create(user=user)
        
        # Define the fields to update
        fields_to_update = [
            'name','bio_txt', 
            'instagram_link','facebook_link', 'tiktok_link',
            'youtube_link', 'x_link', 'spotify_link', 'linkedin_link',
            'profile_image', 'highlight_title','highlight_thumbnail_image',
            
        ]

        # Update fields dynamically if they exist in the request
        for field in fields_to_update:
            if field in data:
                setattr(user_info, field, data[field])  # Dynamically set the value
                user_info.save()

        # Handle the section fields (assuming they are passed as a list of dictionaries)
        # sections = data.get('sections', [])
        # for section_data in sections:
        #     section_name = section_data.get('section_name')
        #     section_title = section_data.get('section_title')
        #     section_image = section_data.get('section_image')  # Handle file upload as needed

        #     # If section_name is provided, create or update the section
        #     if section_name or section_title:
        #         section, _ = Section.objects.get_or_create(user_info=user_info, section_name=section_name)
        #         section.section_title = section_title
        #         if section_image:
        #             section.section_image = section_image  # Handle file uploads appropriately
        #         section.save()

          # Save the updated UserInfo instance

        return JsonResponse({'message': 'User info updated successfully!'})

    return JsonResponse({'message': 'Invalid request method!'}, status=400)
