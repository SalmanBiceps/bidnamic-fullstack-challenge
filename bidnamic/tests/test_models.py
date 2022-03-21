from django.test import TestCase
from django.contrib.auth.models import User
from bidding.models import Bidding

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

        self.bidding = Bidding.objects.create(title="Title", first_name="Firstname", surname="Lastname", dob="1990-12-30", company_name="Company", address_1="Address 1",
                                              address_2="Address 2", city="City", state="State", postcode="123123", telephone="12345678", bidding="HIGH", google_ads_account_id="123", user=self.user)

    def test_bidding_belongs_to_user(self):
        self.assertEquals(self.bidding.user, self.user)