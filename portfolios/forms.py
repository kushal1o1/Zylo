from django import forms
from .models import Highlight,Section, SectionData

class HighlightForm(forms.ModelForm):
    class Meta:
        model = Highlight
        fields = ['highlight_title', 'highlight_thumbnail_image', 'link']
        
    def __init__(self, *args, **kwargs):
        super(HighlightForm, self).__init__(*args, **kwargs)
        self.fields['highlight_title'].widget.attrs.update({
            'class': 'w-full p-4 text-gray-700 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter title'
        })
        self.fields['highlight_thumbnail_image'].widget.attrs.update({
            'class': 'w-full p-4 text-gray-700 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
        self.fields['link'].widget.attrs.update({
            'class': 'w-full p-4 text-gray-700 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter link'
        })





class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_title']
        widgets = {
            'section_title': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter section title'
            })
        }

class SectionDataForm(forms.ModelForm):
    class Meta:
        model = SectionData
        fields = ['section', 'main_title', 'desc', 'link', 'pic']
        widgets = {
            'section': forms.Select(attrs={
                'class': 'w-full p-3 rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'main_title': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter main title'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter description',
                'rows': 3
            }),
            'link': forms.URLInput(attrs={
                'class': 'w-full p-3 rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter link'
            }),
            'pic': forms.FileInput(attrs={
                'class': 'w-full p-3 rounded-lg border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].empty_label = "Select Section"  # Set custom label for empty dropdown option
