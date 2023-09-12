from django.contrib import admin
from base.models import *
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('projectname',)}


admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Testimonials)
admin.site.register(Projects, ProjectAdmin)
