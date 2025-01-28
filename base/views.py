from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Room, Topic, Message
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm

# Create your views here.

# View to handle user login
def loginPage(request):
    page = 'login'

    # Redirect authenticated users to the home page
    if request.user.is_authenticated:
        return redirect('home')

    # Process login form submission
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password does not exist!")

    context = {'page': page}
    return render(request, "base/login_register.html", context)

# View to handle user logout
def logoutUser(request):
    logout(request)
    return redirect("home")

# View to handle user registration
def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)  # Automatically log in the new user
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")
    
    return render(request, 'base/login_register.html', {'form': form})

# View to display the home page
def home(request):
    # Search functionality: Filter rooms by query parameter
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))  

    context = {"rooms": rooms, "topics": topics, "rooms_count": rooms_count, "room_messages": room_messages}
    return render(request, "base/home.html", context)

# View to display a specific room and its messages
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')  # Fetch messages in descending order
    participants = room.participants.all()
    
    if request.method == "POST":
        # Add a new message to the room
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)  # Add user to room participants
        return redirect('room', pk=room.id)
    
    context = {"room": room, "room_messages": room_messages, "participants": participants}
    return render(request, "base/room.html", context)

# View to display user profile
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()  # Rooms created by the user
    room_messages = user.message_set.all()  # Messages sent by the user
    topics = Topic.objects.all()
    context = {"user":user, "rooms": rooms, "room_messages":room_messages, "topics":topics}
    return render(request, 'base/profile.html', context)

# View to create a new room (login required)
@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user  # Assign the logged-in user as the host
            room.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)

# View to update an existing room (login required)
@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)  # Pre-fill the form with the room's current data
    
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!!")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)

# View to delete a room (login required)
@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here !! ')

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})

# View to delete a message (login required)
@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('You are not allowed here !! ')

    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": message})
