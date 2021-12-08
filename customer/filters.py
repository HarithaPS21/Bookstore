import django_filters
from owner.models import Book

class BookFilter(django_filters.FilterSet):
    book_name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=Book
        fields=["author","price"]