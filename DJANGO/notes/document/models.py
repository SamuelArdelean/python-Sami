from django.db import models

class Document(models.Model):   #pentru crearea unui tabel, clasa Document care mosteneste pachetul models.Model
    title=models.CharField(max_length=255)   #fiecare camp din baza de date reprezinta o variabila, Charfield- e string
    content=models.TextField(blank=True,null=True)  #pot sa ramana necompletate

    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('title',)  #documentele sunt ordonate in functie de titlu

#modelarea aplicatiilor in baza de date se realizeaza prin intermediul fisierului models.py
