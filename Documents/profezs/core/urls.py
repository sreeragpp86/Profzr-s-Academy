from django.urls import path
from . import views

urlpatterns = [
    # Main Landing Page
    path('', views.index, name='index'),

    # Subject Selection Pages (The 3 grid pages you just built)
    path('sslc/', views.sslc_subjects, name='sslc_subjects'),
    path('plus-one/', views.plus_one_subjects, name='plus_one_subjects'),
    path('plus-two/', views.plus_two_subjects, name='plus_two_subjects'),

    # The PDF Material List Page
    # This captures 'sslc', 'plus-one', or 'plus-two' as <category>
    path('materials/<str:category>/', views.material_list, name='material_list'),
]
