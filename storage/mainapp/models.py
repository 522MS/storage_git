import os

from django.db import models


# def extension(uploaded):
#     extension = uploaded.name.split('.')[-1]
#     return extension


class Document(models.Model):
    def extenDocumentsion(self):
        extension = os.path.splitext(self.uploadedFile.name)[-1]
        return extension

    uploadedFile = models.FileField(
        upload_to="",
        verbose_name='Файл',
        null=True,
    )

    title = models.CharField(
        verbose_name='название файла',
        max_length=200,
        default='',
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.title = self.uploadedFile.name.split('.')[-1]
        super(Document, self).save(*args, **kwargs)
