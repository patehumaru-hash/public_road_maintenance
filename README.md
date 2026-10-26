# Public Road Maintenance Tracking System

A Python OOP project for recording road damage and tracking
maintenance progress in Freetown.

All starting reports are fictional classroom examples.

## Features
- Add road damage reports.
- Display all reports.
- Search by report code.
- Update maintenance status.
- Reject duplicate codes and invalid entries.

## Run the program
Install Python 3, then run:

python main.py

No additional packages are needed.

## OOP concepts
- Classes: RoadReport and MaintenanceRegister.
- Dictionary: stores report objects by report code.
- Instance methods: display_info and update_status.
- Class method: create_pothole_report.
- Static method: is_valid_severity.
- Tuples: hold severity and status choices.

## Digital Public Goods principles
- Open source: released under the MIT licence.
- Inclusive design: offline operation and a numbered text menu.
- Privacy: no citizen names or contact details are requested.
- Reusable: separate classes manage reports and the register.

## Limitations
Records disappear when the program closes.
This prototype is not connected to a government service.

## Licence
MIT License. See LICENSE.