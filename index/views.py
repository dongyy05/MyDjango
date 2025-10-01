from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.urls import resolve,reverse

def index(request):
    # kwargs={'year': 2010, 'month': 2, 'day': 3}
    # args=['2019', '12', '12']
    # print(reverse('index:mydate', args=args))
    # print(reverse('index:mydate', kwargs=kwargs))
    # return redirect(reverse('index:mydate', args=args))

    html = '<h1>Hello, Django!</h1>'
    return HttpResponse(html, status=200)


def indexView(request):
    c = ContentType.objects.values_list().all()
    print(c)
    return render(request, 'index.html')

def myvariable(request, year, month, day):
    return HttpResponse(f"{year}-{month}-{day}")

def index2(request, month):
    return HttpResponse('Variables other than routing address information is:'+" " +month)

def mydate(request, year, month, day):
    args=['2019', '12', '12']
    result=resolve(reverse('index:mydate', args=args))
    print('kwargs:', result.kwargs)
    print('url_name:', result.url_name)
    print('namespace:', result.namespace)
    print('view_name:', result.view_name)
    print('app_name:', result.app_name)

    return HttpResponse(str(year)+"-"+str(month)+"-"+str(day))

