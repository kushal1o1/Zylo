from django import forms
from .models import Highlight,Section, SectionData,UserInfo

tailwind_css_for_highlights ='bg-transparent dark:text-gray-300 mb-6 w-full p-4 text-gray-700 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
tailwind_css_for_sections='bg-transparent dark:text-gray-300 w-full p-4 text-gray-700 focus:outline-none border rounded-lge focus:ring-2 focus:ring-blue-500'

class HighlightForm(forms.ModelForm):
    class Meta:
        model = Highlight
        fields = ['highlight_title', 'highlight_thumbnail_image', 'link']
        
    def __init__(self, *args, **kwargs):
        super(HighlightForm, self).__init__(*args, **kwargs)
        self.fields['highlight_title'].widget.attrs.update({
            'class': tailwind_css_for_highlights,
            'placeholder': 'Enter highlight title'
        }
        )
        self.fields['highlight_thumbnail_image'].widget.attrs.update({
            'class': tailwind_css_for_highlights,
        })
        self.fields['link'].widget.attrs.update({
            'class': tailwind_css_for_highlights,
            'placeholder': 'Enter link (optional)'
        })
        self.fields['link'].required = False
        
    def clean_highlight_title(self):
        """Validate the highlight title"""
        highlight_title = self.cleaned_data.get('highlight_title')
        if not highlight_title:
            raise forms.ValidationError("Title is required.")
        return highlight_title

    def clean_highlight_thumbnail_image(self):
        """Validate the thumbnail image"""
        image = self.cleaned_data.get('highlight_thumbnail_image')
        if not image:
            raise forms.ValidationError("Thumbnail image is required.")
        
        # Check if the uploaded file is a valid image type
        valid_image_formats = ['image/jpeg', 'image/png', 'image/gif']
        if image.content_type not in valid_image_formats:
            raise forms.ValidationError("Unsupported file format. Please upload a JPEG, PNG, or GIF image.")
        
        # Limit file size to 5MB
        max_file_size = 5 * 1024 * 1024  # 5MB
        if image.size > max_file_size:
            raise forms.ValidationError("File size must not exceed 5MB.")
        
        return image
    




class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_title']
        widgets = {
            'section_title': forms.TextInput(attrs={
                'class': tailwind_css_for_highlights,
                'placeholder': 'Enter section title(min 2 characters)'
            })
        }
    def clean_section_title(self):
        """Validate that section title is not empty and trimmed properly."""
        section_title = self.cleaned_data.get('section_title')
        
        # Check if section title is provided
        if not section_title or section_title.strip() == '':
            raise forms.ValidationError("Section title is required.")
        
        # Optional: Check for title length if needed
        if len(section_title) < 2:
            raise forms.ValidationError("Section title must be at least 2 characters long.")
        
        return section_title

class SectionDataForm(forms.ModelForm):
    class Meta:
        model = SectionData
        fields = ['section', 'main_title', 'desc', 'link', 'pic']
        widgets = {
            'section': forms.Select(attrs={
                'class': ' dark:bg-dark dark:text-gray-300 w-full p-4 text-gray-700 focus:outline-none border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'main_title': forms.TextInput(attrs={
                'class': tailwind_css_for_sections,
                'placeholder': 'Enter main title'
            }),
            'desc': forms.Textarea(attrs={
                'class': tailwind_css_for_sections,
                'placeholder': 'Enter description',
                'rows': 3
            }),
            'link': forms.URLInput(attrs={
                'class': tailwind_css_for_sections,
                'placeholder': 'Enter link'
            }),
            'pic': forms.FileInput(attrs={
                'class': tailwind_css_for_sections
            })
        }

    def __init__(self, *args, **kwargs):
        # Pop the user from kwargs
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        print(user)
        # Filter sections based on the logged-in user
        if user:
            self.fields['section'].queryset = Section.objects.filter(user=user)
        else:
            self.fields['section'].queryset = Section.objects.none()

        self.fields['section'].empty_label = "Select Section"
        self.fields['link'].required = False
        self.fields['pic'].required = False
    
    def clean_section(self):
        """Ensure section is selected"""
        section = self.cleaned_data.get('section')
        if not section:
            raise forms.ValidationError("Section is required.")
        return section

    def clean_main_title(self):
        """Ensure main title is not empty"""
        main_title = self.cleaned_data.get('main_title')
        if not main_title or main_title.strip() == '':
            raise forms.ValidationError("Main title is required.")
        return main_title

  

    def clean_pic(self):
        """Validate the uploaded image (optional)"""
        pic = self.cleaned_data.get('pic')
        if pic:
            valid_image_formats = ['image/jpeg', 'image/png', 'image/gif']
            if pic.content_type not in valid_image_formats:
                raise forms.ValidationError("Unsupported file format. Please upload a JPEG, PNG, or GIF image.")
            # Optional: Limit file size to 5MB
            max_file_size = 5 * 1024 * 1024
            if pic.size > max_file_size:
                raise forms.ValidationError("File size must not exceed 5MB.")
        return pic
    
    def clean_desc(self):
        """Make description optional"""
        return self.cleaned_data.get('desc', '')

# forms.py


class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['background_image']
    def clean_background_image(self):
        image = self.cleaned_data.get('background_image')

        # Check if the image is provided
        if not image:
            raise forms.ValidationError("Background image is required.")

        # Validate the file type (only allow JPEG, PNG, GIF)
        valid_image_formats = ['image/jpeg', 'image/png', 'image/gif']
        if image.content_type not in valid_image_formats:
            raise forms.ValidationError("Unsupported file format. Please upload JPEG, PNG, or GIF images.")

        # Limit the file size (e.g., max 5MB)
        max_file_size = 1 * 1024 * 1024  # 5MB
        if image.size > max_file_size:
            raise forms.ValidationError("File size must not exceed 5MB.")

        return image

