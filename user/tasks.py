
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from user.models import User
from celery.decorators import task
from allauth.account.models import EmailAddress
from django.core import serializers
from datetime import datetime, timedelta
from django.conf import settings

@shared_task
def delete_unverified():
	count = 0
	emails = EmailAddress.objects.filter(verified=False)
	for e in emails:
		users = User.objects.filter(email=e.email, date_joined__lte=datetime.now()-timedelta(days=30))
		rows_affected = users.delete()
		if rows_affected > 0:
			e.delete()
		count += rows_affected[0]
	return count

@shared_task
def show_unverified():
	if settings.DEBUG:
		unverified_emails = "Unverified: "
		emails = EmailAddress.objects.filter(verified=False)
		for e in emails:
			unverified_emails += e.email
			unverified_emails += "  "
		return unverified_emails

@shared_task
def show_verified():
	if settings.DEBUG:
		unverified_emails = "Verified: "
		emails = EmailAddress.objects.filter(verified=True)
		for e in emails:
			unverified_emails += e.email
			unverified_emails += "  "
		return unverified_emails
"""
@shared_task
def mul(x, y):
    return x * y

EmailAddress.objects.filter(email=e, verified=False).delete()

@shared_task
def xsum(numbers):
    return sum(numbers)
    """