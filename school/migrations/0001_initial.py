# Generated by Django 4.1 on 2023-01-02 12:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("surname", models.CharField(max_length=20, null=True)),
                ("First_Name", models.CharField(max_length=20, null=True)),
                ("Other_Name", models.CharField(max_length=20, null=True)),
                ("Date_of_Birth", models.DateField()),
                ("postal_address", models.CharField(max_length=50, null=True)),
                ("Residential_Address", models.CharField(max_length=50, null=True)),
                ("Latest_school_addresss", models.CharField(max_length=50, null=True)),
                (
                    "Latest_class_Attended",
                    models.CharField(
                        choices=[
                            ("Nur1", "Nursery 1"),
                            ("Nur2", "Nursery 2"),
                            ("Nur3", "Nursery 2"),
                            ("Pry1", "Primary 1"),
                            ("Pry2", "Primary 2"),
                            ("Pry3", "Primary 3"),
                            ("Pry4", "Primary 4"),
                            ("Pry5", "Primary 5"),
                        ],
                        default="Nur1",
                        max_length=20,
                    ),
                ),
                (
                    "Home_telephone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                ("name_of_father", models.CharField(max_length=20, null=True)),
                ("Occupation_of_Father", models.CharField(max_length=20, null=True)),
                (
                    "Contact_address_of_Father",
                    models.CharField(max_length=20, null=True),
                ),
                (
                    "tel_No_of_Father",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                ("name_of_mother", models.CharField(max_length=20, null=True)),
                ("Occupation_of_mother", models.CharField(max_length=20, null=True)),
                (
                    "Contact_address_of_mother",
                    models.CharField(max_length=20, null=True),
                ),
                (
                    "tel_No_of_mother",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                (
                    "who_to_call_in_case_of_emergency",
                    models.CharField(max_length=20, null=True),
                ),
                ("any_allergy_or_physical_deafect", models.CharField(max_length=20)),
                ("picture", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
