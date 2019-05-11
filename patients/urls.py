from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.doctors,name="doctors"),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    #path('message/',views.message,name='message'),
    path('<doctor_id>',views.patients_names,name='p_names'),
    path('<doctor_id>/details/<patient_id>',views.patients_details,name='p_details'),
]