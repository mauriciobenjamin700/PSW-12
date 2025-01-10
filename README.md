# Aprendendo a Criar API's Com Django

## Comandos básicos

Cria o núcleo do projeto e salva na pasta `core`, mas você pode trocar core pelo nome que preferir

```bash
django-admin startproject core .
```

Cria um novo módulo para o projeto em Django, neste caso o modulo se chama `shortener` mas pode ser qualquer nome

```bash
python3 manage.py startapp shortener
```

Move o novo modulo para dentro da pasta apps, organizando melhor o código. Lembre-se de acessar o `core` do seu projeto e adicionar na constante `INSTALLED_APPS` o caminho novo, ex: `apps.shortener`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.shortener'
]
```

```bash
mv shortener apps/
```

Abra o novo modulo e acesse o arquivo apps.py, altere o nome do modulo de `shortener` para `apps.shortener` de forma que o django entenda que o novo modulo está dentro da pasta `apps`.

```python
from django.apps import AppConfig


class ShortenerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.shortener'

```



Cria um servidor local para os testes e visualizações

```bash
python3 manage.py runserver
```
