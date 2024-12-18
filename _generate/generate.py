# File is (mostly) Claude generated
import csv
import random
import uuid
from datetime import datetime, timedelta
import string

def generate_random_user_id():
    return f"USER{''.join(random.choices(string.digits, k=6))}"

def generate_random_transaction_id():
    return str(uuid.uuid4())

def generate_random_amount():
    return round(random.uniform(1.0, 1000.0), 2)

def generate_random_timestamp(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)
    return random_date.replace(hour=random_hours, minute=random_minutes, second=random_seconds).isoformat()

def generate_error_value():
    if random.random() < 0.5:
        random_length = random.randint(8, 16)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random_length))
    else:
        return ''

records = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

user_ids = [generate_random_user_id() for _ in range(100)]

ERROR_PROBABILITY = 0.05

for _ in range(10000):
    record = {
        'user_id': random.choice(user_ids),
        'transaction_id': generate_random_transaction_id(),
        'amount': generate_random_amount(),
        'timestamp': generate_random_timestamp(start_date, end_date)
    }
    
    if random.random() < ERROR_PROBABILITY:
        # Choose a random field to corrupt
        field_to_corrupt = random.choice(list(record.keys()))
        record[field_to_corrupt] = generate_error_value()
    
    records.append(record)

filename = 'data/input_data.csv'
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['user_id', 'transaction_id', 'amount', 'timestamp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for record in records:
        writer.writerow(record)

print(f"Generated {filename} with {len(records)} records")

