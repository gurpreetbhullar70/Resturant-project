# from django.test import TestCase,Client
# from django.urls import reverse
# from reservation.models import Customer, Table, Reservation
# from django.contrib.auth.models import User

# class TestReservationsViews(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='project.test@test.com',
#             email='project.test@test.com', password='12345')
#         self.client.login(
#             username='project.test@test.com',
#             email='project.test@test.com', password='12345')
#         self.reservations_url = reverse('reservation:reserve_table')
#         self.register_url = reverse('reservation:register')
#         self.login_url = reverse('reservation:login')
#         self.view_reservations_url = reverse('reservation:customer_table',args=[1])
#         self.create_customer_details_url = reverse('reservation:create_order')
#         self.update_reservation1_url = reverse('reservation:update_order', args=[2])
#         self.delete_reservation1_url = reverse('reservation:delete_order',args=[2])

#         self.table = Table.objects.create(
#             table_name='Table 5',
#             max_no_people=4
#         )

#         self.customer = Customer.objects.create(
#             name='Project Test',
#             email='project.test@test.com',
#             phone='+447980987654',
#             owner = '1'
#         )

#         self.reservation1 = Reservation.objects.create(
#             user=self.user,
#             customer=self.customer,
#             table=self.table,
        
#             persons=1,
#             date='2022-05-20',
#             time='12:00',
#             status='pending'
#         )

#         self.reservation2 = Reservation.objects.create(
#             user=self.user,
#             customer=self.customer,
#             table=self.table,
            
#             persons=1,
#             date='2022-05-20',
#             time='12:00',
#             status='pending'
#         )


#     def test_reservation_GET(self):
#         response = self.client.get(self.reservations_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/reservation.html')

#     def test_view_reservation_GET(self):
#         response = self.client.get(self.view_reservations_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/view_reservation.html')
        
#     def test_create_reservation_GET(self):
#         response = self.client.get(self.create_customer_details_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/create_reservation.html')
        
#     def test_update_reservation_GET(self):
#         response = self.client.get(self.update_reservation1_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/update_reservation.html')     
        
#     def test_delete_reservation_GET(self):
#         response = self.client.get(self.delete_reservation1_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/delete_reservation.html')



#     def test_register_form_GET(self):
#         response = self.client.get(self.register_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/register.html')
        
        
#     def test_login_form_GET(self):
#         response = self.client.get(self.login_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Reservation/login.html')



        
        
        
        
        
        
        
        
#     def test_reservation_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.reservations_url)

#         self.assertEquals(response.status_code, 302)    
        

#     def test_view_reservation_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.view_reservations_url)

#         self.assertEquals(response.status_code, 302)


#     def test_delete_reservation_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.delete_reservation1_url)

#         self.assertEquals(response.status_code, 302)


#     def test_edit_reservation_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.create_customer_details_url)

#         self.assertEquals(response.status_code, 302)


#     def test_update_reservation_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.update_reservation1_url)

#         self.assertEquals(response.status_code, 302)
    
    
    
    
#     def test_register_form_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.register_url)

#         self.assertEquals(response.status_code, 200)
        
        
#     def test_login_form_GET_unathorised_user_redirected(self):
#         self.client.logout()
#         response = self.client.get(self.login_url)

#         self.assertEquals(response.status_code, 200)
    
    
    
    
    
#     def test_reservation_POST_adds_new_customer_and_reservation(self):
#         table = self.table

#         customer = Customer.objects.create(
#             name='Project Test123',
#             email='project.test123@test.com',
#             phone='+447980987654',
#             owner = '2'
#         )

#         reservation = Reservation.objects.create(
#             user=self.user,
#             customer=customer,
#             table=table,
        
#             persons=1,
#             date='2022-03-29',
#             time='12:00',
#             status='pending'
#         )

#         response = self.client.post(self.reservations_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(len(Reservation.objects.all()), 3)
#         self.assertEquals(len(Customer.objects.all()), 2)


#     def test_reservation_POST_does_not_add_customer_that_exists(self):
#         table = self.table
#         customer = self.customer
#         reservation = Reservation.objects.create(
#            user=self.user,
#             customer=self.customer,
#             table=self.table,
        
#             persons=1,
#             date='2022-05-20',
#             time='12:00',
#             status='pending'
#         )

#         response = self.client.post(self.reservations_url)

#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(len(Reservation.objects.all()), 3)
#         self.assertEquals(len(Customer.objects.all()), 1)
        
        
        
        
        
#     def test_edit_reservation_POST_updates_model(self):
#         reservation = self.reservation1

#         reservation.date = '2022-04-01'

#         response = self.client.post(self.update_reservation1_url)

#         self.assertEquals(self.reservation1.date, '2022-04-01')

#     def test_delete_reservation_POST_updates_model(self):
#         reservation = self.reservation2
#         response = self.client.post(self.delete_reservation1_url)

#         self.assertEquals(len(Reservation.objects.all()), 1)
#         self.assertNotIn(self.reservation2, Reservation.objects.all())




# from ast import arg
# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from reservation.views import registerPage,loginPage,logoutUser,reserve_table,create_order,update_order,delete_order,customer_table


# # Create your tests here
# class TestReservationUrls(SimpleTestCase):
#     def test_register_url_is_resolved(self):
#         url = reverse('reservation:register')
#         self.assertEquals(resolve(url).func, registerPage)
        
        
#     def test_loginPage_url_is_resolved(self):
#         url = reverse('reservation:login')
#         self.assertEquals(resolve(url).func, loginPage)
        
        
#     def test_logoutUser_url_is_resolved(self):
#         url = reverse('reservation:logout')
#         self.assertEquals(resolve(url).func, logoutUser)
        
        
#     def test_reserve_table_url_is_resolved(self):
#         url = reverse('reservation:reserve_table')
#         self.assertEquals(resolve(url).func, reserve_table)
        
        
#     def test_create_order_url_is_resolved(self):
#         url = reverse('reservation:create_order')
#         self.assertEquals(resolve(url).func, create_order)
        
        
#     def test_update_order_url_is_resolved(self):
#         url = reverse('reservation:update_order', args=['some-slug'])
#         self.assertEquals(resolve(url).func, update_order)
        
        
#     def test_delete_order_url_is_resolved(self):
#         url = reverse('reservation:delete_order', args=['some-slug'])
#         self.assertEquals(resolve(url).func, delete_order)
        
        
#     def test_customer_table_url_is_resolved(self):
#         url = reverse('reservation:customer_table', args=['some-slug'])
#         self.assertEquals(resolve(url).func, customer_table)   




from django.test import TestCase
from reservation.models import Reservation, Table, Customer


class TestReservationsModels(TestCase):

    def setUp(self):
        self.table = Table(table_name='Table 1', max_no_people=4)
        self.customer = Customer(
            name='Test 123', email='test123@gmail.com',phone='12345',owner='1')
        self.reservation = Reservation(
            table=self.table,
            customer=self.customer,
            persons=4, date='2022-01-23',
            time='12:00', status='pending')

    def test_create_table(self):
        self.assertEquals(self.table.table_name, 'Table 1')
        self.assertEquals(self.table.max_no_people, 4)

    def test_create_customer(self):
        self.assertEquals(self.customer.name, 'Test 123')
        self.assertEquals(self.customer.email, 'test123@gmail.com')

    def test_create_reservation(self):
        self.assertEquals(self.reservation.table, self.table)
        self.assertEquals(self.reservation.customer, self.customer)
        self.assertEquals(self.reservation.persons, 4)
        self.assertEquals(self.reservation.date, '2022-01-23')
        self.assertEquals(self.reservation.time, '12:00')
        self.assertEquals(self.reservation.status, 'pending')

    def test_customer_on_delete_cascade_works(self):
        customer = self.customer
        customer.save()

        reservations = len(Reservation.objects.all())

        self.assertEquals(reservations, 0)

    def test_table_on_delete_cascade_works(self):
        table = self.table
        table.save()

        reservations = len(Reservation.objects.all())

        self.assertEquals(reservations, 0)