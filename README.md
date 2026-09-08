# Automotive CAN Cybersecurity & TARA Home Lab

## Project Overview

This home lab was created to understand how basic vehicle ECUs communicate using CAN messages and how a cybersecurity engineer can identify suspicious CAN activity.

The project starts with a small set of normal CAN messages from an Engine ECU, Brake ECU, and Gateway ECU. I then added simulated malicious CAN messages and used a simple Python script to detect the abnormal activity. After identifying the suspicious messages, I performed a basic Threat Analysis and Risk Assessment (TARA) to understand the potential impact and recommend security controls.

---

## Project Flow

```text
Normal CAN Messages
        ↓
Create CAN Baseline
        ↓
Add Simulated Malicious Messages
        ↓
Run Python Detection Script
        ↓
Detect Abnormal CAN Activity
        ↓
Investigate Finding
        ↓
Perform TARA
        ↓
Recommend Security Controls


**## Outcome**

The home lab successfully detected both simulated CAN anomalies:

- A valid CAN ID carrying an abnormal `Speed=250` value.
- An unknown CAN ID `0x999` carrying a brake-related message.

Overall, the lab demonstrated the full workflow from **normal CAN baseline → malicious message injection → automated detection → risk assessment → security recommendations**.
