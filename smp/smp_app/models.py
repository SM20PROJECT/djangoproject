from djongo import models


# Create your models here.
class Login(models.Model):
    def __str__(self):
        return self.nickName

    GENDER = (
        ('E', 'Erkek'),
        ('K', 'Kadın'),
        ('N', 'Belirmek istemiyorum.')
    )
    nickName = models.CharField(max_length=15)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    eMail = models.EmailField(max_length=254)
    gender = models.CharField(max_length=20, choices=GENDER)
