from django.shortcuts import render, redirect
from app.forms import AcoesForm
from app.models import Acoes
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Acoes.objects.filter(descricao__icontains=search)
    else:
        data['db'] = Acoes.objects.all()
    
    #all= Acoes.objects.all()
    #paginator = Paginator(all, 10)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AcoesForm
    return render(request, 'form.html', data)

def create(request):
    form = AcoesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Acoes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Acoes.objects.get(pk=pk)
    data['form'] = AcoesForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Acoes.objects.get(pk=pk)
    form = AcoesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(resquest, pk):
    db = Acoes.objects.get(pk=pk)
    db.delete()
    return redirect('home')
