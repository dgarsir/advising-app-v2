from django.shortcuts import render, redirect, HttpResponse
from .forms import MessageCreationForm
from .models import Message
from users.models import CustomUser
from django.db.models import Count

def send_message(request):
	if request.method == "POST":
		form = MessageCreationForm(request.POST)
		if form.is_valid():
			m_form = form.save(commit=False)
			m_form.sender = request.user
			m_form.save()
			return redirect('home')
	else:
		form = MessageCreationForm()

	return render(request, 'send_message.html', {'form': form})

def view_inbox(request):
	num_messages = Message.objects.filter(receiver = request.user).count()
	#num_messages = len(Message.objects.filter(receiver = request.user))
	user_list = CustomUser.objects.all()
	return render(request, 'view_messages.html', {
		'messages' : Message.objects.all(),
		'num_messages' : num_messages,
		'user_list' : user_list,
	})

def delete_message(request):
	inbox = list(Message.objects.filter(receiver = request.user))
	if request.method == "POST":
		Message.objects.filter(pk = request.POST.get('to-delete')).delete()
		return redirect('delete_message')
	return render(request, 'delete_message.html',{'inbox': inbox})
















