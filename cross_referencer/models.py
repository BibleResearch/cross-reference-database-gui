from django.db import models


class BiblePassage(models.Model):
    """
    Description: A passage from the Bible
    """
    reference = models.CharField(max_length=30)
    first_seen = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.reference)


class CrossReference(models.Model):
    """
    Description: A cross reference between two passages in scripture.
    """
    first_seen = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # TODO: eventually, I would like to change this to a standard set of options
    classification = models.CharField(max_length=100)
    explanation = models.TextField(blank=True, null=True)
    sources = models.TextField()
    start = models.ForeignKey('BiblePassage', related_name='start')
    destination = models.ForeignKey('BiblePassage', related_name='destination')

    def sources_as_list(self):
        return self.sources.split('|')

    def __str__(self):
        return '{} & {}'.format(self.start, self.destination)
