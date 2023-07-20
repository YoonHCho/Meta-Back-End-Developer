- Set up a new Django project in a virtual environment using pipenv.
- Use the virtual environment from the integrated terminal in VS Code.

1. First create a directory called LittleLemon `mkdir LittleLemon` and `cd` into the directory
2. `pipenv install django`
3. `pipenv shell` this will open a new shell session in the virtual environment for your project. Then use django admin to create a new django project in this directory. `django-admin startproject Littlelemon .`
4. `python manage.py startapp LittlelemonAPI` to create app for API
5. `python manage.py runserver`

Download and try Insomnia, GET & POST using https://httpbin.org/

How to convert a model instance to a JSON response
from django.forms.models import model_to_dict
from django.http from JsonResponse

book = Book.object.get(pk=16)
return JsonResponse(model_to_dic(book))

URL pattern -> for delete or editing `api/books/<int:pk>`

**Example JSON string or payload**

```
{
  "title": "Seawolf",
  "author": "Jack London"
}
```

However, you need to parse this string to access these individual data elements. To do this, use the QueryDict class from django.http module to parse the request body from this dictionary.

```
from django.http import QueryDict
...
request_body = QueryDict(request.body)

title = request_body.get('title')
```
