import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from django.db import connection

for table in ['app_user_user', 'users']:
    print(f"\n{table} columns:")
    with connection.cursor() as cur:
        cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name=%s ORDER BY ordinal_position", [table])
        for row in cur.fetchall():
            print(f"  {row[0]} ({row[1]})")
