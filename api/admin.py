from django.contrib import admin
from myapp.api.models import *

admin.site.register(Forumpost, ForumpostAdmin)
admin.site.register(Tag, TagAdmin)
