from django.shortcuts import render
from blogs.models import Post, Categoria

def blog(request):
    posts = Post.objects.all()
    return render(request, "blogs/blog.html", {'vPost': posts})

def categoria(request, categoria_id):
    vCategoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=vCategoria)
    return render(request, "blogs/categoria.html", {'categorias': vCategoria, 'vPost': posts})