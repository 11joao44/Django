# Django for TASK EBAC

## Estrutura de um projeto Django

![alt text](/image/image.png)

## Get Started

**No Console CMD ou VScode**
```cmd 
django-admin startproject Djang_WebSite
```
```cmd
python manage.py startapp blog
```
![alt text](/image/image1.png)

```cmd
python manage.py migrate
```
```cmd
python manage.py runserver
```

## ORM - Mapeamento de Objeto Relacional

**Quando criando um novo modelo**
```cmd
python manage.py makemigrations
>>>
python manage.py migrate
```

```cmd
python manage.py createsuperuser
```

```cmd
python manage.py shell
```

## PyTest

![alt text](/image/image3.png)

## Views em Django

![alt text](/image/image4.png)

### Base View

![alt text](/image/image5.png)

```py
from django.http import HttpResponse
from django.views.generic import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
```

### Template View

```py
from django.views.generic.base import TemplateView

from articles.models import Article

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
```

### List View

```py
from django.views.generic.list import ListView
from django.utils import timezone

from articles.models import Artigo

class ArticleListView(ListView):

    model = Artigo

    def get_queryset(self, **kwargs):
        return Artigo.objects.filter(status='publicado')
```
