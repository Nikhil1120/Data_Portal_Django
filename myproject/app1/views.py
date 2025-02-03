from django.shortcuts import render
from app1.models import *
# Create your views here.

def home_view(request):
    response=render(request, "app1/home.html")
    return response

def display_template(request):
    response = render(request, "app1/index.html")
    return response

def display_data(request):
    n=request.GET['name']
    p = request.GET['ph']
    e = request.GET['email']
    try:
        u = User(Name=n, Phone=p, Email=e)
        u.save()
        msg = "Details send successfully.......!"
    except:
        msg = "Invalid Details"
    response = render(request, "app1/index.html", context={'msg':msg})
    return response

def user_search_template(request):
    response = render(request, "app1/search.html")
    return response

                 
def user_search_data(request):
    context = {}
    
    if 'search' in request.GET:  # Check if 'search' parameter exists in the GET request
        search_term = request.GET['search']  # Extract the search term (phone number)
        

        try:
            # Check if the search term is a numberr
            if search_term.isdigit() or len(search_term) ==10:
                # Search by phone number
                user = User.objects.get(Phone=search_term)  # Assuming 'Phone' is the field name in your model
                context['user'] = user
            # else:
            #     context['number_error']='Invalid mobile number'
            #     response = render(request, 'app1/search.html', context)
            #     return response
            
            elif search_term.isalnum():
                
                # Search by name
                user = User.objects.get(Name=search_term)
                # If user is found, add details to the context
                context['user'] = user
            
            

        except User.DoesNotExist:
            
            context['number_error'] = 'Invalid mobile number'
            response = render(request, 'app1/search.html', context)
            return response
        finally:
            context['spam'] = 'This number is spam.'

    return render(request, "app1/res.html", context)
