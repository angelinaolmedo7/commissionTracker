from django.http import HttpResponse, Http404
from .models import Commission, ArchivedCommission
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    active_commission_list = Commission.objects.order_by('creation_date')
    context = {'active_commission_list': active_commission_list}
    return render(request, 'tracker/index.html', context)


def detail(request, commission_id):
    comm = get_object_or_404(Commission, pk=commission_id)
    return render(request, 'tracker/detail.html', {'commission': comm})


def archived_detail(request, archivedCommission_id):
    comm = get_object_or_404(ArchivedCommission, pk=archivedCommission_id)
    return render(request, 'tracker/detail.html', {'archived_commission': comm})
