from django.shortcuts import render,redirect
from .models import Document

def editor(request):
    docid=int(request.GET.get('docid', 0))   # atribuim id-ul fiecarui document
    documents=Document.objects.all()  # atribuim toate documentele in baza de date

    if request.method=='POST': #metoda prin care atribuim scrierea noului document
        docid=int(request.POST.get('docid', 0))
        title=request.POST.get('title')
        content=request.POST.get('content','')

        if docid>0:  #adaugarea informatiilor si salvarea documentului
            document=Document.objects.get(pk=docid)
            document.title=title
            document.content=content
            document.save()

            return redirect('/?docid=%i'% docid)

        else:
            document=Document.objects.create(title=title, content=content)


    if docid>0:   #functia prin care salvam documentele si le atribuim variabilei document
        document=Document.objects.get(pk=docid)
    else:
        document=''

    context ={    # am creat un dictionar sa le avem organizate
        'docid':docid,
        'documents':documents,
        'document':document
    }

    return render(request, 'editor.html',context)

def delete_document(request, docid):
    document=Document.objects.get(pk=docid)
    document.delete()

    return redirect('/?docid=0')