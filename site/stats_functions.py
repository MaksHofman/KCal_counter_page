import sqlite3
from datetime import datetime, timedelta
import re

def account_creation_date_generation() -> datetime:
    return datetime.now()

# Get user's streaks by email
def get_streaks_by_email(email, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f'SELECT best_streak, current_streak, days_when_on_site FROM users WHERE email = "{email}";')
    output = cursor.fetchall()
    conn.close()
    return output[0][0], output[0][1], output[0][2]

# This function gets all the necessary info about account creation
def get_account_creation_info(email, database_path):
    account_created_date_str, account_created_date = get_account_created_date(email, database_path)
    days_from_account_creation = get_days_from_account_creation(account_created_date)
    return account_created_date_str, days_from_account_creation

def get_account_created_date(email, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f'SELECT account_created_date FROM users WHERE email = "{email}";')
    output = cursor.fetchall()
    conn.close()
    date_raw = output[0][0]

    # check if account creation date is empty in DB
    if not date_raw:
        return None, None

    account_created_date = datetime.strptime(output[0][0], '%Y-%m-%d %H:%M:%S.%f')
    account_created_date_str = account_created_date.strftime("%d.%m.%y")
    return account_created_date_str, account_created_date

def get_days_from_account_creation(account_created_date):
    return (datetime.now() - account_created_date).days
