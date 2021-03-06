from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Word, WordBook, zoom
from django.template import RequestContext
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.cache import cache

class IndexView(ListView):
    model = WordBook
    paginate_by = 10
    ordering = ['teacher']

class ZoomView(ListView):
    template_name = 'words/zoom_list.html'
    context_object_name = 'object_list'
    queryset = zoom.objects.filter(see=True).order_by('cLass')

class WordLV(ListView):
    model = Word
    paginate_by = 20
    ordering = ['word']
    
    def get_queryset(self):
        words = cache.get('words')
        if not words:
            words = Word.objects.all()
            print("set",cache.set('words',words))
        return words
            


class WordDelV(LoginRequiredMixin, DeleteView):
    model = Word
    success_url = reverse_lazy('words')
    success_message = "Delete word successful"
    login_url = 'https://www.funvoca.com/admin/login/?next=/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        print("del",cache.delete('words'))
        return super(WordDelV, self).delete(request, *args, **kwargs)


class WordCV(LoginRequiredMixin, CreateView):
    model = Word
    fields = '__all__'
    login_url = 'https://www.funvoca.com/admin/login/?next=/'


class WordUV(LoginRequiredMixin, UpdateView):
    model = Word
    fields = '__all__'
    template_name_suffix = '_update_form'
    login_url = 'https://www.funvoca.com/admin/login/?next=/'

class WordDV(DetailView):
    model = Word
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class search_word(ListView):
    model = Word
    context_object_name = 'word_list'
    template_name = 'words/word_list.html'
    paginate_by = 20
    
    def get_queryset(self):
        q = self.request.GET.get('w','')
        if q=='':
            word_list = self.model.objects.all().order_by('word')
        else:
            word_list = self.model.objects.filter(word__icontains=q).order_by('word')
        return word_list

class search(ListView):
    model = WordBook
    context_object_name = 'wordbook_list'
    template_name = 'words/wordbook_list.html'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('wb','')
        if q == '':
            wordbook_list = self.model.objects.all().order_by('teacher')
        else:
            try:
                tmp = q.split()
                wordbook_list = self.model.objects.filter(teacher__icontains=tmp[0],_class__icontains=tmp[1]).order_by('title')
            except:
                wordbook_list = self.model.objects.filter(Q(teacher__icontains=q) | Q(_class__icontains=q)).order_by('title')
        return wordbook_list

def detail(request,pk):
    wordbook = WordBook.objects.get(id = pk)
    try:
        subject = wordbook.subjects.subject.first()
    except:
        subject = None
    try:
        verb = wordbook.verbs.verb.first()
    except:
        verb = None
    try:
        obj = wordbook.objs.obj.first()
    except:
        obj = None
    return render(request,'words/wordbook_detail.html', {'subject':subject, 'verb':verb, 'obj':obj, 'pk':pk})

def getNextVerb(request):
    wordbook = WordBook.objects.get(id = int(request.GET['pk']))
    try:
        verb = wordbook.verbs.verb.all()[int(request.GET['id'])+1]
        return HttpResponse(verb)
    except:
        raise Http404

def getPrevVerb(request):
    wordbook = WordBook.objects.get(id = int(request.GET['pk']))
    try:
        verb = wordbook.verbs.verb.all()[int(request.GET['id'])-1]
        return HttpResponse(verb)
    except:
        raise Http404

def getNextSub(request):
    wordbook = WordBook.objects.get(id = int(request.GET['pk']))
    try:
        sub = wordbook.subjects.subject.all()[int(request.GET['id'])+1]
        return HttpResponse(sub)
    except:
        raise Http404

def getPrevSub(request):
    wordbook = WordBook.objects.get(id = int(request.GET['pk']))
    try:
        sub = wordbook.subjects.subject.all()[int(request.GET['id'])-1]
        return HttpResponse(sub)
    except:
        raise Http404

def getNextObj(request):
    wordbook = WordBook.objects.get(id = int(request.GET['pk']))
    try:
        obj = wordbook.objs.obj.all()[int(request.GET['id'])+1]
        return HttpResponse(obj)
    except:
        raise Http404

def getPrevObj(request):
    wordbook = WordBook.objects.get(id = int(request.GET['pk']))
    try:
        obj = wordbook.objs.obj.all()[int(request.GET['id'])-1]
        return HttpResponse(obj)
    except:
        raise Http404


