from django.contrib import admin
from .models import Question, Option

# Register the Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')  # Display these fields in the admin list view

# Register the Option model
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_text', 'question','is_correct')  # Display these fields in the admin list view
