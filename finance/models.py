from django.db import models
from django.db.models.deletion import DO_NOTHING
from academics.models import Class, StudentClass, AcademicSession, AcademicTerm
from admissions.models import Student
from django import utils
from django.urls import reverse
# Create your models here.


class FeeStructure(models.Model):
    class_name = models.ForeignKey(Class, on_delete=DO_NOTHING)
    date = models.DateField()
    file = models.FileField(upload_to=f'fee_structure/{class_name.name}/%Y')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.class_name.name} - {self.date}"
    

class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    class_for = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    balance_from_previous_term = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("closed", "Closed")],
        default="active",
    )

    class Meta:
        ordering = ["student", "term"]

    def __str__(self):
        return f"{self.student}"

    def balance(self):
        payable = self.total_amount_payable()
        paid = self.total_amount_paid()
        return payable - paid

    def amount_payable(self):
        items = InvoiceItem.objects.filter(invoice=self)
        total = 0
        for item in items:
            total += item.amount
        return total

    def total_amount_payable(self):
        return self.balance_from_previous_term + self.amount_payable()

    def total_amount_paid(self):
        receipts = Receipt.objects.filter(invoice=self)
        amount = 0
        for receipt in receipts:
            amount += receipt.amount_paid
        return amount

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"pk": self.pk})


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()


class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    date_paid = models.DateField(default=utils.timezone.now)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Receipt on {self.date_paid}"
