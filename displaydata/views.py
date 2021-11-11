from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/") #this is so that the user can only add data if they are logged in, if not logged in, redirect to login page
def displayData(request):
    display_form = forms.DisplayData()
    return render(request, 'displaydata/displaydata.html',{'form': display_form})
