from re import I
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
from importlib.util import find_spec
from fastapi.staticfiles import StaticFiles


# Export Django settings env variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Get Django WSGI app
django_app = get_wsgi_application()

# Import a model
# And always import your models after you export settings
# and you get Django WSGI app
from django.contrib.auth import get_user_model
from test_faker.models import Person
from test_faker.views import PersonSerializer

Account = get_user_model()

# Create FasatAPI instance
app = FastAPI()

# Serve Django static files
app.mount('/static',
    StaticFiles(
         directory=os.path.normpath(
              os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
         )
   ),
   name='static',
)


#TEST FUNC FOR FASTAPI
@app.get('/users')
def get_users():
    s = PersonSerializer(Person.objects.all(), many=True)
    return s.data
    

# Mount Django app
app.mount('', WSGIMiddleware(django_app))