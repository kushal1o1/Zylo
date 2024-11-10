import json
from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo,Highlight,Section,SectionData
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Highlight
from .forms import HighlightForm,SectionForm,SectionDataForm,BackgroundImageForm
import os

background_templates = {
        "bg0": "designs/default.html",
        "bg1": "designs/bg2.html",
        "bg2": "designs/bigbox.html",
        "bg3": "designs/checkboard.html",
        "bg4": "designs/dotted.html",
        "bg5": "designs/dottedbg.html",
        "bg6": "designs/graphbigboxes.html",
        "bg7": "designs/overlay.html",
        "bg8": "designs/test.html",
        "bg9": "animated/canvas.html",
        "bg10": "animated/circle.html",
        "bg11": "animated/colorcircle.html",
        "bg12": "animated/diagonalstrip.html",
        "bg13": "animated/hexagon.html",
        "bg14": "animated/polygon.html",
        "bg15": "animated/star.html",
        "bg16": "animated/test.html",
        "bg17": "animated/particles.html",
        "bg18": "designs/Wavyy.html",
        "bg19": "designs/polygon.html",
        "bg20": "designs/Celebration.html",
        }
background_names = {
    "bg0": "Default Design",    
    "bg1": "Minimalistic Graph",
    "bg2": "Big Box Design",
    "bg3": "Checkerboard Pattern",
    "bg4": "Dotted Grid",
    "bg5": "Dotted Background",
    "bg6": "Large Grid Boxes",
    "bg7": "Overlay Effect",
    "bg8": "Test Pattern",
    "bg9": "Animated Canvas",
    "bg10": "Animated Circles",
    "bg11": "Color Circles Animation",
    "bg12": "Diagonal Stripes Animation",
    "bg13": "Hexagonal Pattern",
    "bg14": "Polygonal Shapes",
    "bg15": "Star Animation",
    "bg16": "Test Animation",
    "bg17": "Particles Animation",
    "bg18": "Wavy Background",
    "bg19": "Polygonal Background",
    "bg20": "Celebrations Background",
}

def MainPage(request):
    return render(request, 'MainPage/index.html')


# Create your views here.
def index(request,userUrl):
    user_info = UserInfo.objects.filter(userUrl=userUrl).first()
    if user_info:
        
        highlights = Highlight.objects.filter(user=user_info.user)
        sections = Section.objects.filter(user=user_info.user)
        user_info.selected_template = background_templates.get(user_info.selected_background)
        return render(request, 'portfolio/portfolioServer.html', {'user_info': user_info ,"background_templates": background_templates,'highlights': highlights,'sections': sections})
    else:
        return redirect("/NotFound")


@login_required
def home(request):
    user_info = None
    if request.user.is_authenticated:
        highlights = Highlight.objects.filter(user=request.user)
        sections = Section.objects.filter(user=request.user)
        user_info = UserInfo.objects.filter(user=request.user).first()
        if not user_info:
            user_info = UserInfo.objects.create(user=request.user)
        user_info.selected_template = background_templates.get(user_info.selected_background)
        if request.method == "POST":
            form_type = request.POST.get("form_type")
            if form_type == "section_form":
            # Handle creating a new section
                section_form = SectionForm(request.POST)
                if section_form.is_valid():
                    new_section = section_form.save(commit=False)
                    new_section.user = request.user
                    new_section.save()
                    return redirect('home')
            
            elif form_type == "section_data_form":
            # Handle adding a new section data entry to an existing section
                section_data_form = SectionDataForm(request.POST, request.FILES)
                if section_data_form.is_valid():
                    new_section_data = section_data_form.save(commit=False)
                    new_section_data.user = request.user
                    new_section_data.save()
                    return redirect('home')

            elif form_type == "other_form":
            # Handle the other form submission here
                highlight_id = request.POST.get("highlight_id")  # Get the highlight ID (if editing)
                
                if highlight_id:
                    # Editing an existing highlight
                    highlight = get_object_or_404(Highlight, id=highlight_id, user=request.user)
                    form = HighlightForm(request.POST, request.FILES, instance=highlight)
                    
                    if form.is_valid():
                        form.save()
                        return redirect('home')  # Redirect to the highlight list after saving
                    
                else:
                    # Adding a new highlight
                    form = HighlightForm(request.POST, request.FILES)
                    
                    if form.is_valid():
                        new_highlight = form.save(commit=False)
                        new_highlight.user = request.user  # Associate the new highlight with the logged-in user
                        new_highlight.save()
                        return redirect('home')  # Redirect to the highlight list after saving

        
        form = HighlightForm()
        section_form = SectionForm()
        section_data_form = SectionDataForm()


        return render(request, 'portfolio/index.html', {'user_info': user_info, "background_templates": background_templates,'highlights': highlights,'form': form,'sections': sections,
        'section_form': section_form,
        'section_data_form': section_data_form,
        'background_names': background_names})
    else:
        return redirect("accounts/login")



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
            'name','bio_txt','profession', 
            'instagram_link','facebook_link', 'tiktok_link',
            'youtube_link', 'x_link', 'spotify_link', 'linkedin_link',
            'selected_background','userUrl'
            
        ]

        # Update fields dynamically if they exist in the request
        for field in fields_to_update:
            if field in data:
                setattr(user_info, field, data[field])  # Dynamically set the value
                user_info.save()

        

        return JsonResponse({'message': 'User info updated successfully!'})

    return JsonResponse({'message': 'Invalid request method!'}, status=400)

@login_required  
def update_images(request):
    if request.method == 'POST':
       
        user = request.user

       
        user_info, created = UserInfo.objects.get_or_create(user=user)
        
        if 'profile_img' in request.FILES:
            print("done")
            user_info.profile_image = request.FILES['profile_img']
        user_info.save()
        return redirect("home")
    
@login_required
def update_background_image(request):
    if request.method == 'POST':
        user = request.user
        user_info, created = UserInfo.objects.get_or_create(user=user)
        if 'background_image' in request.FILES:
            user_info.background_image = request.FILES['background_image']
        user_info.save()
        return redirect("home")
    
    


@login_required
def delete_highlight(request, highlight_id):
    # Get the highlight and delete it if it belongs to the current user
    highlight = get_object_or_404(Highlight, id=highlight_id, user=request.user)
    highlight.delete()
    return redirect('home')  # Redirect back to the highlight list after deletion

@login_required
def delete_section(request, section_id):
    section = get_object_or_404(Section, id=section_id, user=request.user)
    section.delete()
    return redirect('home')

@login_required
def delete_section_data(request, data_id):
    print("heheh")
    print(data_id)
    section_data = get_object_or_404(SectionData, id=data_id, section__user=request.user)  # Check ownership
    section_data.delete()
    return redirect('home')

def NotFound(request):
    return render(request, 'Notfound.html')




@login_required
def delete_background_image(request):
    try:
        user_info = UserInfo.objects.get(user=request.user)
        if user_info.background_image:
            # Delete the background image file
            old_image_path = user_info.background_image.path
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
            user_info.background_image = None
            user_info.save()
    except UserInfo.DoesNotExist:
        pass

    return redirect('home')  