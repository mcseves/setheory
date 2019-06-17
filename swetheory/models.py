# Defining our proposition model

from django.db import models
from django.urls import reverse


class AreaOfInterest(models.Model):
    name = models.CharField(max_length=60, help_text='Enter area of study')

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return reverse('area-of-interest', args=[str(self.id)])


class Value(models.Model):
    name = models.CharField(max_length=60, help_text='Enter value')

    def __str__(self):
        return self.name


class Construct(models.Model):
    name = models.TextField()
    area = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE)
    # values = models.ManyToManyField(Value)

    def __str__(self):
        return self.name


class Cause(models.Model):
    name = models.ForeignKey(Construct, on_delete=models.CASCADE, related_name="cause_construct", default='')
    reference_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="reference_value", default='')
    observed_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="observed_value", default='')

    def __str__(self):
        return self.name.name


class Effect(models.Model):
    name = models.ForeignKey(Construct, on_delete=models.CASCADE, related_name="effect_construct")
    observed_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="observed_effect_value")

    def __str__(self):
        return self.name.name


class Proposition(models.Model):
    area = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE, related_name="proposition")
    cause = models.ManyToManyField(Cause)
    effect = models.ManyToManyField(Effect)


class EvidenceEffect(models.Model):
    name = models.TextField()
    scope = models.TextField()
    proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)

    TYPES_EVIDENCE = (
        ('p', 'Philosophical'),
        ('e', 'Empyrical')
    )

    evidence_type = models.CharField(
        max_length=1,
        choices=TYPES_EVIDENCE,
        blank=True,
        default='p',
        help_text=''
    )

    doi_number = models.IntegerField()

    def __str__(self):
        return self.name
