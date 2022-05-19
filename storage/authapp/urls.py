from django.urls import path
from .views import login, logout, Register, UsersListView, UserUpdateView, UserDeleteView

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('user/read/', UsersListView.as_view(), name='user_read'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
