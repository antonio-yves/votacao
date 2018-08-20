from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from datetime import datetime
from django.views import View
from django.http import HttpResponse

from .models import Lei, Comment
from .forms import RegistrationLei
from app.core.models import UUIDUser

class HomeView(ListView):
	model = Lei
	template_name = 'votacao/index.html'

	def get_context_data(self, **kwargs):
		kwargs['leis'] = Lei.objects.all().order_by('-create')
		return super(HomeView, self).get_context_data(**kwargs)

class PropostaView(DetailView):
	model = Lei
	template_name = 'votacao/proposta/index.html'

	def get_context_data(self, **kwargs):
		kwargs['comentarios'] = Comment.objects.filter(lei = self.object.id)
		return super(PropostaView, self).get_context_data(**kwargs)

class Proposta(View):
	def get(self, request, pk):
		kwargs = Lei.objects.filter(id = pk)
		print (kwargs)
		return render(request, 'votacao/proposta/index.html', {'object': kwargs})

class AddPropostaView(CreateView):
	model = Lei
	template_name = 'votacao/proposta/add-proposta.html'
	success_url = reverse_lazy('core:home')
	form_class = RegistrationLei

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.valid = datetime.now()
		obj.save()
		return super(AddPropostaView, self).form_valid(form)

class UserView(DetailView):
	model = UUIDUser
	template_name = 'votacao/user/profile.html'

	def get_context_data(self, **kwargs):
		kwargs['leis'] = Lei.objects.filter(user = self.object.id)
		return super(UserView, self).get_context_data(**kwargs)

class CommentView(DetailView):
	model = Lei
	template_name = 'votacao/proposta/comentario.html'
	success_url = reverse_lazy('core:proposta')




