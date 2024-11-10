from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import (
    RangeNumericFilter,
    MultipleChoicesDropdownFilter,
    MultipleRelatedDropdownFilter,
    RangeDateFilter,
)
from .models import Member, Coach, TrainingSession, TrainingRegistration


class TrainingRegistrationInline(TabularInline):
    model = TrainingRegistration
    extra = 1


@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ("user", "date_of_birth", "join_date", "belt_color")
    search_fields = ("user__username", "user__email", "belt_color")
    list_filter = (("join_date", RangeDateFilter),)


@admin.register(Coach)
class CoachAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ("user", "experience_years", "specialization")
    search_fields = ("user__username", "user__email", "specialization")
    list_filter = (("experience_years", RangeNumericFilter),)


@admin.register(TrainingSession)
class TrainingSessionAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ("coach", "date", "time", "duration", "max_participants")
    search_fields = ("coach__user__username", "date", "time")
    list_filter = (("date", RangeDateFilter), ("coach", MultipleRelatedDropdownFilter))


@admin.register(TrainingRegistration)
class TrainingRegistrationAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ("member", "training_session", "registration_date")
    search_fields = (
        "member__user__username",
        "training_session__date",
        "training_session__time",
    )
    list_filter = (
        ("registration_date", RangeDateFilter),
        ("training_session", MultipleRelatedDropdownFilter),
    )
