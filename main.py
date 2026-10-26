"""
PUBLIC ROAD MAINTENANCE TRACKING SYSTEM
PROG211 - Object-Oriented Programming

All starting reports are fictional examples.
The program does not connect to a government service.
Records remain in memory only and disappear on exit.
"""


class RoadReport:
    """Represents one road damage report."""

    # Optional tuples: fixed choices used by the program.
    SEVERITIES = ("Low", "Medium", "High")
    STATUSES = ("Reported", "In Progress", "Completed")

    def __init__(self, report_id, location, damage_type, severity):
        report_id = report_id.strip().upper()
        location = location.strip()
        damage_type = damage_type.strip()
        severity = severity.strip().title()

        if not (
            report_id.startswith("RD")
            and len(report_id) == 5
            and report_id[2:].isascii()
            and report_id[2:].isdigit()
        ):
            raise ValueError("Use a report code such as RD001.")

        if not location:
            raise ValueError("Location cannot be blank.")

        if not damage_type:
            raise ValueError("Damage type cannot be blank.")

        if not self.is_valid_severity(severity):
            raise ValueError("Severity must be Low, Medium or High.")

        # Attributes belonging to each individual report.
        self.report_id = report_id
        self.location = location
        self.damage_type = damage_type
        self.severity = severity
        self.status = "Reported"

    @staticmethod
    def is_valid_severity(severity):
        """Checks a value without needing an individual report."""
        return severity in RoadReport.SEVERITIES

    @classmethod
    def create_pothole_report(cls, report_id, location, severity):
        """Alternative way to create a report for a pothole."""
        return cls(report_id, location, "Pothole", severity)

    def update_status(self, new_status):
        """Changes the maintenance status of this report."""
        new_status = new_status.strip().title()

        if new_status not in self.STATUSES:
            raise ValueError(
                "Choose Reported, In Progress or Completed."
            )

        if new_status == self.status:
            return "This report already has that status."

        current_position = self.STATUSES.index(self.status)
        new_position = self.STATUSES.index(new_status)

        # Prototype rule: move forward one maintenance stage at a time.
        if new_position != current_position + 1:
            raise ValueError(
                "Follow: Reported -> In Progress -> Completed."
            )

        self.status = new_status
        return "Maintenance status updated successfully."

    def display_info(self):
        """Displays this report."""
        print("-" * 45)
        print(f"Report code : {self.report_id}")
        print(f"Location    : {self.location}")
        print(f"Damage type : {self.damage_type}")
        print(f"Severity    : {self.severity}")
        print(f"Status      : {self.status}")


class MaintenanceRegister:
    """Stores and manages RoadReport objects."""

    def __init__(self, register_name):
        self.register_name = register_name

        # One dictionary stores all report objects.
        self.reports = {}

    def add_report(self, report):
        """Adds a report without overwriting an existing code."""
        if report.report_id in self.reports:
            raise ValueError("This report code already exists.")

        self.reports[report.report_id] = report

    def find_report(self, report_id):
        """Returns the report matching the supplied code."""
        report_id = report_id.strip().upper()

        if report_id not in self.reports:
            raise ValueError("Report not found.")

        return self.reports[report_id]

    def update_report(self, report_id, new_status):
        """Demonstrates interaction between register and report."""
        report = self.find_report(report_id)
        return report.update_status(new_status)

    def display_reports(self):
        """Loops through and displays the stored objects."""
        print(f"\n{self.register_name}")
        print("CLASSROOM DEMONSTRATION - unverified reports")

        if not self.reports:
            print("No reports have been added.")
            return

        for report in self.reports.values():
            report.display_info()

        print("-" * 45)
        print(f"Total reports: {len(self.reports)}")


def load_sample_reports(register):
    """Adds fictional reports using the supplied locations."""

    register.add_report(
        RoadReport.create_pothole_report(
            "RD001", "Goderich Street", "High"
        )
    )

    register.add_report(
        RoadReport(
            "RD002", "Circular Road", "Road crack", "Medium"
        )
    )

    register.add_report(
        RoadReport.create_pothole_report(
            "RD003", "Wilkinson Road", "Medium"
        )
    )

    register.add_report(
        RoadReport(
            "RD004", "Spur Road", "Road erosion", "High"
        )
    )

    register.add_report(
        RoadReport.create_pothole_report(
            "RD005", "Lumley Road", "Low"
        )
    )

    register.add_report(
        RoadReport(
            "RD006", "Campbell Street", "Road crack", "Low"
        )
    )

    register.add_report(
        RoadReport(
            "RD007", "St John area", "Road erosion", "Medium"
        )
    )

    register.add_report(
        RoadReport.create_pothole_report(
            "RD008", "Regent Road", "High"
        )
    )


def main():
    register = MaintenanceRegister(
        "Freetown Public Road Maintenance Register"
    )

    load_sample_reports(register)

    print("=" * 50)
    print("PUBLIC ROAD MAINTENANCE TRACKING SYSTEM")
    print("=" * 50)
    print("Starting reports are fictional demonstration data.")
    print("Do not enter names, phone numbers or private addresses.")
    print("Records disappear when you close the program.")

    while True:
        print("\nMAIN MENU")
        print("1. Add road damage report")
        print("2. Display all reports")
        print("3. Search for a report")
        print("4. Update maintenance status")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                print("\nADD ROAD DAMAGE REPORT")

                report_id = input("Report code, e.g. RD009: ")
                location = input("Public road or area: ")
                damage_type = input("Damage type: ")
                severity = input(
                    "Severity (Low, Medium or High): "
                )

                report = RoadReport(
                    report_id,
                    location,
                    damage_type,
                    severity
                )

                register.add_report(report)
                print("Report added successfully.")

            elif choice == "2":
                register.display_reports()

            elif choice == "3":
                report_id = input("Enter report code: ")
                report = register.find_report(report_id)
                report.display_info()

            elif choice == "4":
                report_id = input("Enter report code: ")

                report = register.find_report(report_id)
                report.display_info()

                print("\nMaintenance order:")
                print("Reported -> In Progress -> Completed")

                new_status = input("Enter new status: ")

                message = register.update_report(
                    report_id, new_status
                )

                print(message)

            elif choice == "5":
                print("Program closed. Temporary records are not saved.")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 5.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed.")