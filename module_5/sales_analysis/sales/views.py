import pandas as pd
from django.shortcuts import render
from .models import SalesData, SalesReport
from .forms import UploadFileForm
from django.db.models import Sum

def load_sales_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)

            # Example preprocessing
            df['date'] = pd.to_datetime(df['date'])
            df['sales_amount'] = df['sales_amount'].astype(float)

            # Save to the database
            for _, row in df.iterrows():
                SalesData.objects.create(
                    product_name=row['product_name'],
                    sales_amount=row['sales_amount'],
                    date=row['date']
                )

            return render(request, 'upload_success.html')

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

'''
def generate_report(request):
    # Aggregate sales data by month
    monthly_sales = (
        SalesData.objects.values('date__year', 'date__month')
        .annotate(total_sales=Sum('sales_amount'))
        .order_by('date__year', 'date__month')
    )

    # Get top-selling products
    top_products = (
        SalesData.objects.values('product_name')
        .annotate(total_sales=Sum('sales_amount'))
        .order_by('-total_sales')[:5]
    )

    context = {
        'monthly_sales': monthly_sales,
        'top_products': top_products,
    }
    return render(request, 'report.html', context)
'''

from django.db.models import Sum, Q

def generate_report(request):
    # Aggregate monthly sales data
    monthly_sales = (
        SalesData.objects.values('date__year', 'date__month')
        .annotate(total_sales=Sum('sales_amount'))
        .order_by('date__year', 'date__month')
    )

    # Get top-selling products
    top_products = (
        SalesData.objects.values('product_name')
        .annotate(total_sales=Sum('sales_amount'))
        .order_by('-total_sales')[:5]
    )

    # Calculate quarterly sales
    quarterly_sales = (
        SalesData.objects.values('date__year')
        .annotate(
            Q1=Sum('sales_amount', filter=Q(date__month__in=[1, 2, 3])),
            Q2=Sum('sales_amount', filter=Q(date__month__in=[4, 5, 6])),
            Q3=Sum('sales_amount', filter=Q(date__month__in=[7, 8, 9])),
            Q4=Sum('sales_amount', filter=Q(date__month__in=[10, 11, 12]))
        )
        .order_by('date__year')
    )

    context = {
        'monthly_sales': monthly_sales,
        'top_products': top_products,
        'quarterly_sales': quarterly_sales,  # Pass the new data to the template
    }
    return render(request, 'generate_report.html', context)

def generate_report(request):
    # Aggregate monthly sales data
    monthly_sales = (
        SalesData.objects.values('date__year', 'date__month')
        .annotate(total_sales=Sum('sales_amount'))
        .order_by('date__year', 'date__month')
    )

    # Get top-selling products
    top_products = (
        SalesData.objects.values('product_name')
        .annotate(total_sales=Sum('sales_amount'))
        .order_by('-total_sales')[:5]
    )

    # Calculate quarterly sales
    quarterly_sales = (
        SalesData.objects.values('date__year')
        .annotate(
            Q1=Sum('sales_amount', filter=Q(date__month__in=[1, 2, 3])),
            Q2=Sum('sales_amount', filter=Q(date__month__in=[4, 5, 6])),
            Q3=Sum('sales_amount', filter=Q(date__month__in=[7, 8, 9])),
            Q4=Sum('sales_amount', filter=Q(date__month__in=[10, 11, 12]))
        )
        .order_by('date__year')
    )

    context = {
        'monthly_sales': monthly_sales,
        'top_products': top_products,
        'quarterly_sales': quarterly_sales,  # Pass the new data to the template
    }
    return render(request, 'generate_report.html', context)
