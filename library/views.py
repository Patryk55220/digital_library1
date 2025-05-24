from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    paginate_by = 10
    template_name = "library/book_list.html"
    def get_queryset(self):
        qs = super().get_queryset().select_related("author")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(author__last_name__icontains=q)
            )
        if self.request.GET.get("available") == "1":
            qs = [b for b in qs if b.is_available]
        return qs

class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"

class BookCreateView(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:book-list")

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:book-list")

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("library:book-list")
