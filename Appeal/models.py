from django.db import models

class Audit(models.Model):
    official_names = models.CharField(max_length=255, verbose_name="Please State Your Official Names")
    country = models.CharField(max_length=100, verbose_name="Please select your Country")
    assessor_name = models.CharField(max_length=255, verbose_name="Name Of Assessor that Audited the Call")
    assessor_email = models.EmailField(verbose_name="Quality Assessor Email address")
    phone_number = models.CharField(max_length=20, verbose_name="Appealed call phone number")
    agent_listened = models.CharField(max_length=5, verbose_name="Did Agent Listen to the Call again?")
    parameter_not_fairly_scored = models.CharField(max_length=255, verbose_name="Parameter that was supposedly not fairly scored")
    feedback_received = models.TextField(verbose_name="Feedback Received")
    reason_for_appeal = models.TextField(verbose_name="Please state your reason for appeal")
    call_link = models.URLField(verbose_name="Attach the link to the call that was audited")

    def __str__(self):
        return f"{self.official_names} - {self.phone_number}"
