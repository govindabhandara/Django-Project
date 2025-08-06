from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from.forms import usersForm
from service.models import Service

# Home Page
def homepage(request):
    
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


# About Page
def about(request):
    return render(request, "about.html")


# Contact Page
def contact(request):
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
    servicesData=Service.objects.all().order_by('id')[:3]
    data= {
        'servicesData':servicesData
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
