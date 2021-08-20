from django.contrib import admin

from .models import AboutSite
from .models import Slider
from .models import Contact
from .models import Notice
from .models import Books

admin.site.register(AboutSite)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Notice)
admin.site.register(Books)

