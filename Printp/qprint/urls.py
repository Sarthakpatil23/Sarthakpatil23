from django.urls import path
from .views import first_page, landing_page, select_college, select_printing_shop, upload_file, upload_success, about_page

urlpatterns = [
    path('', first_page, name='first_page'),
    path('landing/', landing_page, name='landing_page'),
    path('select-college/', select_college, name='select_college'),
    path('select_printing_shop/<int:college_id>/', select_printing_shop, name='select_printing_shop'),
    path('upload_file/<int:college_id>/<int:shop_id>/', upload_file, name='upload_file'),
    path('upload-success/', upload_success, name='upload_success'),
    path('about/', about_page, name='about_page'),
]