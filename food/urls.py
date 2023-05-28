from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    #path('', views.index, name='index'),
    path('', views.IndexClassView.as_view(), name='index'),
    #/food/1
    #path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.items, name='item'),
    #add_items
    #path('add/',views.create_item, name='create_item'),
    path('add/',views.CreateItem.as_view(), name='create_item'),
    #update_item
    path('update/<int:id>',views.update_item, name='update_item'),
    #delete_item
    path('delete/<int:id>',views.delete_item, name='delete_item'),

    ]