from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import SubCityModel, WoredaModel, CabinetModel, GalleryModel, CommentModel, EventModel, VacancyModel,TenderModel, OfficeModel, NewsModel, HeadlineNewsModel, CarouselModel
from . forms import ComplaintForm

def navbar(request):
    subcity = SubCityModel.objects.all()
    context = {
        'subcity':subcity,
    }
    return render(request, 'navbar.html', context)

def footer(request):
    subcity = SubCityModel.objects.all()
    context = {
        'subcity':subcity,
    }
    return footer(request, 'footer.html',context)

def home(request):
    carouses = CarouselModel.objects.all()
    subcity = SubCityModel.objects.all()
    woredas = WoredaModel.objects.all()
    # cabinets = CabinetModel.objects.all()
    events = EventModel.objects.all()
    chief_executive = CabinetModel.objects.filter(cabinete_title = 'Chief Executive Manager')

    news = NewsModel.objects.all()
    selected_news = news[:3]

    offices = OfficeModel.objects.all()
    selected_items = offices[:4]
    
    context = {
        'subcity':subcity,
        'news':selected_news,
        'woredas':woredas,
        # 'cabinets':cabinets,
        'events':events,
        'selected_items':selected_items,
        'chief_executive':chief_executive,
        'carouses':carouses,
    }
    return render(request, 'home.html', context)

def feedback(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')  # Replace 'complaints:list' with the URL name of the page you want to redirect to after successful submission
    else:
        form = ComplaintForm()
    context = {
        'form':form,
    }
    return render(request, 'pages/feedback.html', context)

def about(request):
    subcity = SubCityModel.objects.all()
    context = {
        'subcity':subcity,
       
    }
    return render(request, 'pages/about.html', context)

def news(request):
    news = NewsModel.objects.all()
    headline_news = HeadlineNewsModel.objects.all()
    selected_news = headline_news[:1]

    not_recent_news = [n for n in news if not n.is_recent]
    paginator = Paginator(not_recent_news, 2)  # Display 10 posts per page
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)  # If page is not an integer, show the first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # If page is out of range, show the last page



    context = {
        'news' : news,
        'headline_news':selected_news,
        'posts':posts,
    }
    return render(request, 'pages/news.html', context)

def gallery(request):
    galleries = GalleryModel.objects.all()
    context = {
        'galleries':galleries,
    }
    return render(request, 'pages/gallery.html', context)

def chiefexecutive(request):
    # chief_executive = SubCityModel.objects.values('chief_executive_name','chief_executive_image','chief_executive_message').get(id=id)
    chief_executive = CabinetModel.objects.filter(cabinete_title = 'Chief Executive Manager')

    context = {
        'chief_executive':chief_executive,
    }
    return render(request, 'pages/chiefexecutive.html', context)

def cabinate(request):
    cabinets = CabinetModel.objects.all()
    context = {
        'cabinets':cabinets,
    }
    return render(request, 'pages/cabinate.html',context)

def structure(request):
    return render(request, 'pages/structure.html')

def woredas(request):
    woredas = WoredaModel.objects.all()
    context = {
        'woredas':woredas,
    }
    return render(request, 'pages/woredas.html', context)

def offices(request):
    offices = OfficeModel.objects.all()
    context = {
        'offices':offices,
    }
    return render(request, 'pages/offices.html', context)

def tender(request):
    tenders = TenderModel.objects.all()
    return render(request, 'pages/tender.html',{'tenders':tenders})

def vacancy(request):
    vacancies = VacancyModel.objects.all()
    return render(request, 'pages/vacancy.html', {'vacancies':vacancies})

def event(request):
    events = EventModel.objects.all()
    return render(request, 'pages/event.html', {'events':events})

# def carousel(request):
#     carouses = CarouselModel.objects.all()
#     return render(request, 'home.html', {'carouses':carouses})

