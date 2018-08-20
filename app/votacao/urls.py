from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as votacao

app_name = 'votacao'

urlpatterns = [
	path('', votacao.HomeView.as_view(template_name='votacao/index.html'), name='home'),
	path('proposta/<pk>', votacao.Proposta.as_view(), name='proposta'),
	#path('comment/', votacao.CommentView.as_view(), name='comment'),
	path('user/<pk>', votacao.UserView.as_view(), name='user-profile'),
	path('new/proposta', votacao.AddPropostaView.as_view(), name='add-proposta'),
]