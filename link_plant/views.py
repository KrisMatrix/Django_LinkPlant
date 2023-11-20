from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link
from django.urls import reverse_lazy

# Create your views here.
class LinkListView(ListView):
  # if func based view, we would query for all the links
  # Link.objects.all()
  # context = {'link':links} 
  # return render(request, 'link_list.html', context)
  # But we are doing class based views.
  model = Link
  # my default looks for model_list.html -> link_list.html

class LinkCreateView(CreateView):
  # create forms.py file & form
  # check if this was a post or get request
  # return an empty form or save the form data
  model = Link
  fields = "__all__"
  success_url = reverse_lazy('link-list')
  # template model_form -> link_form.html

class LinkUpdateView(UpdateView):
  # create a form
  # check if a get request or a put request
  # either render the form or update and save in our db.
  model = Link
  fields = ['text', 'url']
  success_url = reverse_lazy('link-list')
  # template model_form -> link_form.html

class LinkDeleteView(DeleteView):
  # take in a id/pk of an object
  # query to db for that object
  # check if it exists -> delete the object
  # return some template or forward user to some url
  model = Link
  success_url = reverse_lazy('link-list')

## external profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)