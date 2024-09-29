
from django.contrib import admin
from .models import UserInfo,Question

# @admin.register(ChatQuestion)
# class ChatQuestionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'is_active')
#     search_fields = ('text',)

# @admin.register(ChatSession)
# class ChatSessionAdmin(admin.ModelAdmin):
#     list_display = ('answer', 'question', 'created_at')
#     search_fields = ('answer',)
#     list_filter = ('created_at',)

admin.site.register(UserInfo)

admin.site.register(Question)
