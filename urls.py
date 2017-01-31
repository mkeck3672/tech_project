from django.conf.urls import url
from . import views

app_name = 'food'
urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^details/(?P<f_name>)/', views.details, name='details'),
	url(r'^details/(.+)/', views.details, name='details'),
	url(r'^details/',views.details, name='details'),
	url(r'^submit/(?P<pk>\d+)/', views.submit, name='submit'),
	url(r'^showAll/$', views.showAll, name='showAll'),
	url(r'^delete/$', views.delete, name='delete'),






	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	

#	url(r'^$', include('food.urls')),
   	#url(r'^admin/', admin.site.urls),
	
	#url(r'^$', views.IndexView.as_view(), name='index'),
      #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
] 
