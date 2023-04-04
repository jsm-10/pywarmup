from django.shortcuts import render, redirect
from .models import Libro, Autor, Editorial
from .forms import LibroForm

def home(request):
    libros = Libro.objects.all()
    return render(request, 'libros/home.html', {'libros': libros})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LibroForm


def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El libro ha sido agregado correctamente')
            return redirect('lista_libros')
    else:
        form = LibroForm()

    return render(request, 'agregar_libro.html', {'form': form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'libros/lista_autores.html', {'autores': autores})

def lista_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'libros/lista_editoriales.html', {'editoriales': editoriales})
