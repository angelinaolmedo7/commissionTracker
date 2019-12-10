from django.http import HttpResponse
from .models import Commission, ArchivedCommission


# Create your views here.
def index(request):
    active_commission_list = Commission.objects.order_by('creation_date')
    output = ', '.join([c.commission_title for c in active_commission_list])
    return HttpResponse(output)


def detail(request, commission_id):
    return HttpResponse("Commission %s." % commission_id)


def archived_detail(request, archivedCommission_id):
    return HttpResponse("Archived Commission %s." % archivedCommission_id)
