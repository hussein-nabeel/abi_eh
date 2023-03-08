from django.db import models

class Prodect (models .Model):
    category =models.CharField( max_length=200)
    title =models.CharField(max_length=255)
  
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=11,decimal_places=1)
        # price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to='Images/' )

    class Meta:
     ordering = ('-created_at',)

   
    def __str__(self) -> str:
       return self.title