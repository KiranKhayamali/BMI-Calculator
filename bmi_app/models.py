from django.db import models

# Create your models here.
class History(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_at']