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

# Melhorias planejadas  

- Postagem de imagens e vídeos  
- Salvar posts favoritos  
- Sistema de seguir usuários  
- Perfil de usuário com foto  
- Edição de perfil  
- Pesquisa de usuários e posts  
- Hashtags  
- Chat privado  
- Dark Mode  
- Compartilhamento de posts  
- Emojis/Reações nas publicações  

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

# Polimorfismo planejado  

A ideia é implementar diferentes tipos de posts utilizando polimorfismo:  

```python
PostTexto
PostImagem
PostVideo
```

Cada tipo de post terá comportamentos específicos, mas compartilhando a mesma estrutura base.

---

# Uso do padrão Builder (Design Pattern Criacional)  

O plano é utilizar o padrão Builder justamente na parte relacionada ao polimorfismo, separando a construção do objeto da sua representação.  

O Builder ajuda a resolver problemas causados por construtores com muitos parâmetros, permitindo criar objetos passo a passo. Já o polimorfismo permite que diferentes objetos respondam de maneiras diferentes utilizando a mesma chamada de método.  

A junção dos dois padrões parece uma boa solução para a estrutura do projeto, principalmente na parte de criação de diferentes tipos de posts.  

## Exemplo da ideia  

```python
builder = PostBuilder()

post = (
    builder
    .tipo("imagem")
    .texto("Olá")
    .imagem("foto.png")
    .build()
)
```

Então:  

- **Builder** → responsável por construir o post  
- **Polimorfismo** → responsável pelo comportamento específico de cada tipo de post  

---

# Observação  

Os planos descritos acima podem ser alterados conforme o desenvolvimento do projeto evoluir. No momento, esta é a arquitetura planejada.
