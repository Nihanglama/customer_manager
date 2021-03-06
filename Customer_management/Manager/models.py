from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
          user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
          name=models.CharField(max_length=200,null=True)
          phone=models.CharField(max_length=200,null=True)
          email=models.EmailField(null=True)
          photo=models.ImageField(default='alternative.jpg',null=True,blank=True) 
          date_created=models.DateTimeField(auto_now_add=True)

          def __str__(self):
              return self.name
              
class Tag(models.Model):
          name=models.CharField(max_length=200,null=True)
          def __str__(self):
              return self.name
       
       
class Product(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
        Cate=(
                    ('Cloths','cloths'),
                    ('Shoes','shoes'),
                    ('Games','games'),
                    ('IOTs','iots'),
                    ('Books','books'),
              )
        name=models.CharField(max_length=200,null=True)             
        price=models.FloatField(null=True)
        category=models.CharField(max_length=200,null=True,choices=Cate)
        description=models.TextField(null=True,max_length=300)
        added_date=models.DateTimeField(auto_now_add=True)
        tags=models.ManyToManyField(Tag)
        photo=models.ImageField(default='alternative.jpg',null=True,blank=True)

        def __str__(self):
            return self.name



class Order(models.Model):
          Status=(
            ('Pending','pending'),
            ('Delivered','delivered'),
            )
          customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
          name=models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
          phone=models.CharField(max_length=10,null=True)
          address=models.CharField(max_length=200,null=True)
          status=models.CharField(max_length=200,default='pending',choices=Status)
          order_date=models.DateTimeField(auto_now_add=True,null=True)
          quentity=models.IntegerField(null=True,default=1)


         

             










