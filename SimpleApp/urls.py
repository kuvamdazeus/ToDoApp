from django.contrib import admin # Not needed here

from django.urls import path, include # Include function not needed here as we will not be
                                      # redirecting user to any other place as this will be the end point

from SimpleApp.views import index, delete_todo # views.py is a default generated file used to show content for a specific
                                  # web request made by the client (App specific file)

urlpatterns = [
    path('', index), # It says that if there is nothing after the base URL, run the index function of views.py
    # Its Damn simple man !
    path('delete_todo/<int:todo_id>/', delete_todo)

]
