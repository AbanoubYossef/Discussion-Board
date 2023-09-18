from django.contrib import admin
from .models import Board,Topic
from import_export.admin import ImportExportModelAdmin
# from django.contrib.auth.models import Group
# Register your models here.
admin.site.site_header ="Boarders Admin Panel"
admin.site.site_title = "Boarders Admin Panel"
# admin.site.unregister(Group)
# @admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    fields=['subject', 'board', 'created_by', 'views']
    list_display=['subject', 'board', 'created_by', 'combine_subject_and_the_writer']
    list_display_links=['created_by','board']
    list_editable=['subject']
    list_filter=['subject', 'board', 'created_by']
    def combine_subject_and_the_writer(self,obj):
        return "{} is created by {}.".format(obj.subject,obj.created_by).title()



class InlineTopic(admin.StackedInline):
    model=Topic
    extra=1

class BoardAdmin(admin.ModelAdmin):
    inlines=[InlineTopic]



admin.site.register(Board,BoardAdmin)
admin.site.register(Topic,TopicAdmin) 