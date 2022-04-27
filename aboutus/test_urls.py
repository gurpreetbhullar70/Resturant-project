
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from aboutus.views import aboutus_list



class TestAboutusUrls(SimpleTestCase):
    def test_aboutus_list_url_is_resolved(self):
        url = reverse('aboutus:aboutus_list')
        self.assertEquals(resolve(url).func, aboutus_list)

   
   
   


# from django.test import TestCase
# from aboutus.models import AboutUs, Why_Choose_Us, Chef


# class TestAboutusModels(TestCase):

#     def setUp(self):
#         self.aboutus = AboutUs(title='title', content='content')
#         self.why_choose_us = Why_Choose_Us(
#             title='title 1', content='content 1')
#         self.chef = Chef(title='title 3', name='name 1')
        
        
        

#     def test_create_aboutus(self):
#         self.assertEquals(self.aboutus.title, 'title')
#         self.assertEquals(self.aboutus.content, 'content')
        
#     def test_create_why_choose_us(self):
#         self.assertEquals(self.why_choose_us.title, 'title 1')
#         self.assertEquals(self.why_choose_us.content, 'content 1')
       
#     def test_create_chef(self):
#         self.assertEquals(self.chef.title, 'title 3')
#         self.assertEquals(self.chef.name, 'name 1')



#     def test_aboutus_works(self):

#         aboutus = AboutUs.objects.last()

#         self.assertEquals(aboutus, None)



#     def test_why_choose_us_works(self):

#         why_choose_us = len(Why_Choose_Us.objects.all())

#         self.assertEquals(why_choose_us, 0)
        
        
#     def test_Chef_works(self):

#         chef = len(Chef.objects.all())

#         self.assertEquals(chef, 0)