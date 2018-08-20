from django import forms

from . import models

class RegistrationLei(forms.ModelForm):

	class Meta:
		model = models.Lei
		fields = ('user', 'name', 'description', 'valid')
		labels = {
			'user': 'Usuário',
    		'name': 'Nome da Proposta',
    		'description': 'Descrição',
    		'valid': 'Validade'
    	}

class CommentForm(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = {'user', 'lei', 'comment'}
		labels = {
			'user': 'Usuário',
			'lei': 'Lei',
			'comment': 'Comentário'
		}
