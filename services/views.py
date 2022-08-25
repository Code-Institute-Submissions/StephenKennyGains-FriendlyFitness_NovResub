""" Services App Views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Category
from .forms import ServiceForm

# Create your views here.


def all_services(request):
    """ All Services View """

    services = Service.objects.all()

    # service separated will go here
    services_by_category = {}

    # iterate over all services and seperate them
    for service in list(services):

        # get category name
        category = service.category

        # check if key exists
        category_exists = services_by_category.get(category)

        # if it doesnt exist, create the key and add to it
        if not category_exists:
            services_by_category[category] = []

        # add the service to it
        services_by_category[category].append(service)

    context = {
        'services': services,
        'services_by_category': services_by_category,
        }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """Services Detail View """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


@login_required
def add_service(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to add Service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('services'))
