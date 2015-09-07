from django.contrib import admin
from irs.models import F8872, Contribution, Expenditure, Committee


class F8872Admin(admin.ModelAdmin):
    pass


class ContributionAdmin(admin.ModelAdmin):
    pass


class ExpenditureAdmin(admin.ModelAdmin):
    pass


class CommitteeAdmin(admin.ModelAdmin):
    pass

admin.site.register(F8872, F8872Admin)
admin.site.register(Contribution, ContributionAdmin)
admin.site.register(Expenditure, ExpenditureAdmin)
admin.site.register(Committee, CommitteeAdmin)
