from .models import UserInfo,Highlight,Section,SectionData,Alldesigns
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
#         }
background_templates = {}
background_names = {}
def get_background_data():

    
    # Retrieve all designs from the database
    designs = Alldesigns.objects.all()

    # Loop through the designs and build the dictionaries
    for design in designs:
        # Create the template path (based on the location selected in the admin)
        file_path = f"{design.location}/{design.template_file.name.split('/')[-1]}"
        
        # Add to the dictionary using the code_name as key
        background_templates[design.code_name] = file_path
        background_names[design.code_name] = design.name

    return background_templates, background_names

background_templates, background_names = get_background_data()

def get_user_data(user_info):
    """
    Returns user data
    """
    highlights = Highlight.objects.filter(user=user_info.user)
    sections = Section.objects.filter(user=user_info.user)
    user_info.selected_template = background_templates.get(user_info.selected_background)
    return highlights, sections, user_info


def handle_section_form(section_form,user):
    if section_form.is_valid():
        new_section = section_form.save(commit=False)
        new_section.user = user
        new_section.save()
        return True
    return False

def handle_section_data_form(section_data_form,user):
    if section_data_form.is_valid():
        new_section_data = section_data_form.save(commit=False)
        new_section_data.user = user
        new_section_data.save()
        return True
    return False

def handle_background_image_form(background_image_form, user):
    if background_image_form.is_valid():
        user_info = background_image_form.save(commit=False)
        user_info.user = user
        user_info.save()
        return True
    return False


