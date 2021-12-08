from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True,blank=True)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    category=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name


class Order(models.Model):
    product=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    address=models.CharField(max_length=120)
    options=(
        ("ordered","ordered"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("in_transit","in_transit")
    )
    status=models.CharField(max_length=30,choices=options,default="ordered")
    phone_number=models.CharField(max_length=12)
    expected_deliverydate=models.DateField(null=True)

# product
# user
# address
#














# python manage.py makemigrations  ->  creates a querry file to generate querries corresponding to changes
# python manage.py migrate  ->  apply changes to the database (sqlite by default)

# python manage.py shell

# insert into book(book_name,author,price,copies) values("randamoozham","mt",200,210); mysql
# orm (object relational mapper)


# orm querry for creating an object:
# reference= ModelName(field_name=value,field_name=value,field_name=value,field_name=value)
# reference.save()

# book=Book(book_name="randamoozham",author="mt",price=200,copies=210)
# book.save()


# select * from Book;
# fetching all records from model:

# reference=modelname.objects.all()
# books=Book.objects.all()

# for book in books:
#     print(book.book_name)
#     print(book.author)
#     print(book.price)
#     print(book.copies)


# orm querry for fetching a special record:
# reference=ModelName.objects.get(field_name=value)
# book=Book.objects.get(id=1)


# orm querry for updating a specific record:
# book=Book.object.get(id=1)
# book.price=250
# book.save()

# orm for displaying book_name of all books whose price<300 :
# books=Book.objects.filter(price__lt=300)
# books

# orm to display book_name of all books whose price <=300 :
# books=Book.objects.filter(price__lte=300)
# books

# orm to display book_name of all books whose price >300 :
# books=Book.objects.filter(price__gt=300)
# books

# orm to display book_name of all books whose price>=300 :
# books=Book.objects.filter(price__gte=300)
# books

# orm to display book_name of all books whose category="novel" :
# books=Book.objects.filter(category="novel")
# books

# books=Book.objects.filter(book_name__iexact="randamoozham")
# books

# books=Book.objects.filter(book_name__contains="ra")
# books

# books=Book.objects.all().order_by("-price")
# books

# book=Book.objects.get(id=4)
# book
# book.delete()

