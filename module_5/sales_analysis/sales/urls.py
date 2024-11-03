from django.urls import path
from .views import load_sales_data, generate_report

urlpatterns = [
    path('upload/', load_sales_data, name='load_sales_data'),
    path('report/', generate_report, name='generate_report'),
]
