USERS = [
    {"id": 1, "name": "Ансар", "role": "admin"},
    {"id": 2, "name": "Александр", "role": "user"},
    {"id": 3, "name": "Данияр", "role": "user"}
]

BOOKINGS = [
    {"id": 101, "user_id": 1, "details": "Room 1, 2 hours", "status": "confirmed"},
    {"id": 102, "user_id": 2, "details": "Conference Hall, 4 hours", "status": "pending"}
]

PAYMENTS = [
    {"id": 201, "user_id": 2, "amount": 100.0, "status": "completed"},
    {"id": 202, "user_id": 3, "amount": 50.0, "status": "pending"}
]

def get_users():
    return USERS

def get_bookings():
    return BOOKINGS

def get_payments():
    return PAYMENTS
