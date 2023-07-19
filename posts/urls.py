from django.urls import path
from .views import *

app_name = 'posts'
urlpatterns = [
    path('', MusHome.as_view(), name='home'),
    path('about/',  about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MusCategory.as_view(), name='category')
]
