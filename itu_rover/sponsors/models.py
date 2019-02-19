from django.db import models

from core.mixins import OrderableMixin
from core.models import TimeStampedModel
from members.utils import validate_one_object


class Sponsor(TimeStampedModel):
    """ Represents organizations supporting the project """
    image = models.ImageField(upload_to='images/sponsors')
    display_width = models.PositiveSmallIntegerField(
        help_text="in pixels"
    )
    name = models.CharField(
        max_length=50,
        verbose_name='name',
    )
    website = models.URLField(verbose_name='website')
    sponsorship_type = models.ForeignKey(
        "SponsorshipType",
        on_delete=models.SET_NULL,
        null=True,
        related_name='sponsors',
        verbose_name='type of sponsorship',
    )
    is_name_on_display = models.BooleanField(
        default=False,
        verbose_name='put name under the image on display?',
    )
    is_old = models.BooleanField(
        default=False,
        verbose_name='is sponsor old?',
    )

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class SponsorshipType(OrderableMixin, TimeStampedModel):
    """ Represents kinds of sponsorships """
    name = models.CharField(
        max_length=30,
        verbose_name='type name',
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class SupportPage(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "support page"
        verbose_name_plural = verbose_name

    def clean(self):
        validate_one_object(self)

    def __str__(self):
        return "Support page"
