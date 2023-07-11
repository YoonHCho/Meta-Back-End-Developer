# This is to handle errors in Views and this views.py must be in the project level.

# views.py
from django.http import HttpResponse,

# handler404 handles all the pages not found by the URL conf file
def handler404(request, exception):
    return HttpResponse('404: Page not found!')

# urls.py
# add the error handling
handler404 = 'myproject.views.handler404'