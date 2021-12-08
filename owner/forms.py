from django import forms
from django.forms import ModelForm
from owner.models import Book,Order


class BookForm(ModelForm):

    # book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # # author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-width"}))
    # price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    # copies=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    class Meta:
        model=Book
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"})
        }
        labels={
            "book_name":"Bookname"
        }
    def clean(self):
        # print("validation")
        cleaned_data=super().clean()
        book_name=cleaned_data['book_name']
        price=cleaned_data['price']
        copies=cleaned_data['copies']
        books=Book.objects.filter(book_name=book_name)
        if books:
            msg="Book with this name already exists"
            self.add_error("book_name",msg)
        if int(price)<0:
            msg="invalid price"
            self.add_error("price",msg)
        if int(copies)<0:
            msg="invalid copies"
            self.add_error("copies",msg)


class RegistrationForm(forms.Form):

    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    user_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password1=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        print("Validation")


class LoginForm(forms.Form):

    user_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean(self):
        print("Validation")


class BookEditForm(ModelForm):
    # book_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    class Meta:
        model=Book
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"})
        }
        labels={
            "book_name":"Bookname"
        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data['price']
        copies=cleaned_data['copies']
        if int(price)<0:
            msg="invalid price"
            self.add_error("price",msg)
        if int(copies)<0:
            msg="invalid copies"
            self.add_error("copies",msg)


class BookSearchForm(forms.Form):
    book_name=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","required":False}))


class DashEditForm(ModelForm):
    class Meta:
        model=Order
        fields=["status","expected_deliverydate"]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "expected_deliverydate":forms.DateInput(attrs={"type":"date"})
        }