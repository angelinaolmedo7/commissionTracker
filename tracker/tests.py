import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Commission


def create_comm(comm_title, days, comm_name, comm_plat, comm_desc, comp_rating):
    """
    Create a commission with the given info.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Commission.objects.create(commission_title=comm_title,
                                     commissioner_name=comm_name,
                                     commissioner_platform=comm_plat,
                                     commission_description=comm_desc,
                                     complexity_rating=comp_rating,
                                     creation_date=time)


class CommissionIndexViewTests(TestCase):
    def test_no_commissions(self):
        """
        If no commissions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('tracker:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No active commissions.")
        self.assertQuerysetEqual(response.context['active_commission_list'], [])

    def test_past_commission(self):
        """
        Commissions are displayed on the index page.
        """
        create_comm(commission_title='title', days=-30,
                    comm_name='name', comm_plat='plat', comm_desc='desc',
                    comp_rating=5)
        response = self.client.get(reverse('tracker:index'))
        self.assertQuerysetEqual(
            response.context['active_commission_list'],
            ['<Commission: title>']
        )
    
