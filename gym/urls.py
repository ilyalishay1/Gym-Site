from django.urls import path
from gym import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('price/', views.price, name='price'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('suplements/', views.suplements, name='suplements'),
    path('suplements/protein/', views.protein, name='protein'),
    path('suplements/creatin/', views.creatin, name='creatin'),
    path('suplements/bcaa/', views.bcaa, name='bcaa'),
    path('suplements/vitamins/', views.vitamins, name='vitamins'),
    path('suplements/preworkout/', views.preworkout, name='preworkout'),
    path('suplements/amins/', views.amins, name='amins'),
    path('suplements/boosters/', views.boosters, name='boosters'),
]
