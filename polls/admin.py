from django.contrib import admin
from .models import Question,Choice,member


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    #fieldsets = [
    #    (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    inlines = [ChoiceInline]

    def was_published_recently(self):
       return 'false'

class MemberAdmin(admin.ModelAdmin):
    list_display=('admno','name','fname','std')

admin.site.register(Question, QuestionAdmin)
admin.site.register(member,MemberAdmin)
