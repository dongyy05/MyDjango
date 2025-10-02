from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.urls import resolve,reverse
from django.http.response import Http404,StreamingHttpResponse, FileResponse
def index(request):
    # 1.
    # kwargs={'year': 2010, 'month': 2, 'day': 3}
    # args=['2019', '12', '12']
    # print(reverse('index:mydate', args=args))
    # print(reverse('index:mydate', kwargs=kwargs))
    # return redirect(reverse('index:mydate', args=args))

    # 2.
    # html = '<h1>Hello, Django!</h1>'
    # return HttpResponse(html, status=200)

    # 3.
    # value = {'title': 'Hello, MyDjango!'}
    # return render(request, 'index.html', context=value)

    # 4.
    # title = {'key': 'Hello, MyDjango!'}
    # content = {'key': 'This is MyDjango!'}
    # return render(request, 'index.html', locals())

    return render(request, 'index.html')


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

def shop(request):
    return render(request, 'index.html')

def pag_not_found(request, exception):
    return render(request, '404.html', status=404)

def page_error(request):
    return render(request, '500.html', status=500)

def download1(request):
    file_path = 'index/Mystatic/1.jpeg'
    try:
        r = HttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=1.png'
        return r
    except Exception:
        raise Http404('Donwload error')
    
def download2(request):
    file_path = 'index/static/2.jpeg'
    try:
        r = StreamingHttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=2.png'
        return r
    except Exception:
        raise Http404('Donwload error')
    
def download3(request):
    file_path = 'static/3.jpeg'
    try:
        r = FileResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=3.png'
        return r
    except Exception:
        raise Http404('Donwload error')