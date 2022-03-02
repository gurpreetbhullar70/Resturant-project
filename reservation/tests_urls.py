from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import (reserve_table, create_order,
                                update_order, delete_order,customer_table)

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_reserve_table_url_is_resolved(self):
        assert 1==2
        