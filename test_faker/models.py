from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Person(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})

