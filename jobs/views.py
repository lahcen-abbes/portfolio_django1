from django.shortcuts import render, get_object_or_404  #tretourner object yla ka kayn snn te3tina error 404
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id) #Job howa model ta3na représente objects f database w pk représente id ta3 jobs f database li tecréat lewla tmetel 1 zawja 2...
    #ro7na lel database dkhelna fl object lewla li créenaha kherjetlna hada lien http://127.0.0.1:8000/admin/jobs/job/1/change/ kima rak tchof 1 tema kon nbedlo 1 b 2 tedina 3nd li créeanaha zawja... 
    return render(request, 'jobs/detail.html', {'job' : job_detail})
