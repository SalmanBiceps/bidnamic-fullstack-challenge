from django.db import models



class Bidding(models.Model):
    
    BIDDING_OPTIONS = [
        ('H', 'HIGH'),
        ('M', 'MEDIUM'),
        ('L', 'LOW'),
    ]

    title = models.CharField(max_length=50,unique=True  )
    first_name= models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    company_name=models.CharField(max_length=50)
    address_1=models.CharField(max_length=50)
    address_2=models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)  
    postcode =models.CharField(max_length=20)
    telephone = models.CharField(max_length=50)
    bidding = models.CharField(max_length=10, choices=BIDDING_OPTIONS)
    google_ads_account_id = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,)

    class Meta:
        """Meta definition for Biddung."""

        verbose_name = "Bidding"
        verbose_name_plural = "Biddings"

    def __str__(self):
        """Unicode representation of Bidding."""
        return "%s" % self.title



    
