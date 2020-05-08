from django.contrib import admin
from sbs.models.CategoryItem import CategoryItem
from sbs.models.DirectoryCommission import DirectoryCommission
from sbs.models.DirectoryMember import DirectoryMember
from sbs.models.DirectoryMemberRole import DirectoryMemberRole
from sbs.models.MenuDirectory import MenuDirectory

# Register your models here.
admin.site.register(CategoryItem)
admin.site.register(DirectoryCommission)
admin.site.register(DirectoryMember)
admin.site.register(DirectoryMemberRole)
admin.site.register(MenuDirectory)
