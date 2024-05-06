from django.shortcuts import render,redirect
from .models import Event 
from .forms import BookingForm


# Create your views here.

def index(request):
    return render(request,'index.html')

def events(request):
    
    obj=Event.objects.all()
    return render(request,'sample.html',{"x":obj})
    
    return render(request,'event.html')

# def booking(request):
#     return render(request,'booking.html')

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event_app')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contact.html')



