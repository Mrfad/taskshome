from django.urls import path
from .views import mytasks, addtask

urlpatterns = [
    path('', mytasks, name='mytasks' ),
    path('addtask/', addtask, name='addtask' ), 
]
