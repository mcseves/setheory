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
    name = models.CharField(max_length=200, help_text='Enter construct name')
    area = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE, related_name="construct")
    # values = models.ManyToManyField(Value)

    def __str__(self):
        return self.name


class Cause(models.Model):
    cause = models.ForeignKey(Construct, on_delete=models.CASCADE, related_name="cause")
    reference_value_c = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="cause_ref")
    observed_value_c = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="cause_obs")

    def __str__(self):
        return self.cause.name

    def get_area(self):
        return self.cause.area.name


class Effect(models.Model):
    effect = models.ForeignKey(Construct, on_delete=models.CASCADE, related_name="effect")
    observed_value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name="effect_obs")

    def __str__(self):
        return self.effect.name

    def get_area(self):
        return self.effect.area.name


class EvidenceEffect(models.Model):
    TYPES_EVIDENCE = (
        ('p', 'Philosophical'),
        ('e', 'Empyrical')
    )

    name = models.TextField()
    scope = models.TextField()
    doi_number = models.IntegerField()

    evidence_type = models.CharField(
        max_length=1,
        choices=TYPES_EVIDENCE,
        blank=True,
        default='p',
        help_text=''
    )

    def __str__(self):
        return self.name


class Proposition(models.Model):
    area = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE, related_name="proposition")
    cause = models.ManyToManyField(Cause)
    effect = models.ManyToManyField(Effect)
    evidence = models.ForeignKey(EvidenceEffect, on_delete=models.CASCADE)

    def get_cause_values(self):
        ret = ' '
        for cse in self.cause.all():
            if cse.reference_value_c:
                ret = ret + cse.reference_value_c.name + " "
            if cse.observed_value_c:
                ret = ret + cse.observed_value_c.name + " "
            ret = ret + cse.cause.name + ','

        return ret[:-1]

    def get_effect_values(self):
        ret = ' '
        for eft in self.effect.all():
            if eft.observed_value:
                ret = ret + eft.observed_value.name + " "
            ret = ret + eft.effect.name + ','
        return ret[:-1]

    def get_phrase(self):
        causes = self.get_cause_values()
        effects = self.get_effect_values()

        return "Using" + causes + "results in" + effects

