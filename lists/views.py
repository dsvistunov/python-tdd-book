from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import FormView, CreateView, DetailView
from lists.forms import ItemForm, ExistingListItemForm, NewListForm
from lists.models import Item, List

User = get_user_model()


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)


class NewListView(CreateView):
    form_class = NewListForm
    template_name = 'home.html'

    def form_valid(self, form):
        list_ = form.save(owner=self.request.user)
        return redirect(list_)


class MyListView(DetailView):
    model = User
    template_name = 'my_lists.html'
    context_object_name = 'owner'


