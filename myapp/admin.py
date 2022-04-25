from django.contrib import admin
from .models import EMPLOYEE, ORDER,STORES
class PostAdminSite(admin.AdminSite):
    site_header = "Bonjour Sales"
    site_title = "Bonjour Sales Admin Portal"
    index_title = "Welcome to Bonjour Sales"

post_admin_site = PostAdminSite(name='post_admin')
admin.site.site_header = "Bonjour Sales Admin "
admin.site.site_title = "Bonjour Sales Admin Portal"
admin.site.index_title = "Welcome to Bonjour Sales"
# Register your models here.
admin.site.register(EMPLOYEE)
post_admin_site.register(STORES)
post_admin_site.register(EMPLOYEE)
post_admin_site.register(ORDER)



