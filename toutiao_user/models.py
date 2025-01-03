from django.db import models
from fake_useragent import UserAgent

def generate_random_user_agent():
    ua = UserAgent()
    return ua.random

class TTUser(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cookie = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = '头条用户'

    def save(self, *args, **kwargs):
        # 如果没有提供 user_agent 则使用随机生成的值
        if not self.user_agent:
            self.user_agent = generate_random_user_agent()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
