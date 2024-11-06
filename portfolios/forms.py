from django import forms
from .models import Highlight

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
