# # Defining our proposition model
#
# from django.conf import settings
# from django.db import models
#
# class AreaOfInterest(models.Model):
#     areaTitle = models.TextField(unique=True)
#
# class Construct(models.Model):
#     name = models.TextField()
#     relatedArea = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE())
#
# class Value(models.Model):
#     VALUE_TYPES = (
#         ('G','Good'),
#         ('B', 'Bad')
#     )
#     valueType = models.CharField(max_length=1, choices=VALUE_TYPES)
#
#
# class Cause(models.Model):
#     causeName = models.ForeignKey(Construct, on_delete=models.CASCADE())
#     causeReferenceValue = models.ForeignKey(Value, on_delete=models.CASCADE())
#     causeObservedValue = models.ForeignKey(Value, on_delete=models.CASCADE())
#
# class Effect(models.Model):
#     effectName = models.ForeignKey(Construct, on_delete=models.CASCADE())
#     effectObservedValue = models.ForeignKey(Value, on_delete=models.CASCADE())
#
# class Evidence(models.Model):
#     evidenceName = models.TextField()
#     evidenceScope = models.TextField()
#     # evidenceType = Evidence
#     doiNumber = models.IntegerField()
#
# class Proposition(models.Model):
#     propositionArea = models.ForeignKey(AreaOfInterest, on_delete=models.CASCADE())
#     propositionTitle = models.TextField()
#     propositionCause = models.ManyToManyField()
#     propositionEffect = models.ManyToManyField()
#     propositionEvidence = models.ForeignKey(Evidence, on_delete=models.CASCADE())
