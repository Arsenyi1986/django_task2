from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reg', views.regpage, "reg"),
    path('reg/', views.regpage, "reg"),
    path('login', views.loginpage, "login"),
    path('login/', views.loginpage, "login"),
    path('logout', views.logoutpage, "logout"),
    path('logout/', views.logoutpage, "logout"),
    path('notes', views.notespage, "notes"),
    path('notes/', views.notespage, "notes"),
    path('add_note', views.add_notepage, "add_note"),
    path('add_note/', views.add_notepage, "add_note"),
]