from django.shortcuts import render, redirect
from django.contrib import messages
from tutor_match.models import Tutor
from django.http import HttpResponse
from django import forms
from django.contrib.auth import forms as auth_forms
from .forms import UserAuthForm, UserSearchForm, UserProfileForm, UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'tutor_match/index.html')

def login(request):
    if request.method == 'POST':
        login_form = UserAuthForm(request.POST)
        if login_form.is_valid():
            u_auth = []
            u_auth.append(login_form.cleaned_data.get("u_email"))
            u_auth.append(login_form.cleaned_data.get("u_password"))
            user_object = login_helper(u_auth)
            if user_object == None:
                return render(request, 'tutor_match/login.html', {'form': login_form})
            else:
                messages.success(request, 'Signed in')
                userID = user_object.username
                template = generateProfileTemplate(userID)
                return render(request, 'tutor_match/profile.html', {"template": template})
    else:
        login_form = UserAuthForm()
    return render(request, 'tutor_match/login.html', {'form': login_form})

def login_helper(u_credentials):
    query = Tutor.objects.filter(email = u_credentials[0], password = u_credentials[1])
    if (len(query) == 1):
        return query[0]
    else:
        return None

def register(request):
    if request.method == 'POST':
        registration_form = auth_forms.UserCreationForm(request.POST)
        if registration_form.is_valid():
            u_data = []
            email = registration_form.cleaned_data.get("username")
            password = registration_form.cleaned_data.get("password1")
            u_data.append(email)
            u_data.append(password)
            new_user(u_data)
            return redirect(newProfile)
    else:
        registration_form = auth_forms.UserCreationForm()
    return render(request, 'tutor_match/signup.html', {'form': registration_form})

def new_user(user_data):
    ID = str(int(Tutor.objects.latest('username').username) + 1)
    user_entry = Tutor(username = ID, email = user_data[0], 
        password = user_data[1], priceID = 0, rating = 0)
    user_entry.save()

def profile(request):
    return render(request, f'tutor_match/profile.html', {"template": ""})

def newProfile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            fullName = profile_form.cleaned_data.get("u_fullName")
            priceID = profile_form.cleaned_data.get("u_priceID")
            classID = profile_form.cleaned_data.get("u_classID")
            contact = profile_form.cleaned_data.get("u_contact")
            rating = profile_form.cleaned_data.get("u_rating")

            index = len(Tutor.objects.all()) - 1

            email = Tutor.objects.all()[index].email

            user_object = Tutor.objects.filter(username=str(index))
            user_object.update(fullName = fullName)
            #user_object.update(priceID = priceID)
            # Future fix
            user_object.update(classID = classID)
            user_object.update(contact = contact)
            user_object.update(rating = rating)

            template = ''
            template += f'<h1> Name: {fullName} </h1>\n'
            template += f'<li> Cost: {priceID} </li>\n'
            template += f'<li> Class: {classID} </li>\n'
            template += f'<li> Email: {email} </li>\n'
            template += f'<li> Contact Info: {contact} </li>\n'
            template += f'<li> Rating: {rating} </li>\n'
            user_object.update(template = template)
            return render(request, 'tutor_match/profile.html', {"form": '', "template": template})
    else:
        profile_form = UserProfileForm()
    return render(request, 'tutor_match/profile.html', {"form": profile_form, "template": ''})


def generateProfileTemplate(userID):
    #this is what the user will see after doing a search and clicking on a link with a match
    u_data = []
    user_object = Tutor.objects.filter(username=userID)
    u_data.append(user_object[0].priceID)
    u_data.append(user_object[0].classID)
    u_data.append(user_object[0].email)
    u_data.append(user_object[0].contact)
    u_data.append(user_object[0].rating)
    fullName = user_object[0].fullName
    template = ''
    template += f'<h1> {fullName} </h1>\n'
    for data in u_data:
        template += f'<li> {data} </li>\n'
    return template

# Algorithm to search based on a set of instructions.
def search(request):
    #bridge between form inputs and database query
    #output database results using dynamic html templates
    #search_helper(#add in field forms)
    #generateSearchTemplate(query)
    if request.method == 'POST':
        search_form = UserSearchForm(request.POST)
        if search_form.is_valid():
            u_data = []
            u_data.append(search_form.cleaned_data.get("t_name"))
            u_data.append(search_form.cleaned_data.get("t_classID"))
            u_data.append(search_form.cleaned_data.get("t_price"))
            u_data.append(search_form.cleaned_data.get("t_rating"))
            u_matches = search_helper(u_data)
            template = generateSearchTemplate(u_matches)
            return render(request, 'tutor_match/search.html', {"form": search_form, "template": template})
    else:
        search_form = UserSearchForm()
    return render(request, 'tutor_match/search.html', {"form": search_form, "template": ''})

# Takes a string as an input and displays the subsequent classes.
def search_helper(u_class_filter):
    # Grab all objects
    query = Tutor.objects.all()

    # Filter by name if there is a field input.
    if (u_class_filter[0] != None):
        query = query.filter(fullName__contains=u_class_filter[0])

    # Filter the query by class id if there is a field input.
    if (u_class_filter[1] != None):
        query = query.filter(classID__contains=u_class_filter[1])
    
    # Filter the query by price if there is a field input.
    if (u_class_filter[2] != None):    
        query = query.filter(priceID__contains=u_class_filter[2])

    # Filter the query by price if there is a field input.
    if (u_class_filter[3] != None):
        query = query.filter(rating__contains=u_class_filter[3])

    # returns the query SET with the filtered data
    return query

# Algorithm to search based on a set of instructions.
def generateSearchTemplate(u_matches):
    template = ''
    for match in u_matches:
        template += f'<li> <a href="/profile" {match.fullName}>{match.fullName}</a> {match.contact} </li>\n' #add href link leading to profile (generate profile page using generateProfileTemplate)
    return template

def test(request):
    output = "1"
    return HttpResponse(f'<h1> {output} </h1>')