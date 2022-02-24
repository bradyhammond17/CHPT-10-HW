import PatientClass as pat
import ProcedureClass as proc


def main():

    # Create instance of Patient class for Matt Jones
    Matt = pat.Patient(
        "1", "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True
    )

    # Create instances for the three Procedures
    procedure1 = proc.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, "1")
    procedure2 = proc.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, "1")
    procedure3 = proc.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, "2")

    # Display bill
    # Patient info
    print("*** Patient Bill ***")
    print("Name:", Matt.get_name())
    print("Address:", Matt.get_address())
    print("Phone:", Matt.get_phone() + "\n")

    # Procedures
    print("Procedure:", procedure1.get_procedure())
    print("Date:", procedure1.get_date())
    print("Practitioner:", procedure1.get_practitioner())
    print("Charge: $" + format(procedure1.get_charges(), ".2f") + "\n")

    print("Procedure:", procedure2.get_procedure())
    print("Date:", procedure2.get_date())
    print("Practitioner:", procedure2.get_practitioner())
    print("Charge: $" + format(procedure2.get_charges(), ",.2f") + "\n")

    # Calculate and display total charge
    total_charge = procedure1.get_charges() + procedure2.get_charges()
    if Matt.get_veteran_status() == True:
        total_charge *= 0.6
    print("Total Charges: $" + format((total_charge), ",.2f"))


main()
