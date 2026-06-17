from abc import ABC, abstractmethod
from .models import Notificacao


# Contrato/Interface do Subject
class IObservable(ABC):

    @abstractmethod
    def registrar(self, observer):
        pass

    @abstractmethod
    def apagar(self, observer):
        pass

    @abstractmethod
    def notify(self,autor,destino,tipo,lida):
        pass

class Subject(IObservable):

    def __init__(self):
        self.observadores = set()

    def registrar(self, observer):
        self.observadores.add(observer)

    def apagar(self,observer):
        self.observadores.remove(observer)

    def notify(self, autor,destino,tipo):
        for observer in self.observadores:
            observer.notify(autor,destino,tipo)

class IObserver(ABC):

    @abstractmethod
    def notify(self, autor,destino,tipo):
        pass

class Observer(IObserver):

    def __init__(self, observable):
        observable.registrar(self)

    def notify(self, autor,destino,tipo):

        Notificacao.objects.create(autor=autor,destino=destino,tipo=tipo,lida=False)
        
