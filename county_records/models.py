from django.db import models
# Richard Roda
# The following models pertain to the Lien Search feature on BreazeHome
# CountyRecord and LienRecord

# Create your models here.
class CountyRecord(models.Model):
    cfn_number = models.CharField(
        max_length=4,
        null=True,
        blank=True
    )
    cfn_sequence = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    group_id = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    recording_date = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    recording_time = models.CharField(
        max_length=6,
        null=True,
        blank=True
    )
    recording_book = models.CharField(
        max_length=14,
        null=True,
        blank=True
    )
    recording_page = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    book_type = models.CharField(
        max_length = 5,
        null = True,
        blank=True
    )
    document_pages = models.CharField(
        max_length = 5,
        null = True,
        blank=True
    )
    append_pages = models.CharField(
        max_length = 5,
        null = True,
        blank=True
    )
    document_type = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    document_type_description = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    document_date = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    first_party = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    first_party_code = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    cross_party_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    original_cfn_year = models.CharField(
        max_length=4,
        null=True,
        blank=True
    )
    original_cfn_sequence = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    original_recording_book = models.CharField(
        max_length=14,
        null=True,
        blank=True
    )
    original_recording_page = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    original_misc_reference = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    subdivision_name = models.CharField(
        max_length=90,
        null=True,
        blank=True
    )
    folio_number = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    legal_description = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    section = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    township = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    range = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    plat_book = models.CharField(
        max_length=14,
        null=True,
        blank=True
    )
    plat_page = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    block = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    case_number = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    consideration_one = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    consideration_two = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    deed_doc_tax = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    single_family = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    surtax = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    intangible = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    doc_stamps = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    key = models.CharField(
        max_length=13,
        null=True,
        blank=True
    )
    transaction_type = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )
    party_sequence = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    modified_date = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )


class LienRecord(models.Model):
    cfn_number = models.CharField(
        max_length=4,
        null=True,
        blank=True
    )
    cfn_sequence = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    group_id = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    recording_date = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    recording_time = models.CharField(
        max_length=6,
        null=True,
        blank=True
    )
    recording_book = models.CharField(
        max_length=14,
        null=True,
        blank=True
    )
    recording_page = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    book_type = models.CharField(
        max_length = 5,
        null = True,
        blank=True
    )
    document_pages = models.CharField(
        max_length = 5,
        null = True,
        blank=True
    )
    append_pages = models.CharField(
        max_length = 5,
        null = True,
        blank=True
    )
    document_type_description = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    document_date = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    first_party = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    first_party_code = models.CharField(
        max_length=1,
        null=True,
        blank=True
    )
    cross_party_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    modified_date = models.CharField(
        max_length=8,
        null=True,
        blank=True
    )
    folio_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )


