from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bidding .views import biddings_view, bidding_create_view, bidding_edit_view
class TestUrls(SimpleTestCase):
    def test_biddings_url_is_resolved(self):
        url = reverse('biddings')
        self.assertEqual(resolve(url).func,biddings_view )
        
    def test_create_url_is_resolved(self):
        url = reverse('biddings_create')
        self.assertEqual(resolve(url).func, bidding_create_view)
   

   
