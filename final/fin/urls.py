

from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('detail',views.detail,name="detail"),
    path('add_data',views.add_data,name="add-data"),
    path('list_emp',views.list_emp,name="list-emp"),
    path('show_emp/<emp_id>',views.show_emp,name="show-emp"),
    path('delete_emp/<emp_id>',views.delete_emp,name="delete-emp"),
    path('update_emp/<emp_id>',views.update_emp,name="update-emp")
]
