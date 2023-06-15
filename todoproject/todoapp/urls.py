from django.urls import path
from .import views

urlpatterns = [
    path('',views.add,name='home'),
    # path('details/',views.details,name='details'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TasksListView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TasksDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TasksUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TasksDeleteView.as_view(), name='cbvdelete'),
]