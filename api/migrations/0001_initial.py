from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="harsha",
                          email="harshainukollu3@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="9652059241",
                          gender="Male"
                          )
        user.set_password("mar@2020")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
