"""
URL configuration for to_do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegistrationView.as_view()),
    path('login/',views.LoginView.as_view(),name='login'),
    path('task/',views.TaskaddView.as_view(),name='create'),
    path('alltask/',views.Taskall.as_view(),name='alltask'),
    path('deletetask/<int:pk>',views.TaskDelete.as_view(),name='delete'),
    path('taskupdate/<int:pk>',views.TaskUpdate.as_view(),name='update'),
    path('detail/<int:pk>',views.TaskDetail.as_view(),name='detail'),
    path('taskedit/<int:pk>',views.TaskEdit.as_view(),name='taskedit'),
    path('signout/',views.Signout.as_view()),
    path('complete/',views.CompletedView.as_view()),
    path('userdetail/',views.UserdetailsView.as_view())
]
