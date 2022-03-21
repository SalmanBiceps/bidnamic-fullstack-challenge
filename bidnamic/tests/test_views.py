from django.test import TestCase, Client
from django.urls import reverse
from bidding.models import Bidding
from django.contrib.auth.models import User

from bidding.forms import BiddingForm

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.bidding = Bidding.objects.create(title = "Title",first_name = "Firstname",surname = "Lastname",dob = "1990-12-30",company_name = "Company",address_1 = "Address 1",address_2 = "Address 2",city = "City",state = "State",postcode = "123123",telephone = "12345678",bidding = "H",google_ads_account_id = "123",user = self.user)

        self.list_url = reverse('biddings')
        self.detail_url = reverse('bidding_view', args=[self.bidding.id])
        self.create_url = reverse('biddings_create')

    def test_biddings_view_not_logged_in(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response)

    def test_biddings_view_logged_in(self):
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.list_url)
        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"bidding/index.html")

    def test_bidding_view_not_logged_in(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response)

    def test_bidding_view_logged_in(self):
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.detail_url)

        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bidding/bidding_view.html')

    def test_bidding_create_view(self):
        login = self.client.login(username='testuser', password='12345')
        
        form = BiddingForm(data={
            "title": "Title1", "first_name": "Firstname", "surname": "Lastname", "dob": "1990-12-30", "company_name": "Company", "address_1": "Address 1",
            "address_2": "Address 2", "city": "City", "state": "State", "postcode": "123123", "telephone": "12345678", "bidding": "H", "google_ads_account_id": "123"})
        
        response = self.client.post(self.create_url, {'form': form})
        
        self.assertTrue(login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bidding/bidding_create.html')
