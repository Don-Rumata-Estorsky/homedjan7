


from django.contrib import admin
from django.urls import path,include#  simple, stream
from app.views import listt
# from app.views import create_movie

# from .views import get_slug
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', listt),

]




