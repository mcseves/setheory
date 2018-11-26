# Defining our proposition model

from django.conf import settings
from django.db import models
from django.urls import reverse

class AreaOfInterest(models.Model):
    area_name = models.TextField(max_length=40, help_text='Enter area of study')

    def __str__(self):
        return self.area_name

    @property
    def get_absolute_url(self):
        return reverse('area-of-interest', args=[str(self.id)])


class Value(models.Model):
    value_name = models.TextField()

    def __str__(self):
        return self.value_name

class Construct(models.Model):
    construct_name = models.TextField()
    construct_area = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE)
    construct_values = models.ManyToManyField(Value)

    def __str__(self):
        return self.construct_name


class Cause(models.Model):
    cause_name = models.ForeignKey(Construct, on_delete=models.CASCADE, related_name="causeconstruct",default='')
    reference_cause_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="referencevalue",default='')
    observed_cause_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="observedvalue",default='')

    def __str__(self):
        return self.cause_name.construct_name


class Effect(models.Model):
    effect_name = models.ForeignKey(Construct, on_delete=models.CASCADE)
    observed_effect_value = models.ForeignKey(Value, on_delete=models.CASCADE)

    def __str__(self):
        return self.effect_name.construct_name


class Proposition(models.Model):
    proposition_area = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE)
    proposition_cause = models.ManyToManyField(Cause)
    proposition_effect = models.ManyToManyField(Effect)


class EvidenceEffect(models.Model):
    evidence_name = models.TextField()
    evidence_scope = models.TextField()
    evidence_proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)

    # TODO checar nome dos tipos possiveis de evidencia
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
        return self.evidence_name