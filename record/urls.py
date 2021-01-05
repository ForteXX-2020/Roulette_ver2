from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    path('',views.index, name='index'), #/record
    path('add/',views.add, name='add'), #/record/add
    path('next_matrix/',views.next_matrix, name='next_matrix'), #/record/next
    path('update/<int:pk>/',views.update, name='update'), #/record/update/1
    path('delete/<int:pk>/',views.delete, name='delete'), #/record/delete/1
    path('all_delete/',views.all_delete, name='all_delete'), #/record/delete/1

]
