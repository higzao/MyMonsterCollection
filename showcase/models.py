from django.db import models

# Create your models here.
class Can(models.Model):
    name = models.CharField(max_length=100)
    line = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    size = models.IntegerField()  # Armazena o valor numérico do tamanho em ml
    sku = models.CharField(max_length=20, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)

    # Colors
    main_color = models.CharField(max_length=20)
    detail_color = models.CharField(max_length=20)
    color_lid = models.CharField(max_length=20)
    color_top = models.CharField(max_length=20)

    logo_lid = models.BooleanField(default=False)
    sugar_warning = models.BooleanField(default=False)
    condition = models.IntegerField()  # Assume um valor de 0 a 100 para condição
    top_intact = models.BooleanField(default=True)
    
    # Promotion
    is_promotion = models.BooleanField(default=False)
    promotion_name = models.CharField(max_length=100, blank=True, null=True)
    promotion_details = models.TextField(blank=True, null=True)

    bottle = models.BooleanField(default=False)
    tasted = models.BooleanField(default=False)

    # Notes
    top_notes = models.TextField(blank=True, null=True)
    bottom_notes = models.TextField(blank=True, null=True)

    # Images
    img_front = models.CharField(max_length=100)
    img_back = models.CharField(max_length=100)
    img_back_2 = models.CharField(max_length=100)
    img_top = models.CharField(max_length=100)

    # Gift information
    is_gift = models.BooleanField(default=False)
    friend_name = models.CharField(max_length=100, blank=True, null=True)
    gift_date = models.DateField(blank=True, null=True)

def __str__(self):
    return self.name