import csv

input_file = "data/can_messages.csv"
output_file = "data/attacked_can_messages"

#reading the normal CAN traffic

with open(input_file, "r") as file:

    reader = csv.DictReader(file)

    can_messages = list(reader)

#simulated malicious CAN messages

bad_message_1 = {
    "timestamp": "09:00:07",
    "can_id": "0x100",
    "ecu": "Engine ECU",
    "data": "Speed=250",
    "status": "NORMAL"
}

bad_message_2 = {
    "timestamp": "09:00:08",
    "can_id": "0x999",
    "ecu": "Unknown ECU",
    "data": "Brake=OFF",
    "status": "NORMAL"
}

# Add the bad messages to the normal traffic
can_messages.append(bad_message_1)
can_messages.append(bad_message_2)

# Save everything into a new CSV file
with open(output_file, "w", newline="") as file:

    columns = [
        "timestamp",
        "can_id",
        "ecu",
        "data",
        "status"
    ]

    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader()
    writer.writerows(can_messages)

print("Attack simulation completed.")
print("Bad CAN messages were added.")
print("New file created:", output_file)