from django.test import TestCase, Client
from django.urls import reverse


class TestMenusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.meal_list_url = reverse('hotel:meal_list')
        
       
        

    def test_meal_list_GET(self):
        response = self.client.get(self.meal_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Meals/list.html')
