from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post ,Comment
from .forms import CommentForm ,PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout

# Create your views here.
def index(request):
	
	def my_sort(a):
		return a.comment.count()
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

	context={
		"postebis_sia":postebis_sia,
		"popularuli_postebi":popularuli_postebi,
		"contacts":contacts,
		"user":request.user

		}
	return render(request,'app/new.html',context)


def srulad(request,posti_id):
	posti_srulad=Post.objects.get(pk=posti_id)
	form=CommentForm()
	if request.method =="POST":
		form=CommentForm(request.POST)
		if form.is_valid():
			a=form.save()
			
			posti_srulad.comment.add(a)

		
		
	return render(request,'app/srulad.html',{"posti":posti_srulad,"form":form})

def damateba(request):
	form=PostForm()
	if request.method=="POST":
		form=PostForm(request.POST ,request.FILES)
		if form.is_valid():
			post=form.save()
			print(post.id)
			return redirect("app:srulad",post.id)
	return render(request,'app/damateba.html',{"form":form})

