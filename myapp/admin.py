from django.contrib import admin

from .models import Product




admin.site.site_header = "My Django app"
admin.site.site_title = "Title Django"
admin.site.index_title = "My admin"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description') #добавляет отображение дополнительных полей
    search_fields = ("name",) #добавляет поле поиска по имени
    list_editable = ('price', 'description') #добавляет возможность изменения значений прямо из общего списка продуктов
    actions = ('make_zero',) #добавляет дополнительную функцию в поле Action

    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)