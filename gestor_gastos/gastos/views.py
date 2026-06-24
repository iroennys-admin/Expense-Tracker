from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from .models import Gasto
from .forms import GastoForm

def home(request):
    gastos = Gasto.objects.all().order_by('-fecha')

    categoria_filtro = request.GET.get('categoria', '')
    if categoria_filtro:
        gastos = gastos.filter(categoria=categoria_filtro)

    total_general = gastos.aggregate(Sum('monto'))['monto__sum'] or 0

    totales_por_categoria = (
        Gasto.objects.values('categoria')
        .annotate(total=Sum('monto'))
        .order_by('-total')
    )

    categorias = [c[0] for c in Gasto.CATEGORIAS]

    context = {
        'gastos': gastos,
        'total_general': total_general,
        'totales_por_categoria': totales_por_categoria,
        'categorias': categorias,
        'categoria_filtro': categoria_filtro,
    }
    return render(request, 'gastos/home.html', context)

def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gasto guardado correctamente')
            return redirect('home')
    else:
        form = GastoForm()
    return render(request, 'gastos/formulario.html', {'form': form, 'titulo': 'Agregar gasto'})

def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        gasto.delete()
        messages.success(request, 'Gasto eliminado correctamente')
        return redirect('home')
    return render(request, 'gastos/confirmar_eliminar.html', {'gasto': gasto})

def editar(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gasto editado correctamente')
            return redirect('home')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'gastos/formulario.html', {'form': form, 'titulo': 'Editar gasto'})
