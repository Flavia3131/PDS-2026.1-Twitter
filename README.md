# Projeto-de-Software-2026.1
https://miguelcastela.pythonanywhere.com/login/

# Funcionalidades já implementadas  

- Chat com suporte (inclusive para usuários anônimos)  
- Postagens  
- Curtidas  
- Republicações  
- Dislikes  
- Login  
- Cadastro  
- Alerta de senha incorreta  
- Comentários  
- Feed de publicações  

---

# Melhorias

- Postagem de imagens e vídeos  
- Salvar posts favoritos  
- Sistema de seguir usuários  
- Perfil de usuário com foto  
- Edição de perfil    
- Chat privado   
- Compartilhamento de posts  

---

# Herança já implementada  

Localizado na pasta `core`, no arquivo `models.py`:  

```python
class Post(models.Model)
```

A classe `Post` herda de `models.Model`.

```python
class Comentario(models.Model)
```

A classe `Comentario` herda de `models.Model`.

```python
class Suporte(models.Model)
```

A classe `Suporte` herda de `models.Model`.

---

# Uso do padrão Builder (Design Pattern Criacional)  

O Builder ajuda a resolver problemas causados por construtores com muitos parâmetros, permitindo criar objetos passo a passo. Ele foi usado para dividir o processo de criação de um post, que é um objeto complexo, em passos menores, para depois construir esse post conforme seu tipo, seja texto, imagem ou vídeo.

##   Builder

class PostBuilderProtocol(ABC):
class PostBuilder(PostBuilderProtocol):
class Director:

Então:  

- **Builder** → responsável por construir o post  
---

# Uso do padrão Observer (Design Pattern Comportamental) 

O Observer foi usado para notificar os usuários quando recebem uma solicitação para seguir ou quando for preciso aceitar a solicitação de um outro usuário. Assim, para a implementação desse padrão foram feitas 4 classes, sendo duas interfaces, ou seja, o contrato preciso para implementar o observer.

##   Observer

class IObservable(ABC):
class Subject(IObservable):
class IObserver(ABC):
class Observer(IObserver):

# Uso do padrão Decorator (Design Pattern Decorator)

O Decorator foi usado para adicionar funcionalidades extras na rede social. Obrigatoriamente precisa implementar os métodos da classe IComponent(ABC), então tanto class Component(IComponent) quanto class Decorator(IComponent) recebem como parâmetro class IComponent(ABC) para implementar métodos obrigatórios. Contudo, o Decorator tem as obrigatórias e as extras, como repost de um post, like e dislike.

##   Decorator

class IComponent(ABC):
class Component(IComponent):
class Decorator(IComponent):



