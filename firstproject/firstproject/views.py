from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from.forms import usersForm
from service.models import Service
from contactenquiry.models import contactEnquiry
from news.models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Home Page
def homepage(request):
    send_mail(
        'Testing Mail',
        'here is the message',
        'aa@gmail.com',
        ['bb@gmail.com'], #where to send msg
        fail_silently=False 
    )
    
    # for a in servicesData:
    #     print(a)

   
    # You can pass data if needed
    # data = {
    #     "title": "Home Page",
    #     "bdata": "Welcome to Home page | welcome",
    #     "clist": ["python", "django", "react", "java"],
    #     "numbers": [10, 20, 30, 40, 50, 60],
    #     "student_details": [
    #         {'name': 'govinda', 'phone': 1233443},
    #         {'name': 'bhandara', 'phone': 7543357}
    #     ],
    # }
    # return render(request, "passdata.html", data)

    return render(request, "index.html")
def newsDetail(request, slug):
    news_detail = News.objects.get(news_slug=slug)  # fetch the news object by id
    return render(request, "newsdetail.html", {"newsDetail": news_detail})


# About Page
def about(request):
    return render(request, "about.html")

def saveEnquiry(request):
    n=""
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        en=contactEnquiry(name=name,email=email,message=message)
        en.save()
        n='Data Inserted'

    return render(request, "contact.html",{'n':n})
    


# Contact Page
def contact(request):
    final=None
    if request.method=="GET":
        final=request.GET.get('final')
    return render(request, "contact.html",{'final':final})

def projects(request):
    return render (request, "projects.html")

def submitform(request):
    final = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            final = f"Name: {name}, Email: {email}, Message: {message}"

            # url="/contact/?final={}".format(final)
            return HttpResponse(final)
        else:
            final = "Please fill in all fields."

def service(request):
    servicesData=Service.objects.all()
    paginator = Paginator(servicesData,2)
    page_no = request.GET.get('page')
    ServiceDataFinal = paginator.get_page(page_no)
    total_page=ServiceDataFinal.paginator.num_pages
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            servicesData= Service.objects.filter(service_title__icontains=st)
    data= {
        'servicesData':servicesData,
        'servicesData':ServiceDataFinal,
        "lastpage":total_page,
        'totalpagelist':[n+1 for n in range(total_page)]
    }
    return render(request,"service.html",data)


# Course Page
def course(request):
    return HttpResponse("Welcome to course page.")


# Course Details Page with Dynamic ID
def courseDetails(request, courseid):
    return HttpResponse(f"Course ID is: {courseid}")

def userform(request):
    final = ""
    fn=usersForm()

    data={'form':fn}    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
       
        if name and email and message:
            final = f"Name: {name}, Email: {email}, Message: {message}"
            data={
                'form':fn,
                'final':final
            }
            url="/contact/?final={}".format(final)
            return HttpResponseRedirect(url)
        else:
            final = "Please fill in all fields."

    return render(request, 'userform.html',data)
