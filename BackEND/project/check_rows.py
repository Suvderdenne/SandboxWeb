import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from django.db import connection

tables = ['app_user_user', 'users']
for table in tables:
    with connection.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = cur.fetchone()[0]
    print(f"{table} row count: {count}")
