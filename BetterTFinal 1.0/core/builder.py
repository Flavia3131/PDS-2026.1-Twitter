from abc import ABC, abstractmethod
from .models import PostTexto,PostImagem,PostVideo


####### Parte do Builder ######

# Contrato/Interface
class PostBuilderProtocol(ABC):

    @abstractmethod
    def autor(self,autor):
        pass

    @abstractmethod
    def tipo(self,autor):
        pass

    @abstractmethod
    def texto(self,conteudo):
        pass

    @abstractmethod
    def imagem(self,conteudo):
        pass

    @abstractmethod
    def video(self,conteudo):
        pass

    @abstractmethod
    def build(self,tipo): 
        pass

# Implementação das funções obrigatórias 
class PostBuilder(PostBuilderProtocol):

    def __init__(self):
        self.post = {}

    def autor(self,autor):
        self.post["autor"] = autor 
        return self #retorna ele mesmo para seguir para o próximo método

    def tipo(self,tipo):
        self.post["tipo"] = tipo
        return self


    def texto(self,conteudo):
        campo = PostTexto.campo()

        self.post[campo] = conteudo

        return self

    def imagem(self,conteudo):
        campo = PostImagem.campo()

        self.post[campo] = conteudo

        return self

    def video(self,conteudo):
        campo = PostVideo.campo()

        self.post[campo] = conteudo

        return self

    def build(self,tipo):
        if tipo == "texto":
            # O ** é desempacotamento de dicionário
            return PostTexto.objects.create(**self.post)
        if tipo == "imagem":
            return PostImagem.objects.create(**self.post)
        if tipo == "video":
            return PostVideo.objects.create(**self.post)

# Responsável por Ordenar 
class Director:

    @staticmethod
    def construct(autor,tipo,conteudo):

        if tipo == "texto":
            return (PostBuilder()\
                .autor(autor)\
                .tipo(tipo)\
                .texto(conteudo)\
                .build(tipo)
            )
        
        elif tipo == "imagem":
            return (PostBuilder()\
                .autor(autor)\
                .tipo(tipo)\
                .imagem(conteudo)\
                .build(tipo)
            )
         
        elif tipo == "video":
            return (PostBuilder()\
                .autor(autor)\
                .tipo(tipo)\
                .video(conteudo)\
                .build(tipo)
            )
   
