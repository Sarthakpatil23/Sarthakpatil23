from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PrintingShop(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, related_name='printing_shops', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UploadedFile(models.Model):
    COLOR_CHOICES = [
        ('color', 'Color'),
        ('bw', 'Black and White'),
    ]

    PRINT_CHOICES = [
        ('single', 'Single Side'),
        ('double', 'Double Side'),
    ]

    TIME_LIMIT_CHOICES = [
        ('5min', '5 Minutes'),
        ('10min', '10 Minutes'),
        ('15min', '15 Minutes'),
    ]

    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    color_option = models.CharField(max_length=5, choices=COLOR_CHOICES, default='bw')
    print_option = models.CharField(max_length=6, choices=PRINT_CHOICES, default='single')
    additional_instructions = models.TextField(blank=True, null=True)
    time_limit = models.CharField(max_length=5, choices=TIME_LIMIT_CHOICES, default='5min')
    uploaded_at = models.DateTimeField(auto_now_add=True)