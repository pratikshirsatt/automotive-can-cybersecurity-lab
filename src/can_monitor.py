import pandas as pd

# -----------------------------------
# STEP 1: Read the two CSV files
# -----------------------------------

normal_data = pd.read_csv("data/can_messages.csv")
attacked_data = pd.read_csv("data/attacked_can_messages.csv")


# -----------------------------------
# STEP 2: Get the valid CAN IDs
# from the normal CAN file
# -----------------------------------

valid_can_ids = normal_data["can_id"].unique()

print("Valid CAN IDs:")
print(valid_can_ids)


# -----------------------------------
# STEP 3: Check every CAN message
# -----------------------------------

for index, row in attacked_data.iterrows():

    # METHOD 1:
    # Detect an unknown CAN ID

    if row["can_id"] not in valid_can_ids:

        print("\nALERT - UNKNOWN CAN ID")
        print("Time:", row["timestamp"])
        print("CAN ID:", row["can_id"])
        print("ECU:", row["ecu"])
        print("Data:", row["data"])


    # METHOD 2:
    # Detect an abnormal vehicle speed

    if str(row["data"]).startswith("Speed="):

        # Remove "Speed=" and keep only the number
        speed = int(row["data"].replace("Speed=", ""))

        # For this home lab we define
        # anything above 120 as suspicious

        if speed > 120:

            print("\nALERT - ABNORMAL SPEED MESSAGE")
            print("Time:", row["timestamp"])
            print("CAN ID:", row["can_id"])
            print("ECU:", row["ecu"])
            print("Speed:", speed)