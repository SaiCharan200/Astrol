from django.contrib import admin
from .models import Feedback, Login, User, Report, Traits, Rashi


class ReportAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'date']
    search_fields = ['firstname', 'lastname', 'date']
    list_per_page = 10


admin.site.register(Report, ReportAdmin),
admin.site.register(Feedback),
admin.site.register(Login)
admin.site.register(User)
admin.site.register(Traits)
admin.site.register(Rashi)
