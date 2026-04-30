# Projeto-de-Software-2026.1
https://miguelcastela.pythonanywhere.com/login/
class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length=280)
    data = models.DateTimeField(auto_now_add=True)

  curtidas = models.ManyToManyField(User, related_name='curtidas', blank=True)
  dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
  salvados = models.ManyToManyField(User, related_name='salvados', blank=True)


  republicado_de = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f'{self.autor.username} em {self.post.id}'

        LOCALIZADO NA PASTA CORE E NO ARQUIVO "MODELS.PY"

class Post(models.Model): -> A classe Post herda de models.Model.

class Comentario(models.Model): -> A classe Comentario herda de models.Model.

class Suporte(models.Model): -> A classe Suporte herda de models.Model.

      E O POLIMORFISMO TEM UM "TIPO" DELE TAMBÉM NO MODELS.PY
 def __str__(self):
        return f'{self.autor.username} em {self.post.id}'

      QUE SERIA UM "Method Overriding"
