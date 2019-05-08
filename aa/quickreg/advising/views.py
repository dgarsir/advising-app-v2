from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone

from .forms import SubmitAdvisingForm, ApproveDenyForm
from .models import Advising
from users.models import CustomUser

# Create your views here.

def submit_advising(request):
    if request.method == "POST":
        form = SubmitAdvisingForm(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.author = request.user.EMPLID
            a_form.date_submitted = timezone.now()
            if (a_form.total_credits < 45):
                a_form.status = 2
            else:
                a_form.status = 1
            request.user.was_denied = False
            request.user.save()
            a_form.save()
            return redirect('home')
    else:
        form = SubmitAdvisingForm()
    return render(request, 'submit_advising.html', {'form': form})

def select_advising(request):
    if (request.user.user_type == 1):
        to_be_advised = Advising.objects.filter(total_credits__gte=45).filter(status = 1)
    else:
        to_be_advised = Advising.objects.filter(status = 2)
    if request.method=="POST":
        request.session['selected_id'] = request.POST.get('selected_form')
        #for some reason redirect works and render doesn't?
        #idk don't change it
        return redirect('view_advising_faculty')
    return render(request, 'select_advising.html', {'to_be_advised' : to_be_advised})

def view_advising_faculty(request):

    a_form = Advising.objects.get(pk = request.session['selected_id'])
    f_name = CustomUser.objects.get(EMPLID = a_form.author).first_name
    l_name = CustomUser.objects.get(EMPLID = a_form.author).last_name

    return render(request, 'view_advising_faculty.html', {
    'f_name' : f_name,
    'l_name' : l_name,
    'semester' : a_form.semester,
    'major' : a_form.major,
    'QPA' : a_form.QPA,
    'GPA' : a_form.GPA, 
    'intended_courses' : a_form.intended_courses,
    'currently_enrolled' : a_form.currently_enrolled,
    'completed_courses' : a_form.completed_courses,
    'total_credits' : a_form.total_credits,
    'date_submitted' : a_form.date_submitted,
    })


def view_advising(request):

    a_form = list(Advising.objects.filter(author = request.user.EMPLID))[0]
    if request.method == "POST":
        Advising.objects.filter(author = request.user.EMPLID).delete()
        return redirect('home')
    return render(request, 'view_advising.html', {
        'semester' : a_form.semester,
        'major' : a_form.major,
        'QPA' : a_form.QPA,
        'GPA' : a_form.GPA, 
        'intended_courses' : a_form.intended_courses,
        'currently_enrolled' : a_form.currently_enrolled,
        'completed_courses' : a_form.completed_courses,
        'total_credits' : a_form.total_credits,
        'date_submitted' : a_form.date_submitted
    })
    
def confirm_approve(request):
    a_form = Advising.objects.get(pk = request.session['selected_id'])
    if (request.user.user_type == 1):
        if request.method == "POST":
            a_form.status = 2
            a_form.save()
            request.session['selected_id'] = ''
            return redirect('home')
    else:
        if request.method == "POST":
            a_form.status = 3
            a_form.save()
            request.session['selected_id'] = ''
            return redirect('home')

    return render(request, 'confirm_approve.html', {
        'a_form' : a_form
    })

def confirm_deny(request):
    a_form = Advising.objects.get(pk = request.session['selected_id'])
    student = CustomUser.objects.get(EMPLID = a_form.author)
    if request.method == "POST":
        student.was_denied = True
        student.save()
        a_form.delete()
        request.session['selected_id'] = ''
        return redirect('home')
    return render(request, 'confirm_deny.html', {
        'a_form' : a_form
    })