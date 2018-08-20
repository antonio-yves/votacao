from django.db import models
from app.core.models import CreateUpdateModel, UUIDUser

class Lei(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='users', verbose_name='Usuário')
	name = models.CharField(max_length = 255, verbose_name = 'Nome')
	description = models.TextField(verbose_name = 'Descrição') 
	favor = models.IntegerField(verbose_name = 'Votos a favor', default = 0)
	contra = models.IntegerField(verbose_name = 'Votos contra', default = 0)
	create = models.DateTimeField(auto_now_add = True, blank = False, verbose_name = 'Data de Criação')
	valid = models.DateTimeField(verbose_name = 'Data Máxima', blank = False)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Lei'
		verbose_name_plural = 'Leis'

class Comment(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='user', verbose_name='Usuário')
	lei = models.ForeignKey(Lei, on_delete=models.CASCADE, related_name='leis', verbose_name='Lei')
	comment = models.TextField(verbose_name='Comentário')

	def __str__(self):
		return self.comment

	class Meta:
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'





