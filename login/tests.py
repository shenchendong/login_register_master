from django.test import TestCase

# Create your tests here.

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'login_register_master.settings'

if __name__ == "__main__":

    send_mail(
        '测试邮件',
        '欢迎访问',
        '314777533@qq.com',
        ['shenchendong@168.com'],
    )