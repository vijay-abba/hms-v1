from exceptions.custom_exceptions import HMSBaseExpection
from modules.department import Department
from rich.console import Console
from tabulate import tabulate

console = Console()


def safe_run(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except HMSBaseExpection as e:
        console.print(f"[ERROR] {e.message}", style="bold red")
    except KeyboardInterrupt:
        console.print("\n[Info] Operation cancelled by user.\n", style="bold red")
    except Exception as e:
        console.print(f"\n [UNEXPECTED ERROR] {e}\n", style="bold red")


def department_menu():

    dept = Department()
    while True:
        console.print("\n ---- Department Management ----", style="bold blue")
        print("1. Add Department")
        print("2. View All Department")
        print("3. Get Department By ID")
        print("4. Update Department")
        print("5. Delete Department")
        print("0. Back")

        dep_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if dep_choice == "1":

            def _add():
                department_name = console.input("[bold yellow]Enter Department name: ")
                department_code = console.input("[bold yellow]Enter Department code: ")
                dept.add(department_name, department_code)

            safe_run(_add)

        elif dep_choice == "2":
            rows = safe_run(dept.get_all)
            print(tabulate(rows, headers="keys", tablefmt="github"))
        elif dep_choice == "3":
            print("Get dep by id")
        elif dep_choice == "4":
            print("update department")
        elif dep_choice == "5":
            print("delete department")
        elif dep_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def patient_menu():
    while True:
        console.print("\n ---- Patient Management ----", style="bold blue")
        print("1. Add Patient")
        print("2. View All Patient")
        print("3. Get Patient By ID")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("0. Back")

        patient_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if patient_choice == "1":
            print("adding")
        elif patient_choice == "2":
            print("view all")
        elif patient_choice == "3":
            print("Get dep by id")
        elif patient_choice == "4":
            print("update patient")
        elif patient_choice == "5":
            print("delete Patient")
        elif patient_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def doctor_menu():
    while True:
        console.print("\n ---- Doctor Management ----", style="bold blue")

        print("1. Add Doctor")
        print("2. View All Doctor")
        print("3. Get Doctor By ID")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("0. Back")

        doctor_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if doctor_choice == "1":
            print("adding")
        elif doctor_choice == "2":
            print("view all")
        elif doctor_choice == "3":
            print("Get dep by id")
        elif doctor_choice == "4":
            print("update doctor")
        elif doctor_choice == "5":
            print("delete doctor")
        elif doctor_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def appointment_menu():
    while True:
        console.print("\n ---- Appointment Management ----", style="bold blue")

        print("1. Book Appointment")
        print("2. View All Appointment")
        print("3. Get Appointment By ID")
        print("4. Update Appointment")
        print("5. Delete Appointment")
        print("6. Cancel Appointment")
        print("0. Back")

        app_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if app_choice == "1":
            print("adding")
        elif app_choice == "2":
            print("view all")
        elif app_choice == "3":
            print("Get dep by id")
        elif app_choice == "4":
            print("update Appointment")
        elif app_choice == "5":
            print("delete Appointment")
        elif app_choice == "6":
            print("Cancel Appointment")
        elif app_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def treatment_menu():
    while True:
        console.print("\n ---- Treatment Management ----", style="bold blue")

        print("1. Add Treatment")
        print("2. View All Treatment")
        print("3. Get Treatment By ID")
        print("4. Update Treatment")
        print("5. Delete Treatment")
        print("0. Back")

        treatment_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if treatment_choice == "1":
            print("adding")
        elif treatment_choice == "2":
            print("view all")
        elif treatment_choice == "3":
            print("Get dep by id")
        elif treatment_choice == "4":
            print("update Treatment")
        elif treatment_choice == "5":
            print("delete Treatment")
        elif treatment_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def billing_menu():
    while True:
        console.print("\n ---- Billing Management ----", style="bold blue")

        print("1. Add Bill (manual)")
        print("2. Auto-Generate Bill from Treatments")
        print("3. Vill All Bills ")
        print("4. Get Bill By ID")
        print("5. Update Bill")
        print("6. Delete Bill")
        print("0. Back")

        bill_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if bill_choice == "1":
            print("adding")
        elif bill_choice == "2":
            print("view all")
        elif bill_choice == "3":
            print("Get dep by id")
        elif bill_choice == "4":
            print("update bill")
        elif bill_choice == "5":
            print("delete bill")
        elif bill_choice == "6":
            print("delete bill")
        elif bill_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def dashboard_menu():
    while True:
        console.print("\n ---- Dashboard ----", style="bold blue")

        print("1. Summary Numbers")
        print("2. Top Doctors By Revenue")
        print("3. Patients per Department")
        print("4. Monthly Revenue Trend")
        print("5. Pending Payments")
        print("6. Most common Treatments")
        print("0. Back")

        dep_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if dep_choice == "1":
            print("Summary Numbers")
        elif dep_choice == "2":
            print("Top Doctors By Revenue")
        elif dep_choice == "3":
            print("Patients per Department")
        elif dep_choice == "4":
            print("Monthly Revenue Trend")
        elif dep_choice == "5":
            print("Pending Payments")
        elif dep_choice == "6":
            print("Most common Treatments")
        elif dep_choice == "0":
            break
        else:
            console.print("Invalid choice", style="bold red")


def main_menu():

    while True:
        console.print("=" * 45, style="bold blue", height=100)
        console.print(
            " HOSPITAL MANAGEMENT SYSTEM (HMS)", style="bold blue", height=100
        )
        console.print("=" * 45, style="bold blue", height=100)

        print("1. Department Management")
        print("2. Patient Management")
        print("3. Doctor Management")
        print("4. Appointment Management")
        print("5. Treatment Management")
        print("6. Billing Management")
        print("7. Dashboard")
        print("0. Exit")
        user_choice = console.input(
            "[bold yellow] Enter choice: ",
        ).strip()

        if user_choice == "1":
            department_menu()
        elif user_choice == "2":
            patient_menu()
        elif user_choice == "3":
            doctor_menu()
        elif user_choice == "4":
            appointment_menu()
        elif user_choice == "5":
            treatment_menu()
        elif user_choice == "6":
            billing_menu()
        elif user_choice == "7":
            dashboard_menu()
        elif user_choice == "0":
            console.print("Thank you", style="bold green")
            break
        else:
            console.print("Invalid Option", style="bold red")


main_menu()
