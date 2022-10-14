from django.db import models
from django.conf import settings

# Create your models here.

# class Book(models.Model):             #   Classes are the blue-print for a data base tables
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     image = models.ImageField(upload_to="books", null=True)

#     def __str__(self):
#         return self.title
class Room(models.Model):             #   Classes are the blue-print for a data base tables
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books", null=True)

    def __str__(self):
        return self.title

# class Review(models.Model):
#     text = models.TextField()
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

#     def __str__(self):
#         return self.text[:50]
class Message(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text[:50]