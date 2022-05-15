from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    path('caretakers/', views.CaretakerList.as_view(), name='caretakers_index'),
    path('caretakers/<int:pk>/', views.CaretakerDetail.as_view(), name='caretakers_detail'),
    path('caretakers/create/', views.CaretakerCreate.as_view(), name='caretakers_create'),
    path('caretakers/<int:pk>/update', views.CaretakerUpdate.as_view(), name='caretakers_update'),
    path('caretakers/<int:pk>/delete/', views.CaretakerDelete.as_view(), name='caretakers_delete'),
]