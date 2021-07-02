from django.urls import path


from todo_app import views
# app_name='todoapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:tid>/', views.update, name='update'),
    path('cbvhome/', views.listview1.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.detailview1.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.update1.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.delete1.as_view(), name='cbvdelete'),
]