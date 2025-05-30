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
from decouple import config
from . services import get_user_data,handle_section_form,handle_background_image_form,get_background_data
from django.contrib import messages
from PIL import Image 
import imghdr

# background_templates = {
#         "bg0": "designs/default.html",
#         "bg1": "designs/bg2.html",
#         "bg2": "designs/bigbox.html",
#         "bg3": "designs/checkboard.html",
#         "bg4": "designs/dotted.html",
#         "bg5": "designs/dottedbg.html",
#         "bg6": "designs/graphbigboxes.html",
#         "bg7": "designs/overlay.html",
#         "bg8": "designs/test.html",
#         "bg9": "animated/canvas.html",
#         "bg10": "animated/circle.html",
#         "bg11": "animated/colorcircle.html",
#         "bg12": "animated/diagonalstrip.html",
#         "bg13": "animated/hexagon.html",
#         "bg14": "animated/polygon.html",
#         "bg15": "animated/star.html",
#         "bg16": "animated/test.html",
#         "bg17": "animated/particles.html",
#         "bg18": "designs/Wavyy.html",
#         "bg19": "designs/polygon.html",
#         "bg20": "designs/Celebration.html",
#         "bg21": "designs/Development.html",
#         "bg22": "animated/Cosmic.html",
#         "bg23": "animated/circuitboard.html",
#         "bg24": "animated/neoncyberpunk.html",
#         "bg25": "animated/randombubbles.html",
#         "bg26": "animated/blobs.html",
#         "bg27": "animated/codingmatrix.html",
#         "bg28": "animated/forestfirefly.html",
        
#         }

# background_names = {
#     "bg0": "Default Design",    
#     "bg1": "Minimalistic Graph",
#     "bg2": "Big Box Design",
#     "bg3": "Checkerboard Pattern",
#     "bg4": "Dotted Grid",
#     "bg5": "Dotted Background",
#     "bg6": "Large Grid Boxes",
#     "bg7": "Overlay Effect",
#     "bg8": "Test Pattern",
#     "bg9": "Animated Canvas",
#     "bg10": "Animated Circles",
#     "bg11": "Color Circles Animation",
#     "bg12": "Diagonal Stripes Animation",
#     "bg13": "Hexagonal Pattern",
#     "bg14": "Polygonal Shapes",
#     "bg15": "Star Animation",
#     "bg16": "Test Animation",
#     "bg17": "Particles Animation",
#     "bg18": "Wavy Background",
#     "bg19": "Polygonal Background",
#     "bg20": "Celebrations Background",
#     "bg21": "Development Background",
#     "bg22": "Cosmic Background",
#     "bg23": "Circuit Board Animation",
#     "bg24": "Neon Cyberpunk Animation",
#     "bg25": "Random Bubbles Animation",
#     "bg26": "Blobs Animation",
#     "bg27": "Coding Matrix Animation",
#     "bg28": "Forest Firefly Animation",
    
# }

background_templates, background_names = get_background_data()
fasurl=config("FASURL")

def main_page(request):
    """
    Landing Page 
    """
    return render(request, 'MainPage/index.html')


def index(request,userUrl):
    """
    It serve users Website by fetching the user info and highlights from the database.
    It also fetches the sections and their data for the user. The selected background template is set based on the user's choice.
    """
    user_info = UserInfo.objects.filter(userUrl=userUrl).first()
    if user_info:
        highlights, sections, user_info =get_user_data(user_info)
        user_info.selected_template = background_templates.get(user_info.selected_background)
        return render(request, 'portfolio/portfolioServer.html', {'user_info': user_info ,"background_templates": background_templates,'highlights': highlights,'sections': sections})
    else:
        return redirect("/NotFound")


@login_required
def home(request):
    """
    Home Page for Creating and Managing Website with Highlights and Sections
    """
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
                if handle_section_form(section_form,request.user):
                    messages.success(request, "Section created successfully.")
                    return redirect('home')
                else:
                    for field, errors in section_form.errors.items():
                        for error in errors:
                            messages.warning(request, f"{field.capitalize()}: {error}")
                    messages.error(request, "Failed to create section. Please try again.")
                    return redirect('home')
            
            elif form_type == "section_data_form":
            # Handle adding a new section data entry to an existing section
                section_data_form = SectionDataForm(request.POST, request.FILES,user=request.user)
                if handle_section_form(section_data_form,request.user):
                    messages.success(request, "Section data created successfully.")
                    return redirect('home')
                else:
                    for field, errors in section_data_form.errors.items():
                        for error in errors:
                            messages.warning(request, f"{field.capitalize()}: {error}")
                    messages.error(request, "Failed to create section data. Please try again.")
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
                        messages.success(request, "Highlight created successfully.")    
                        return redirect('home')  # Redirect to the highlight list after saving
                


        
        form = HighlightForm()
        section_form = SectionForm()
        section_data_form = SectionDataForm(user=request.user)


        return render(request, 'portfolio/index.html', {'user_info': user_info, "background_templates": background_templates,'highlights': highlights,'form': form,'sections': sections,
        'section_form': section_form,
        'section_data_form': section_data_form,
        'background_names': background_names,
         "fasurl":fasurl
         }
       )
    else:
        return redirect("accounts/login")

@login_required  
def update_user_info(request):
    """
    Update User Information Through AJAX Request
    This view handles the AJAX request to update user information such as name, bio, and social media links.
    """
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
                value = data[field].strip()


                if field == 'userUrl':
                    if UserInfo.objects.filter(userUrl=value).exclude(user=user).exists():
                        return JsonResponse({'message': 'User Url already Taken,Please choose another one.'}, status=400)
                setattr(user_info, field, data[field])  # Dynamically set the value
                user_info.save()

        

        return JsonResponse({'message': 'User info updated successfully!'})

    return JsonResponse({'message': 'Invalid request method!'}, status=400)

@login_required  
def update_images(request):
    """
    Update User Profile Image 
    """
    if request.method == 'POST':
       
        user = request.user

       
        user_info, created = UserInfo.objects.get_or_create(user=user)
        
        # if 'profile_img' in request.FILES:
        #     user_info.profile_image = request.FILES['profile_img']
        if 'profile_img' in request.FILES:
            image_file = request.FILES['profile_img']

            valid_extensions = ['jpeg', 'jpg', 'png','gif']
            extension = image_file.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                messages.warning(request,"Only JPEG , PNG , Gif files are allowed.")
                return redirect("home")

            try:
                img = Image.open(image_file)
                if img.format not in ['JPEG', 'PNG']:
                    messages.warning(request,"Uploaded file is not a valid image.")
                    return redirect("home")
            except Exception as e:
                messages.warning(request,"Invalid image file.")
                return redirect("home")
            
            if image_file.size > 2 * 1024 * 1024:
                messages.warning(request,"Image size exceeds 2MB.")
                return redirect("home")
            
        user_info.profile_image = request.FILES['profile_img']
        user_info.save()
        
        return redirect("home")
    
@login_required
def update_background_image(request):
    """
    Update User Background Image 
    """
    if request.method == 'POST':
        user = request.user
        user_info, created = UserInfo.objects.get_or_create(user=user)   

        form = BackgroundImageForm(request.POST, request.FILES, instance=user_info)
        if form.is_valid():
            form.save()
            messages.success(request, "Background image updated successfully.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"{field.capitalize()}: {error}")
            messages.warning(request, "Background image not updated.")

        return redirect('home')
        
       

@login_required
def delete_highlight(request, highlight_id):
    """
    Delete Highlight Entry
    """
    # Get the highlight and delete it if it belongs to the current user
    highlight = get_object_or_404(Highlight, id=highlight_id, user=request.user)
    highlight.delete()
    return redirect('home')  # Redirect back to the highlight list after deletion

@login_required
def delete_section(request, section_id):
    """
    Delete Section Entry
    """
    # Fetch the section associated with the logged-in user
    section = get_object_or_404(Section, id=section_id, user=request.user)
    
    # Check if there are any associated SectionData entries
    related_data = SectionData.objects.filter(section=section,user=request.user)
    if related_data.exists():
        SectionData.objects.filter(section=section,user=request.user).delete()
    section.delete()
    return redirect('home')

@login_required
def delete_section_data(request, data_id):
    """
    Delete Section Data Entry
    """
    print("heheh")
    print(data_id)
    section_data = get_object_or_404(SectionData, id=data_id, section__user=request.user)  # Check ownership
    section_data.delete()
    return redirect('home')

def not_found(request):
    """
    Render Not Found Page
    """
    return render(request, 'Notfound.html')

@login_required
def delete_background_image(request):
    """
    Delete Background Image
    """
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

@login_required
def get_code_snippet(request):
    """
    Render Code Snippet Partial Template for User To see their website while creating it
    """
    # Get any necessary context data
    user_info =UserInfo.objects.filter(user=request.user).first()
    print(user_info.selected_background)
    user_info.selected_template = background_templates.get(user_info.selected_background)
    highlights = Highlight.objects.filter(user=user_info.user)
    sections = Section.objects.filter(user=user_info.user)
    
    
    # Just render the partial template
    return render(request, 'portfolio/codesnippet.html', {"user_info":user_info,'highlights': highlights,'sections': sections})