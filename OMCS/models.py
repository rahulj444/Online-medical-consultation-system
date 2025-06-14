from django.db import models
from email import message
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password 


#Only admin can add hospitals 
class hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{10}$',
    #     message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed."
    # )
    phone_number = models.CharField(max_length=15)
    pincode_regex = RegexValidator(regex=r'^[0-9]{6}$', message="Enter a valid Indian pincode.")
    pincode = models.CharField(max_length=6, validators=[pincode_regex])
    description=models.CharField(max_length=100)
    # isdelete = models.BooleanField(default=False)




class doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="")

    # password = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=128)  # we will store the hashed password here
    def set_password(self, password):
        """
        Set the password for this doctor, hashing it first.
        """
        self.password = make_password(password)
    def check_password(self, password):
        """
        Check the given password against the stored hash for this doctor.
        """
        return check_password(password, self.password)
        
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices,default="M")
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{10}$',
    #     message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed."
    # )
    SPECIALIZATION_CHOICES = (
        (1, 'Cardiologist'),
        (2, 'Endocrinologist'),
        (3, 'Neurologist'),
        (4, 'Psychiatrists'),
        (5, 'ENT specialist'),
        (6, 'Gynaecologist'),
        (7, 'Orthopaedic surgeon'),
        (8, 'Pulmonologist'),
    )
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=100,default="")
    specialization = models.IntegerField(choices=SPECIALIZATION_CHOICES)
    city = models.CharField(max_length=100,default="")
   # experience = models.CharField(max_length=100)
    pincode_regex = RegexValidator(regex=r'^[0-9]{6}$', message="Enter a valid Indian pincode.")
    pincode = models.CharField(max_length=6, validators=[pincode_regex],default=111111)
    age = models.PositiveIntegerField(default=0)
    #certificate = models.FileField(upload_to='doctor_certificates', blank=True)
    experience=models.CharField(max_length=100,default="")
    isdelete = models.BooleanField(default=False)
    hospitalid = models.IntegerField(default=0)
    #slot_list = models.ArrayField(models.BooleanField(), null=False, blank=False, default=lambda: [False]*6)


class patient(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    age = models.PositiveIntegerField(default=0) 
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices,default="M")
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{10}$',
    #     message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed."
    # )
    phone_number = models.BigIntegerField()
    email = models.EmailField(default="")
    # password = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=128)  # we will store the hashed password here
    def set_password(self, password):
        """
        Set the password for this doctor, hashing it first.
        """
        self.password = make_password(password)
    def check_password(self, password):
        """
        Check the given password against the stored hash for this doctor.
        """
        return check_password(password, self.password)
    
    address = models.CharField(max_length=100,default="")
    pincode_regex = RegexValidator(regex=r'[0-9]{6}$', message="Enter a valid Indian pincode.")
    pincode = models.CharField(max_length=6, validators=[pincode_regex])

    description=models.CharField(max_length=100,default="")
    isdelete = models.BooleanField(default=False)


class appointments(models.Model):

    hospitalid = models.ForeignKey(hospital, on_delete=models.CASCADE)


    doctorid = models.PositiveIntegerField()
    date=models.DateField()
    #lists of booking IDs
    morning=[]
    afternoon=[]
    evening=[]
    # morningtoken = models.PositiveIntegerField(default=1)
    # afternoontoken = models.PositiveIntegerField(default=1)
    # eveninggtoken = models.PositiveIntegerField(default=1)

    
class bookedappointments(models.Model):
    bookingid = models.AutoField(primary_key=True)
    doctorid = models.PositiveIntegerField()
    patientid = models.PositiveIntegerField()
    date=models.DateField()
    time=models.TimeField(default='00:00')
    slot=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default='no action taken')
    description=models.CharField(max_length=100,default="")
    appointment_preference=models.CharField(max_length=100,default="")



class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="")
    password = models.CharField(max_length=128)  # we will store the hashed password here
    def set_password(self, password):
        """
        Set the password for this doctor, hashing it first.
        """
        self.password = make_password(password)
    def check_password(self, password):
        """
        Check the given password against the stored hash for this doctor.
        """
        return check_password(password, self.password)

class pending_doctors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="")

    # password = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=128)  # we will store the hashed password here
    def set_password(self, password):
        """
        Set the password for this doctor, hashing it first.
        """
        self.password = make_password(password)
    def check_password(self, password):
        """
        Check the given password against the stored hash for this doctor.
        """
        return check_password(password, self.password)
        
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices,default="M")
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{10}$',
    #     message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed."
    # )
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=100,default="")
    specialization = models.IntegerField(default=0)
   # experience = models.CharField(max_length=100)
    pincode_regex = RegexValidator(regex=r'^[0-9]{6}$', message="Enter a valid Indian pincode.")
    pincode = models.CharField(max_length=6, validators=[pincode_regex],default=111111)
    age = models.PositiveIntegerField(default=0)
    #certificate = models.FileField(upload_to='doctor_certificates', blank=True)
    experience=models.CharField(max_length=100,default="")
    isdelete = models.BooleanField(default=False)
    hospitalid = models.IntegerField(default=0)
    #slot_list = models.ArrayField(models.BooleanField(), null=False, blank=False, default=lambda: [False]*6)


# Create your models here.  from django.http import JsonResponse

from django.http import JsonResponse

def search_hospitals(request):
    search_term = request.GET.get('q', '')
    specialization = request.GET.get('specialization', '')
    
    hospitals = hospital.objects.all()
    
    if search_term:
        if search_term.isdigit() and len(search_term) == 6:
            hospitals = hospitals.filter(pincode=search_term)
        else:
            hospitals = hospitals.filter(name__icontains=search_term)
    
    if specialization:
        hospitals = hospitals.filter(specialization__id=specialization)
    
    results = [{
        'id': h.id,
        'name': h.name,
        'pincode': h.pincode,
        'address': h.address
    } for h in hospitals[:10]]  # Limit to 10 results
    
    return JsonResponse(results, safe=False)