from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

class Task(models.Model):
    text = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('task_detail', args=[self.id])


class TaskItem(models.Model):
    text = models.TextField(default='')
    task = models.ForeignKey(Task, default=None)

