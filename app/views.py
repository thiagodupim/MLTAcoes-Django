from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser  
from app.api.serializers import AcoesSerializer
from django.shortcuts import render, redirect
from app.forms import AcoesForm
from app.models import Acoes
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role


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

@api_view(['GET', 'POST', 'DELETE'])
def app_list(request):
    if request.method == 'GET':
        app = Acoes.objects.all()
        
        descricao = request.GET.get('descricao', None)
        if descricao is not None:
            app = app.filter(descricao__icontains=descricao)
        
        app_serializer = AcoesSerializer(app, many=True)
        return JsonResponse(app_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        app_data = JSONParser().parse(request)
        app_serializer = AcoesSerializer(data=app_data)
        if app_serializer.is_valid():
            app_serializer.save()
            return JsonResponse(app_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Acoes.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def app_detail(request, pk):
    try:
        app = Acoes.objects.get(pk=pk)
        if request.method == 'GET': 
            app_serializer = AcoesSerializer(app) 
            return JsonResponse(app_serializer.data) 
        
        elif request.method == 'PUT': 
            app_data = JSONParser().parse(request) 
            app_serializer = AcoesSerializer(app, data=app_data) 
            if app_serializer.is_valid(): 
                app_serializer.save() 
                return JsonResponse(app_serializer.data) 
            return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            
        elif request.method == 'DELETE': 
            app.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    except Acoes.DoesNotExist:
        return JsonResponse({'message': 'The ação does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def app_list_published(request):
    app = Acoes.objects.filter(published=True)
        
    if request.method == 'GET': 
        app_serializer = AcoesSerializer(app, many=True)
        return JsonResponse(app_serializer.data, safe=False)