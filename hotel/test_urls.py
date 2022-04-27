
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hotel.views import meal_list, meal_detail

class TestMenusUrls(SimpleTestCase):
    def test_meal_list_url_is_resolved(self):
        url = reverse('hotel:meal_list')
        self.assertEquals(resolve(url).func, meal_list)

    def test_meal_detail_url_is_resolved(self):
        url = reverse('hotel:meal_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, meal_detail)

    



# from django.test import TestCase
# from hotel.models import Meals, Category


# class TestMenuModels(TestCase):

#     def setUp(self):
#         self.meals = Meals(name='name', description='description',people='1',price='2',slug= True)
        
#         self.category = Category(name='Test 1234')
        
        
#     def test_create_slug_on(self):
#         self.assertEquals(self.meals.slug, True)
       

#     def test_create_meals(self):
#         self.assertEquals(self.meals.name, 'name')
#         self.assertEquals(self.meals.description, 'description')
#         self.assertEquals(self.meals.people, '1')
#         self.assertEquals(self.meals.price, '2')
#         self.assertEquals(self.meals.slug, True)

#     def test_create_category(self):
#         self.assertEquals(self.category.name, 'Test 1234')
       



#     def test_customer_save_works(self):
#         category = self.category
#         category.save()
#         meals = len(Meals.objects.all())
#         self.assertEquals(meals, 0)
        
        
#     def test_category_works(self):
#         category = len(Category.objects.all())
#         self.assertEquals(category, 0)

    