# management/commands/load_default_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = '加载默认数据到数据库'

    def handle(self, *args, **kwargs):
        # 创建默认用户
        user = get_user_model()
        if not user.objects.filter(username='admin').exists():
            user.objects.create_superuser(username='admin', password='passwd', email='admin@example.com')
            self.stdout.write(self.style.SUCCESS('默认管理员用户创建成功'))
        else:
            self.stdout.write(self.style.SUCCESS('默认管理员用户已存在'))

        self.stdout.write(self.style.SUCCESS('所有默认数据已成功导入'))
