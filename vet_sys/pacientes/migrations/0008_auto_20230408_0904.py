from django.contrib.postgres.operations import UnaccentExtension

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_paciente_peso'),
    ]

    operations = [
        UnaccentExtension()
    ]
