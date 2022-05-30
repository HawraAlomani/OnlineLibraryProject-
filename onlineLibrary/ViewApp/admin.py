from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')
    list_filter = ('name',)
    # date_hierarchy = 'pub_date'
    search_fields = ('name',)


admin.site.register(Review, ReviewAdmin)
