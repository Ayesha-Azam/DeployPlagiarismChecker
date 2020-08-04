from django .urls import path,include
from . import views
from .import myviews
urlpatterns=[
path("",views.home,name='home'),
path("check",views.check,name='check'),
path("rename",views.rename,name='rename'),
path("fileHandle",views.fileHandle,name='fileHandle'),
path("text",views.text,name="text"),
path('upload',views.upload,name='upload'),
path("register",views.register,name='register'),
path("login",views.login,name='login'),
path("logout",views.logout,name='logout')
]
