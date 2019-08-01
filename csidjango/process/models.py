from django.db import models
from accounts.models import User

# Create your models here.


class Types(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Steps(models.Model):
    def save(self, *args, **kwargs):
        if not self.order or self.order == 0:
            last = Steps.objects.filter(types=self.types).order_by('-order').first()
            if last:
                self.order = last.order + 1
            else:
                self.order = 1

        super(Steps, self).save(*args, **kwargs)

    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=150)
    step_type = models.IntegerField(choices=(
        (0, "Sertifikasi Awal"),
        (1, "Survailen 1"),
        (2, "Survailen 2"),
    ))

    def __str__(self):
        return self.name    


class StepsSections(models.Model):
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, default=None)


class StepsForms(models.Model):
    section = models.ForeignKey(StepsSections, on_delete=models.CASCADE)
    form_type_choices = (
        (0, 'Number'),
        (1, 'Text'),
    )
    form_type = models.IntegerField(choices=form_type_choices, default=1)
    name = models.CharField(max_length=150)
    tooltip = models.TextField(null=True, default=None)

    def __str__(self):
        return self.name


class OfflineDocuments(models.Model):
    section = models.ForeignKey(StepsSections, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    tooltip = models.TextField(null=True, default=None)

    def __str__(self):
        return self.name


class Certifications(models.Model):
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    completed = models.IntegerField(default=0)
    left = models.IntegerField()
    created = models.BigIntegerField()
    updated = models.BigIntegerField()

    def __str__(self):
        return self.name


class CertificationsSteps(models.Model):
    certifications = models.ForeignKey(Certifications, on_delete=models.CASCADE)
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    validated = models.BooleanField(default=False)
    validator_role = models.IntegerField(default=0)
    validator = models.IntegerField(default=None, null=True, blank=True)
    validation_date = models.BigIntegerField(default=None, null=True, blank=True)


class CertificationsDetails(models.Model):
    certifications_steps = models.ForeignKey(CertificationsSteps, on_delete=models.CASCADE)
    steps_forms = models.ForeignKey(StepsForms, on_delete=models.CASCADE)
    steps_sections = models.ForeignKey(StepsSections, on_delete=models.CASCADE)
    value = models.TextField(default=None, null=True, blank=True)


class CertificationsOfflineDocuments(models.Model):
    certifications_steps = models.ForeignKey(CertificationsSteps, on_delete=models.CASCADE)
    offline_documents = models.ForeignKey(OfflineDocuments, on_delete=models.CASCADE)
    steps_sections = models.ForeignKey(StepsSections, on_delete=models.CASCADE)
    files_path = models.CharField(max_length=200, default=None, null=True, blank=True)
