from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Member(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    date_of_birth = models.DateField(_("Дата рождения"))
    join_date = models.DateField(_("Дата вступления"))
    belt_color = models.CharField(_("Цвет пояса"), max_length=50)

    class Meta:
        verbose_name = _("Участник")
        verbose_name_plural = _("Участники")

    def __str__(self) -> str:
        return self.user.username


class Coach(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    experience_years = models.PositiveIntegerField(_("Годы опыта"))
    specialization = models.CharField(_("Специализация"), max_length=255)

    class Meta:
        verbose_name = _("Тренер")
        verbose_name_plural = _("Тренеры")

    def __str__(self) -> str:
        return self.user.username


class TrainingSession(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name=_("Тренер"))
    date = models.DateField(_("Дата"))
    time = models.TimeField(_("Время"))
    duration = models.DurationField(_("Продолжительность"))
    max_participants = models.PositiveIntegerField(
        _("Максимальное количество участников")
    )

    class Meta:
        verbose_name = _("Тренировка")
        verbose_name_plural = _("Тренировки")

    def __str__(self) -> str:
        return f"{self.coach.user.username} - {self.date} {self.time}"


class TrainingRegistration(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, verbose_name=_("Участник")
    )
    training_session = models.ForeignKey(
        TrainingSession, on_delete=models.CASCADE, verbose_name=_("Тренировка")
    )
    registration_date = models.DateField(_("Дата регистрации"))

    class Meta:
        verbose_name = _("Регистрация на тренировку")
        verbose_name_plural = _("Регистрации на тренировки")

    def __str__(self) -> str:
        return f"{self.member.user.username} - {self.training_session.date} {self.training_session.time}"
