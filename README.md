# Automotive CAN Security & TARA Lab

## Project Overview

This beginner-level automotive cybersecurity lab was created to understand how Electronic Control Units (ECUs) communicate over an in-vehicle CAN network and how basic cybersecurity threats can be identified.

The lab simulates Engine, Brake, and Gateway ECUs using Python and introduces basic CAN message monitoring, abnormal-message detection, and Threat Analysis and Risk Assessment (TARA).

## Objectives

- Understand basic ECU architecture
- Understand CAN communication concepts
- Simulate CAN-style vehicle messages
- Identify unexpected CAN messages
- Perform a basic TARA & translate identified threats into cybersecurity requirements

## Lab Architecture


                    SIMULATED VEHICLE

 Engine ECU --------\
                     \
 Brake ECU ----------- CAN BUS -------- Gateway ECU
                     /
                    /
             Unauthorized Actor
                    |
                    |
             Injects CAN Message
                    |
             Manipulates Data
                    |
                    v
          Python Security Monitor
                    |
             Abnormality Found
                    |
              HIGH ALERT
                    |
             Incident Escalation & Reporting

## Technologies

- Python
- Visual Studio Code
- Git/GitHub
- CAN fundamentals
- TARA fundamentals