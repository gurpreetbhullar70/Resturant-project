
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import registerPage,loginPage,logoutUser,reserve_table,create_order,update_order,delete_order,customer_table


# Create your tests here
class TestReservationUrls(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url = reverse('reservation:register')
        self.assertEquals(resolve(url).func, registerPage)
        
        
    def test_loginPage_url_is_resolved(self):
        url = reverse('reservation:login')
        self.assertEquals(resolve(url).func, loginPage)
        
        
    def test_logoutUser_url_is_resolved(self):
        url = reverse('reservation:logout')
        self.assertEquals(resolve(url).func, logoutUser)
        
        
    def test_reserve_table_url_is_resolved(self):
        url = reverse('reservation:reserve_table')
        self.assertEquals(resolve(url).func, reserve_table)
        
        
    def test_create_order_url_is_resolved(self):
        url = reverse('reservation:create_order')
        self.assertEquals(resolve(url).func, create_order)
        
        
    def test_update_order_url_is_resolved(self):
        url = reverse('reservation:update_order', args=['some-slug'])
        self.assertEquals(resolve(url).func, update_order)
        
        
    def test_delete_order_url_is_resolved(self):
        url = reverse('reservation:delete_order', args=['some-slug'])
        self.assertEquals(resolve(url).func, delete_order)
        
        
    def test_customer_table_url_is_resolved(self):
        url = reverse('reservation:customer_table', args=['some-slug'])
        self.assertEquals(resolve(url).func, customer_table)   


