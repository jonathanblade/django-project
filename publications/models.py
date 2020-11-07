from django.db import models

class Publication(models.Model):

    title = models.CharField(max_length=512)
    authors = models.CharField(max_length=2048)
    year = models.PositiveIntegerField()
    journal = models.CharField(max_length=256)
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    doi = models.CharField(max_length=128, blank=True)
    url = models.URLField(blank=True)

    def get_doi_url(self):
        base_url = 'https://doi.org'
        doi_url = base_url + '/' + self.doi
        return doi_url