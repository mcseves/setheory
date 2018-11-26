from django.contrib import admin
from .models import AreaOfInterest, Proposition, Cause, Effect, EvidenceEffect, Value, Construct

admin.site.register(AreaOfInterest)
admin.site.register(Construct)
admin.site.register(Value)
admin.site.register(Cause)
admin.site.register(Effect)
admin.site.register(Proposition)
admin.site.register(EvidenceEffect)
