from abc import ABC, abstractmethod
from .models import Post,PostTexto,PostImagem,PostVideo,User,Comentario, Salvar


class IComponent(ABC):

    @abstractmethod
    def comentar(self, post_id, post_tipo, texto, idUser):
        pass

    @abstractmethod
    def salvar_post(self, post_id, idUser):
        pass

class Component(IComponent):

    def comentar(self, post_id, post_tipo, texto, idUser):
      autor = User.objects.get(id=idUser)

      if post_tipo == 'texto':
        print("chegou post_tipo texto")
        post = PostTexto.objects.get(id=post_id)

      if post_tipo == 'imagem':
        post = PostImagem.objects.get(id=post_id)

      if post_tipo == 'video':
        post = PostVideo.objects.get(id=post_id)

        # criando um comentario em um post que ja existe
      print("chegou no regisrar comentario no banco")
      Comentario.objects.create(autor=autor, post=post, texto=texto)

    def salvar_post(self, post_id, idUser):
        autor = User.objects.get(id=idUser)
        
        post = Post.objects.get(id=post_id)

        if not Salvar.objects.filter(
            salvos=autor,
            post=post
            
        ).exists():
            Salvar.objects.create(salvos=autor,post=post)

class Decorator(IComponent): 
   
   def __init__(self, obj):
      self.object = obj

   def comentar(self, post_id, post_tipo, texto, idUser):
      return self.object.comentar(post_id, post_tipo, texto, idUser)
   
   def salvar_post(self, post_id, idUser):
      return self.object.salvar_post(post_id, idUser)
   
   def curtir_post(self, post_id, idUser):
     autor = User.objects.get(id=idUser) 
     post = Post.objects.get(id=post_id)

     if autor in post.curtidas.all():
        post.curtidas.remove(autor)
     else:
        post.curtidas.add(autor)
        post.dislikes.remove(autor)
   
   def dislike_post(self, post_id, idUser):
     autor = User.objects.get(id=idUser)
     post = Post.objects.get(id=post_id)

     if autor in post.dislikes.all():
        post.dislikes.remove(autor)
     else:
        post.dislikes.add(autor)
        post.curtidas.remove(autor)
   
   def republicar_post(self, post_id, idUser):
     origi = Post.objects.get(id=post_id)
     autor = User.objects.get(id=idUser)

     if origi.tipo == "texto":
       original = PostTexto.objects.get(id=post_id)
       PostTexto.objects.create(autor=autor, tipo=original.tipo, texto=original.texto, republicado_de=original)

     if origi.tipo == "imagem":
       original = PostImagem.objects.get(id=post_id)
       PostImagem.objects.create(autor=autor, tipo=original.tipo, imagem=original.imagem, republicado_de=original)

     if origi.tipo == "video":
       original = PostVideo.objects.get(id=post_id)
       PostVideo.objects.create(autor=autor, tipo=original.tipo, video=original.video, republicado_de=original)
