from . import views
from django.urls import path

urlpatterns = [
    path('reg', views.reg_view, name="reg"),
    path('reg/', views.reg_view, name="reg"),
    path('login', views.login_view, name="login"),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('logout/', views.logout_view, name="logout"),
    path('notes', views.notes_view, name="notes"),
    path('notes/', views.notes_view, name="notes"),
    path('add_note', views.add_note_view, name="add_note"),
    path('add_note/', views.add_note_view, name="add_note"),
]