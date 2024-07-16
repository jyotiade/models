from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_city=models.TextField(max_length=50)
    stu_age=models.IntegerField(null=True)
    stu_password=models.CharField(max_length=10,null=True)
    stu_enroll=models.IntegerField()

    def __str__(self):
        return self.stu_name+' '+self.stu_email  #to display name,email ,age password ,etc on the admin panel
    
    class Meta:
         #=====change table name in database=============
        db_table='Student'             

        #======change table name in admin panel==============
        verbose_name_plural='Student'  # in this it remove s from table name
        #verbose_name='Student'   #by default django give model name with s.
        
        #used to order the name in ascending order according to alphabets
        #capital letter always come first then small according to ascii code
        ordering=['stu_name']
        
         #used to order the name in desending order according to alphabets
        #ordering=['-stu_name']
