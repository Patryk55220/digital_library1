# library/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView, TemplateView
)

from .models import Book, Loan
from .forms  import BookForm, LoanForm


class BookListView(ListView):
    model               = Book
    template_name       = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        qs = super().get_queryset().select_related('author')
        q  = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(author__name__icontains=q)
            )
        if self.request.GET.get('available') == '1':
            qs = [b for b in qs if b.is_available]
        return qs


class BookDetailView(DetailView):
    model         = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    form_class    = BookForm
    template_name = 'library/book_form.html'
    success_url   = reverse_lazy('library:book-list')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model         = Book
    form_class    = BookForm
    template_name = 'library/book_form.html'
    success_url   = reverse_lazy('library:book-list')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model         = Book
    template_name = 'library/book_confirm_delete.html'
    success_url   = reverse_lazy('library:book-list')


class LoanCreateView(LoginRequiredMixin, CreateView):
    model         = Loan
    form_class    = LoanForm
    template_name = 'library/loan_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.book = get_object_or_404(Book, pk=kwargs['pk'])
        if not self.book.is_available:
            return HttpResponseForbidden('Ta książka jest już wypożyczona.')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.book
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('library:book-detail', args=[self.book.pk])


class LoanReturnView(LoginRequiredMixin, DeleteView):
    model         = Loan
    template_name = 'library/loan_confirm_return.html'

    def get_object(self, queryset=None):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        return get_object_or_404(Loan, book=book)

    def get_success_url(self):
        return reverse_lazy('library:book-detail', args=[self.kwargs['pk']])


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'library/profile.html'
