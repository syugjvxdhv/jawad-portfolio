from django.contrib import admin
from .models import Project



# Register your models here.
from .models import ContactMessage

admin.site.register(ContactMessage)
admin.site.register(Project)