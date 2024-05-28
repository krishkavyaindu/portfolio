from django.shortcuts import redirect,render, HttpResponse
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages
import pdfkit
from django.conf import settings
from .forms import ContactForm
from django.http import JsonResponse

# Create your views here.


def home(request):
    #contact form database
    # if request.method == 'POST':
    #     name == request.POST['name']
    #     email == request.POST['email']
    #     subject == request.POST['subject']
    #     message == request.POST['message']
    #     contact = models.Home(name=name, email=email, subject=subject, message=message)
    #     contact.save()
    return render(request, 'home.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
   
    print("Request method:", JsonResponse)
    # print("Request POST data:", request.POST)

    if request.method == "POST":
        name = request.POST.get('name')  
        email = request.POST.get('email')  
        subject = request.POST.get('subject')  
        message = request.POST.get('message') 
        # Perform your backend validation here, such as checking for empty fields, etc.
        if not name or not email or not subject or not message:
            return HttpResponse('All fields are required.')
        
      
        try:
            # contact = Contact(name=name, email=email, subject=subject, message=message)
            # contact.save()
            subject = subject
            message = message
            from_email = 'krishneduunnikrishnan@gmail.com '
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse('OK') 
        except Exception as e:
            return JsonResponse({'error': str(e)})
       
        
        
        
        

    return render(request, 'home.html')

def render_pdf_view(request):
    # Render your HTML content (assuming you have a template called 'template.html')
    html = render_to_string('template.html', {'data': 'Your data here'})
    
    # Configure pdfkit options if needed
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    
    # Convert HTML to PDF
    pdf = pdfkit.from_string(html, False, options=options)
    
    # Create the HTTP response with the PDF as an attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    
    return response

