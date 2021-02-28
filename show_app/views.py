from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from time import gmtime, strftime

def index(request):
    return render(request, "index.html")

def allshows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def newshows(request):
    return render(request, "new_shows.html")

def submitshow(request):
    if request.method == "POST":
        show_ob = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
        return redirect(f'/shows/{show_ob.id}')

def show(request, show_id):
    context = {
        'details_show': Show.objects.filter(id=show_id),
    }
    return render(request, 'show.html', context)

def edit(request, show_id):
    curr_show = Show.objects.get(id=show_id)
    release_date = curr_show.release_date.strftime("%Y-%m-%d")

    context = {
        'show': curr_show,
        'release_date': release_date
    }
    print(curr_show.desc)
    print(curr_show.release_date)
    return render(request, "edit.html", context)

def submitedit(request, show_id):
    editshow = Show.objects.get(id=show_id)
    editshow.title = request.POST['title']
    editshow.network = request.POST['network']
    editshow.release_date = request.POST['release_date']
    editshow.desc = request.POST['desc']
    editshow.save()
    return redirect(f'/shows/{editshow.id}')


def delete(request, show_id):
    showdel = Show.objects.get(id=show_id)
    showdel.delete()
    return redirect('/shows')