import os
import json
import psutil
import time

def create_user_file():
    with open("users.txt", "w") as file:
        file.write("1, Ансар, Admin\n")
        file.write("2, Александр, User\n")
        file.write("3, Данияр, Moderator\n")

def read_user_file():
    with open("users.txt", "r") as file:
        data = file.readlines()
        return [line.strip().split(", ") for line in data]

def update_user_file(user_id, new_data):
    data = read_user_file()
    with open("users.txt", "w") as file:
        for entry in data:
            if entry[0] == str(user_id):
                file.write(", ".join(new_data) + "\n")
            else:
                file.write(", ".join(entry) + "\n")

def delete_user_from_file(user_id):
    data = read_user_file()
    with open("users.txt", "w") as file:
        for entry in data:
            if entry[0] != str(user_id):
                file.write(", ".join(entry) + "\n")

def create_booking_file():
    with open("bookings.txt", "w") as file:
        file.write("101, 1, Room 1, confirmed\n")
        file.write("102, 2, Conference Hall, pending\n")

def read_booking_file():
    with open("bookings.txt", "r") as file:
        data = file.readlines()
        return [line.strip().split(", ") for line in data]

def update_booking_file(booking_id, new_data):
    data = read_booking_file()
    with open("bookings.txt", "w") as file:
        for entry in data:
            if entry[0] == str(booking_id):
                file.write(", ".join(new_data) + "\n")
            else:
                file.write(", ".join(entry) + "\n")

def delete_booking_from_file(booking_id):
    data = read_booking_file()
    with open("bookings.txt", "w") as file:
        for entry in data:
            if entry[0] != str(booking_id):
                file.write(", ".join(entry) + "\n")

def create_payment_file():
    with open("payments.txt", "w") as file:
        file.write("201, 2, 100.0, completed\n")
        file.write("202, 3, 50.0, pending\n")

def read_payment_file():
    with open("payments.txt", "r") as file:
        data = file.readlines()
        return [line.strip().split(", ") for line in data]

def update_payment_file(payment_id, new_data):
    data = read_payment_file()
    with open("payments.txt", "w") as file:
        for entry in data:
            if entry[0] == str(payment_id):
                file.write(", ".join(new_data) + "\n")
            else:
                file.write(", ".join(entry) + "\n")

def delete_payment_from_file(payment_id):
    data = read_payment_file()
    with open("payments.txt", "w") as file:
        for entry in data:
            if entry[0] != str(payment_id):
                file.write(", ".join(entry) + "\n")

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return {
        "cpu_usage": cpu,
        "memory_usage": memory
    }

def run_process(script_name):
    os.system(f"python {script_name}")

def monitor_system_log():
    with open("system_log.txt", "a") as log:
        while True:
            info = get_system_info()
            log.write(f"CPU: {info['cpu_usage']}%, Memory: {info['memory_usage']}%\n")
            time.sleep(5)

def load_system_data(file_name="state.json"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    else:
        return {
            "users": [
                {"id": 1, "name": "Ансар", "role": "Admin"},
                {"id": 2, "name": "Александр", "role": "User"}
            ],
            "bookings": [
                {"id": 101, "user_id": 1, "details": "Room 1", "status": "confirmed"},
                {"id": 102, "user_id": 2, "details": "Conference Hall", "status": "pending"}
            ],
            "payments": [
                {"id": 201, "user_id": 2, "amount": 100.0, "status": "completed"},
                {"id": 202, "user_id": 3, "amount": 50.0, "status": "pending"}
            ]
        }

def save_system_data(data, file_name="state.json"):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def update_system_data(file_name="state.json", user_updates=None, booking_updates=None, payment_updates=None):
    data = load_system_data(file_name)
    if user_updates:
        data["users"].extend(user_updates)
    if booking_updates:
        data["bookings"].extend(booking_updates)
    if payment_updates:
        data["payments"].extend(payment_updates)
    save_system_data(data, file_name)

if __name__ == "__main__":
    create_user_file()
    create_booking_file()
    create_payment_file()
    print("Users:", read_user_file())
    print("Bookings:", read_booking_file())
    print("Payments:", read_payment_file())

    print("System Info:", get_system_info())

    system_data = load_system_data()
    print("Loaded System Data:", system_data)
    update_system_data(user_updates=[{"id": 4, "name": "Charlie", "role": "Moderator"}])
    print("Updated System Data:", load_system_data())
