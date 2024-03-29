import uuid
from django.shortcuts import render
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from rest_framework import viewsets
from cadastro_animal.serializers import AnimalSerializer

# Create your views here.

def home(request):
   # Filtrar apenas os animais que não foram adotados
    list_animals = Animal.objects.filter(adotado=False)
  
    return render(request, 'home.html',{'list_animals':list_animals});

def criar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.id = uuid.uuid4()
            animal.save()
            form = AnimalForm()  # Limpar o formulário após salvar
    else:
        form = AnimalForm()
    return render(request, 'cadastro.html', {'form': form})

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
# Create your views here
