from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Service, Category
from .forms import ServiceForm

# Create your views here.


def all_services(request):
    """ All Services View """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """Services Detail View """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('add_service'))
        else:
            messages.error(request, 'Failed to add Service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)