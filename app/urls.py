from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('<int:id>/update',views.update),
    path('<int:id>/delete',views.delete),
    path('<int:id>/completed',views.completed),
    path('<int:id>/not-completed',views.notcompleted),
]
