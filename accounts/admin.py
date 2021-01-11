from django.contrib import admin

admin.site.site_header = 'Kobiltek Bilisim Kullanici Yönetim Paneli '  # default: "Django Administration"
admin.site.index_title = 'Sistem Yönetimi'  # default: "Site administration"
admin.site.site_title = 'Admin'  # default: "Django site admin"



from sbs.models.CategoryItem import CategoryItem
from sbs.models.DirectoryCommission import DirectoryCommission
from sbs.models.DirectoryMember import DirectoryMember
from sbs.models.DirectoryMemberRole import DirectoryMemberRole
from sbs.models.MenuDirectory import MenuDirectory
from sbs.models.License import License

# Register your models here.
admin.site.register(CategoryItem)
admin.site.register(DirectoryCommission)
admin.site.register(DirectoryMember)
admin.site.register(DirectoryMemberRole)
admin.site.register(MenuDirectory)
admin.site.register(License)
