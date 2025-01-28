from django.contrib import admin
from django.urls import path
from . import views

# URL patterns for the app
urlpatterns = [
    
    # Home page route
    path('', views.home, name='home'),
    # Maps to the home view, which displays the list of rooms, topics, and recent activity
    
    # Room detail page
    path('room/<str:pk>/', views.room, name='room'),
    # Dynamically fetches and displays a specific room based on its primary key (pk)

    # User profile page
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    # Displays the profile of a specific user identified by their primary key (pk)
    
    # Create room page
    path('create-room/', views.createRoom, name='create-room'),
    # Allows authenticated users to create a new chat room

    # Update room page
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    # Allows the host of a specific room to edit its details

    # Delete room page
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    # Allows the host of a specific room to delete it

    # Delete message page
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    # Allows the author of a specific message to delete it

    # Login page
    path('login/', views.loginPage, name='login'),
    # Displays the login page and handles user login

    # Logout route
    path('logout/', views.logoutUser, name='logout'),
    # Logs out the currently authenticated user

    # Registration page
    path('register/', views.registerPage, name='register'),
    # Displays the registration form and handles user sign-up
]
