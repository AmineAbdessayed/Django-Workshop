from django.db import models
from django.core.exceptions import ValidationError
from Person.models import Person




def verifEmail(mail):
    if str(mail).endswith('@esprit.tn')==false:
        raise ValidationError("Your email is not correct!!")
    return mail
    

class Event(models.Model):
    
    Categorys=[
        ('M','Musique'),
        ('C','Cinema'),
        ('S','Sport')
    ]
    title = models.CharField(max_length=200)
    Description=models.TextField()
    image=models.ImageField(upload_to='images/')
    state=models.BooleanField(default=False)
    category=models.CharField(max_length=1,choices=Categorys)
    
    evt_date = models.DateTimeField()           

    
    email=models.EmailField(validators=[verifEmail])
    creation_date = models.DateTimeField(auto_now_add=True)  
    update_date = models.DateTimeField(auto_now=True)  
    
    #organizer
    
    organizer=models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='organized_events')
    
    
    
    participation=models.ManyToManyField(
        Person,
        through='participation_event',
        related_name='part_evt'
      )
    def __str__(self):
        return f"L'evt est: {self.title}" 
     
class participation_event(models.Model):
        person=models.ForeignKey(Person,on_delete=models.CASCADE)
        event=models.ForeignKey(Event,on_delete=models.CASCADE)
        participation_date =models.DateField(auto_now=True)
        class Meta:
         unique_together=('person','event')
        def __str__(self):
         return f"{self.person.email} - {self.event.title}"