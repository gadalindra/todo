from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('detail/<int:pk>', views.DetailTaskView.as_view(), name='detail-task'),
    path('update/<int:pk>', views.UpdateTaskView.as_view(), name='update-task'),
    path('delete/<int:pk>', views.DeleteTastView.as_view(), name='delete-task'),
    path('search/', views.searchTask, name='search-task')
]