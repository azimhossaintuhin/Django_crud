from django.urls import path
from . import views


urlpatterns = [
    path('', views.empolyelist , name = 'home'),
    path('add', views.add , name="add"),
    path('edit', views.edit , name = 'update'),
    path('update/<str:id>', views.update , name = 'update'),
    path('delete/<str:id>', views.delete , name = 'delete'),

]
