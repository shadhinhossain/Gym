from django.contrib import admin
from user.models import Contact,Enrollment,Trainer,MembershipPlan



# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(MembershipPlan)