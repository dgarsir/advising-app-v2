from django.urls import path
from .import views 
#from .views import ()
	#InboxListView,
urlpatterns = [
	path('send/',views.send_message,name='send_message'),
	#path('inbox/', InboxListView.as_view(), name='view_inbox'),
	path('inbox/', views.view_inbox, name='view_inbox'),
	path('delete/', views.delete_message, name='delete_message')
]

	