from django.urls import path
from .views import add_item, update_item, delete_item, ProductListView, ProductDetailView, ProductDeleteView

app_name= "myapp" #добавление пространства имен (namespace) в проект

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:pk>/", ProductDeleteView.as_view(), name="delete_item"),
]
