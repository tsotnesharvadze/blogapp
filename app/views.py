from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
	
	def my_sort(a):
		return a.comment_set.count()
	postebis_sia=Post.objects.all()
	popularuli_postebi=[i for i in postebis_sia]
	popularuli_postebi.sort(key=my_sort,reverse=True)
	popularuli_postebi=popularuli_postebi[:5]

	paginator = Paginator(postebis_sia, 2) # Show 2 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page) 
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	page_num=contacts.number
	postebis_sia=postebis_sia[page_num*2-2:page_num*2]
	return render(request,'app/new.html',{"postebis_sia":postebis_sia,
		"popularuli_postebi":popularuli_postebi,"contacts":contacts})


def srulad(request,posti_id):
	posti_srulad=Post.objects.get(pk=posti_id)
	form=CommentForm()
	if request.method =="POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			print(request.POST)
			print("savestana")
			instance=form.save(commit=False)
			instance.post = Post.objects.get(pk=posti_id)
			print(instance)
			instance.save()
			
		
		
	return render(request,'app/srulad.html',{"posti":posti_srulad,"form":form})


