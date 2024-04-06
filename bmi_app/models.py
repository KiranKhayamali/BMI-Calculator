from django.db import models

# Create your models here.
class History(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.user.username}'s BMI History at {self.created_at}"
    # class Meta:
    #     ordering = ['-created_at']