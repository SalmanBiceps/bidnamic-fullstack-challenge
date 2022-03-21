from django.test import TestCase
from bidding.forms import BiddingForm

class TestForms(TestCase):
    def test_bidding_form_valid_data(self):
        form = BiddingForm(data={
            "title":"Title1", "first_name":"Firstname", "surname":"Lastname", "dob":"1990-12-30", "company_name":"Company", "address_1":"Address 1",
            "address_2":"Address 2", "city":"City", "state":"State", "postcode":"123123", "telephone":"12345678", "bidding":"H", "google_ads_account_id":"123"})
        self.assertTrue(form.is_valid())
    
    def test_bidding_form_no_data(self):
        form = BiddingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),13)
