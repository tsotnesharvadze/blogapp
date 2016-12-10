from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
	
	def my_sort(a):
		return len(a.comment_set.all())
	postebis_sia=Post.objects.all()
	popularuli_postebi=[i for i in postebis_sia]
	popularuli_postebi.sort(key=my_sort,reverse=True)
	popularuli_postebi=popularuli_postebi[:5]

	paginator = Paginator(postebis_sia, 2) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page) 
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)

	return render(request,'app/new.html',{"postebis_sia":postebis_sia,
		"popularuli_postebi":popularuli_postebi,"contacts":contacts})


def srulad(request,posti_id):
	form=CommentForm()
	posti_srulad=Post.objects.get(pk=posti_id)
	if request.method=="POST":
		posti_srulad.comment_set.create(
			komentari=request.POST.get("new_comment"))
	return render(request,'app/srulad.html',{"posti":posti_srulad,"form":form})


