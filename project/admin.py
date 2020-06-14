from django.contrib import admin


from project.models import Project, ProjectImage

# Register your models here.


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]
    inlines = [
        ProjectImageInline,
    ]

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectImage._meta.fields]
    class Meta:
        model = ProjectImage


admin.site.register(ProjectImage, ProjectImageAdmin)
