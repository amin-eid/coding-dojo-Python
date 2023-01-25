from django.db import models

class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255)
class ninja(models.Model):
    dojo = models.ForeignKey(dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"<dojo object: ({self.id}) {self.name} {self.city} {self.state}>"
    def __str__(self):
        return f"<ninja object: ({self.id}) {self.dojo} {self.first_name} {self.last_name} >"