# Generated by Django 4.0.5 on 2022-06-30 23:54

from django.db import migrations, models
import endpoint_manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint_manager', '0008_alter_api_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_http', models.IntegerField(choices=[('GET', endpoint_manager.models.MetodosRequisicao['GET']), ('POST', endpoint_manager.models.MetodosRequisicao['POST']), ('PUT', endpoint_manager.models.MetodosRequisicao['PUT']), ('DELETE', endpoint_manager.models.MetodosRequisicao['DELETE']), ('PATCH', endpoint_manager.models.MetodosRequisicao['PATCH'])])),
                ('tipo_retorno', models.IntegerField(choices=[('JSON', endpoint_manager.models.RetornosRequisicao['JSON']), ('XML', endpoint_manager.models.RetornosRequisicao['XML'])])),
                ('retorno', models.TextField()),
            ],
        ),
    ]
