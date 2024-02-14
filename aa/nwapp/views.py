from django.shortcuts import render, redirect
from nwapp.models import Registermodel
from nwapp.models import Book_Details
from nwapp.models import login


# Create your views here.
def viewdetails(request):
    obj = Registermodel.objects.all()
    return render(request, 'viewdetails.html', {'object': obj})


def index(request):
    if request.method == "POST":
        A = request.POST.get('first Name')
        print(A)
        B = request.POST.get('last Name')
        print(B)
        C = request.POST.get('number')
        print(C)
        D = request.POST.get('email')
        print(D)
        E = request.POST.get('psd')
        print(E)
        F = request.POST.get('uid')
        print(F)
        # H = request.POST.get('gen')
        # print(H)
        object = Registermodel.objects.create(firstname=A, lastname=B, mblenum=C, email=D, password=E, userid=F,
                                              gender=1)
        # try:
        #     check = Registermodel.objects.get(userid=usid,password=pswd)
        #     request.session['userid']=check.id
        #     return redirect('homepage')
        # except:
        #     pass

    return render(request, 'index.html')
    #
    # def register(request):
    #     if request.method=="POST":
    #
    # return render(request,'index.html')


def Book(request):
    if request.method == "POST":
        A = request.POST.get('Book_Name')
        print(A)
        B = request.POST.get('Author_Name')
        print(B)
        C = request.FILES['File_Data']
        print(C)
        D = request.POST.get('Status')
        print(D)

        object = Book_Details.objects.create(Book_Name=A, Author_Name=B, File_Data=C, Status=D
                                             )

    return render(request, 'Book.html')


def login(request):
    if request.method == "POST":
        A = request.POST.get('username')
        print(A)
        B = request.POST.get('password')
        print(B)
        try:
            obj = Registermodel.objects.get(userid=A, password=B)
            return redirect('viewdetails')
        except:
            pass
        # object= login.objects.create(uid=A,password=B,)

    return render(request, 'login.html')


def Book_Details1(request):
    obj = Book_Details.objects.all()
    return render(request, 'bookdetails.html', {'object': obj})
def newfunction():
    pass