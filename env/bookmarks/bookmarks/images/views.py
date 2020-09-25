from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        # The form was sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # Adding an user to the created object
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            # Redirecting an user to the saved photo page
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})
