from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Libro, Editorial
from .forms import NuevoLibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca_app/lista_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = NuevoLibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = NuevoLibroForm()
    return render(request, 'biblioteca_app/agregar_libro.html', {'form': form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores})

def lista_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'biblioteca/lista_editoriales.html', {'editoriales': editoriales})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})
