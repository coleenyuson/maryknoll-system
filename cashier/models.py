from __future__ import unicode_literals

from django.db import models

#SIGNALS = TRIGGERS
from django.db.models.signals import post_save
# Create your models here.
class EnrollmentBreakdown(models.Model):
    """Model definition for EnrollmentBreakdown."""
    payable_name = models.CharField(max_length=50)
    fee_amount = models.FloatField()
    year_level = models.ForeignKey(
        'enrollment.YearLevel', on_delete=models.CASCADE, null=True,blank=True)

    class Meta:
        """Meta definition for EnrollmentBreakdown."""

        verbose_name = 'EnrollmentBreakdown'
        verbose_name_plural = 'EnrollmentBreakdowns'

    def __str__(self):
        """Unicode representation of EnrollmentBreakdown."""
        return " %s costs %s " % (self.payable_name, str(self.fee_amount))


class EnrollmentTransactionsMade(models.Model):
    student = models.ForeignKey(
        'registration.Enrollment', on_delete=models.CASCADE)
    particular_name = models.CharField(max_length=50)
    #Add choices
    payment_type = models.CharField(max_length=50)
    #add Months
    month = models.CharField(max_length=50, null=True, blank=True)
    date_paid = models.DateField()
    ORnum = models.IntegerField()
    
    class Meta:
        """Meta definition for EnrollmentTransactionsMade."""

        verbose_name = 'EnrollmentTransactionsMade'
        verbose_name_plural = 'EnrollmentTransactionsMades'

    def __str__(self):
        """Unicode representation of EnrollmentTransactionsMade."""
        pass


class EnrollmentORDetails(models.Model):
    """Model definition for OR_Details."""
    ORnumber = models.ForeignKey(
        'EnrollmentTransactionsMade', on_delete=models.CASCADE)
    Particular_being_paid = models.CharField(max_length=50)
    money_given = models.FloatField()

    class Meta:
        """Meta definition for OR_Details."""

        verbose_name = 'OR_Details'
        verbose_name_plural = 'OR_Detailss'

    def __str__(self):
        """Unicode representation of OR_Details."""
        pass


class OthersTransactionsMade(models.Model):
    """Model definition for OthersTransactionsMade."""

    student = models.ForeignKey(
        'registration.Enrollment', on_delete=models.CASCADE)
    date_paid = models.DateField()
    ORnum = models.IntegerField()

    class Meta:
        """Meta definition for OthersTransactionsMade."""

        verbose_name = 'OthersTransactionsMade'
        verbose_name_plural = 'OthersTransactionsMades'

    def __str__(self):
        """Unicode representation of OthersTransactionsMade."""
        pass


class OthersORDetails(models.Model):
    """Model definition for OthersORDetails."""

    ORnumber = models.ForeignKey(
        'OthersTransactionsMade', on_delete=models.CASCADE)
    name_of_item = models.CharField(max_length=50)
    money_given = models.FloatField()

    class Meta:
        """Meta definition for OthersORDetails."""

        verbose_name = 'OthersORDetails'
        verbose_name_plural = 'OthersORDetailss'

    def __str__(self):
        """Unicode representation of OthersORDetails."""
        pass
