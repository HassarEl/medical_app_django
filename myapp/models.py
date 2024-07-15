from django.db import models

# Create your models here.
class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    num_cin = models.CharField(max_length=50)


class Rdv(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_rdv = models.DateField()
    heure_rdv = models.TimeField() 
    id_pat = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return ({self.date_rdv}, {self.heure_rdv}, {self.id_pat})

class ordonnance(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    medicament = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    id_pat = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return ({self.medicament}, {self.dose}, {self.id_pat})
    
def __str__(self):
    return(f"{self.first_name} {self.last_name} {self.phone} {self.address} {self.num_cin}")



