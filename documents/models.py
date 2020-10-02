from django.db import models

# Create module for documents


class Document(models.Model):
    address = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=2000)
    date = models.DateField()
    # signature = models.ImageField()
    signed = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # notes = models.CharField(max_length=400)

    def __str__(self):
        return self.address, self.title
        # return the address and the title in the admin panel Documents screen
