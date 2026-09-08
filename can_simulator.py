import time

can_messages = [
{
    "can_id": "0x100",
    "ecu": "Engine ECU",
    "data": "speed=60"
},
{
    "can_id": "0x200",
    "ecu": "brake ECU",
    "data": "brake=OFF"
},
{
    "can_id": "0x300",
    "ecu": "Gateway ECU",
    "data": "status=NORMAL"
}
]

print("------Simulated Vehicle CAN Traffic-----")

for message in can_messages:

    print(

        message["can_id"],
        "|",
        message["ecu"],
        "|",
        message["data"]
    )
    time.sleep(1) #waits one second
