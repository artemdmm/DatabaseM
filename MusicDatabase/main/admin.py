from django.contrib import admin
from .models import Tracks
from .models import Titles
from .models import Artists
from .models import Albums

# Register your models here.
admin.site.register(Tracks)
admin.site.register(Titles)
admin.site.register(Artists)
admin.site.register(Albums)