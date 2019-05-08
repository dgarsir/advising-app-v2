from django.shortcuts import render, redirect
from django.views import generic

from advising.models import Advising
from message.models import Message

def Home(request):

    authenticated = request.user.is_authenticated
    
    if authenticated:

        user_type = request.user.user_type
        num_messages = len(Message.objects.filter(receiver = request.user.EMPLID))

        if (user_type == 0):

            #gets advising form status by checking Advising model for EMPLID match
            adv_form = Advising.objects.filter(author = request.user.EMPLID)
            adv_status = 0

            if len(adv_form) != 0:
                adv_form = list(adv_form)[0]
                adv_status = adv_form.status

            adv_message = ''

            if adv_status == 0:
                adv_message = "You have not been advised.  Please submit an advisement form."
            if adv_status == 1:
                adv_message = "Advisement form submitted, awaiting approval."
            if adv_status == 2:
                adv_message = "Advisement form submitted, awaiting final approval."
            if adv_status == 3:
                adv_message = "Advised.  Thank you for using QuickReg."
            return render(request, 'home.html', {
                'adv_message' : adv_message,
                'adv_status' : adv_status,
                'adv_form' : adv_form,
                'num_messages' : num_messages,
            })
        
        else:   

            if (user_type == 1):
                to_be_advised = Advising.objects.filter(total_credits__gte=45).filter(status = 1)
            else:
                to_be_advised = Advising.objects.filter(status = 2)
            
            num_advise = len(to_be_advised)

            if request.method=="POST":
                request.session['selected_id'] = request.POST.get('selected_form')
                #for some reason redirect works and render doesn't?
                #idk don't change it
                return redirect('view_advising_faculty')

            return render(request, 'home.html', {
                'to_be_advised' : to_be_advised,
                'num_messages' : num_messages,
                'num_advise' : num_advise,
            })

    return render(request, 'home.html')