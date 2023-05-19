from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('monsters/', views.monsters_index, name='index'),
  path('monsters/<int:monster_id>/', views.monsters_detail, name='detail'),
  path('monsters/create/', views.MonsterCreate.as_view(), name='monsters_create'),
  path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monsters_update'),
  path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monsters_delete'),
  path('monsters/<int:monster_id>/add_battle/', views.add_battle, name='add_battle'),
  path('monsters/<int:monster_id>/assoc_type/<int:type_id>/', views.assoc_type, name='assoc_type'),
  path('monsters/<int:monster_id>/unassoc_type/<int:type_id>/', views.unassoc_type, name='unassoc_type'),
  # Type
  path('types/', views.TypeList.as_view(), name='types_index'),
  path('types/<int:pk>/', views.TypeDetail.as_view(), name='types_detail'),
  path('types/create/', views.TypeCreate.as_view(), name='types_create'),
  path('types/<int:pk>/update/', views.TypeUpdate.as_view(), name='types_update'),
  path('types/<int:pk>/delete/', views.TypeDelete.as_view(), name='types_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]