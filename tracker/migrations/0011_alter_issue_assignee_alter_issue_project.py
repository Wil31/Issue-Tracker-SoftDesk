# Generated by Django 4.0.4 on 2022-06-09 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tracker", "0010_alter_comment_author_alter_comment_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="assignee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="issue_assignee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="project",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issue_project",
                to="tracker.project",
            ),
        ),
    ]
