from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UploadForm, PrintingShopForm, CollegeForm
from .models import UploadedFile, PrintingShop, College

def first_page(request):
    return render(request, 'qprint/first_page.html')

def landing_page(request):
    return render(request, 'qprint/landing_page.html')

def select_college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.cleaned_data['college']
            return redirect('select_printing_shop', college_id=college.id)
    else:
        form = CollegeForm()
    return render(request, 'qprint/select_college.html', {'form': form})

def select_printing_shop(request, college_id):
    if request.method == 'POST':
        form = PrintingShopForm(request.POST, college_id=college_id)
        if form.is_valid():
            printing_shop = form.cleaned_data['printing_shop']
            return redirect('upload_file', college_id=college_id, shop_id=printing_shop.id)
    else:
        form = PrintingShopForm(college_id=college_id)
    return render(request, 'qprint/select_printing_shop.html', {'form': form, 'college_id': college_id})

def upload_file(request, college_id, shop_id):
    printing_shop = get_object_or_404(PrintingShop, id=shop_id)
    recipient_email = "sarthakpatil2194@gmail.com"  # Replace with the email address you want to send the file to
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            color_option = form.cleaned_data['color_option']
            print_option = form.cleaned_data['print_option']
            additional_instructions = form.cleaned_data['additional_instructions']
            time_limit = form.cleaned_data['time_limit']
            
            # Send the uploaded file via email
            email = EmailMessage(
                subject=f"New File Uploaded: {name}",
                body=f"A new file has been uploaded.\n\nName: {name}\nColor Option: {color_option}\nPrint Option: {print_option}\nAdditional Instructions: {additional_instructions}\nTime Limit: {time_limit}",
                from_email="patilurmila584@gmail.com",  # Replace with your email address
                to=[recipient_email],
            )
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            
            messages.success(request, 'File uploaded and sent successfully.')
            return redirect('upload_success')
    else:
        form = UploadForm()
    
    return render(request, 'qprint/upload_file.html', {'form': form, 'shop_id': shop_id, 'college_id': college_id})

def upload_success(request):
    return render(request, 'qprint/upload_success.html')

def about_page(request):
    return render(request, 'qprint/about.html')
#sarthakpatil2194@gmail.com
#patilurmila584@gmail.com