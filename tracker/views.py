from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Commission, ArchivedCommission
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


# Create your views here.
def index(request):
    active_commission_list = Commission.objects.order_by('creation_date')
    archived_commission_list = ArchivedCommission.objects.order_by('-completion_date')
    context = {
        'active_commission_list': active_commission_list,
        'archived_commission_list': archived_commission_list
        }
    return render(request, 'tracker/index.html', context)


def detail(request, commission_id):
    comm = get_object_or_404(Commission, pk=commission_id)
    return render(request, 'tracker/detail.html', {'commission': comm})


def archived_detail(request, archivedCommission_id):
    comm = get_object_or_404(ArchivedCommission, pk=archivedCommission_id)
    return render(request, 'tracker/archived-detail.html', {'archived_commission': comm})


def like(request, archivedCommission_id):
    comm = get_object_or_404(ArchivedCommission, pk=archivedCommission_id)
    comm.likes += 1
    comm.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('tracker:archived commission detail', args=(comm.id,)))
