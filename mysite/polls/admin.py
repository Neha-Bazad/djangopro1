from django.contrib import admin
from django.contrib import admin

from .models import Question
from .models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    '''fieldsets = [
        ('Question',         {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]'''
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
# Register your models here.