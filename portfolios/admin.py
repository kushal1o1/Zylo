
from django.contrib import admin
from .models import UserInfo, Highlight,Section,SectionData,Alldesigns
from django.utils.html import mark_safe


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'userUrl','name', 'profession', 'bio_txt', 'profile_image_preview', 'background_image_preview')
    search_fields = ('user__username', 'name')
    
    # Specify the fields to display in the detail view and set the preview fields as read-only
    fields = ('user', 'name', 'profession', 'bio_txt', 'profile_image', 'background_image', 'selected_background')
    readonly_fields = ('profile_image_preview', 'background_image_preview')

    def profile_image_preview(self, obj):
        """Display a small preview of the profile image in the admin."""
        if obj.profile_image:
            return mark_safe(f'<img src="{obj.profile_image.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    profile_image_preview.short_description = 'Profile Image Preview'

    def background_image_preview(self, obj):
        """Display a small preview of the background image in the admin."""
        if obj.background_image:
            return mark_safe(f'<img src="{obj.background_image.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    background_image_preview.short_description = 'Background Image Preview'


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('user', 'highlight_title', 'link', 'highlight_thumbnail_preview')
    search_fields = ('user__username', 'highlight_title')
    list_filter = ('user',)

    fields = ('user', 'highlight_title', 'link', 'highlight_thumbnail_image', 'highlight_thumbnail_preview')
    readonly_fields = ('highlight_thumbnail_preview',)

    def highlight_thumbnail_preview(self, obj):
        """Display a small preview of the uploaded thumbnail image in admin."""
        if obj.highlight_thumbnail_image:
            # Ensure the image is properly marked as safe HTML
            return mark_safe(f'<img src="{obj.highlight_thumbnail_image.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    highlight_thumbnail_preview.short_description = 'Thumbnail Preview'

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'user', 'section_data_count')  # Show the title and count of related SectionData
    search_fields = ('section_title', 'user__username')
    list_filter = ('user',)

    # Function to count the number of SectionData related to each Section
    def section_data_count(self, obj):
        return obj.section_data.count()  # Count the related SectionData entries
    section_data_count.short_description = 'Section Data Count'


# Register SectionData Admin
@admin.register(SectionData)
class SectionDataAdmin(admin.ModelAdmin):
    list_display = ('main_title', 'section', 'user', 'pic_preview', 'link')  # Show title, section, user, and image preview
    search_fields = ('main_title', 'section__section_title', 'user__username')
    list_filter = ('section', 'user')

    # Function to show the image preview
    def pic_preview(self, obj):
        """Display a small preview of the image in the admin."""
        if obj.pic:
            return mark_safe(f'<img src="{obj.pic.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    pic_preview.short_description = 'Image Preview'

    # Make sure the fields are editable directly in the admin form
    fields = ('user', 'section', 'main_title', 'desc', 'link', 'pic')
    
class AlldesignsAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_name', 'location', 'template_file']
    search_fields = ['name', 'code_name']

admin.site.register(Alldesigns, AlldesignsAdmin)

