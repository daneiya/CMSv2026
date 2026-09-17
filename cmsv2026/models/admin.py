import sqlite3

class ClinicalAdminSystem:
    def __init__(self, db_name="clinic.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # 1. View all scheduled appointments with patient and doctor details
    def view_all_appointments(self):
        query = """
            SELECT appointments.id, patients.name, doctors.name, appointments.date, appointments.status 
            FROM appointments
            JOIN patients ON appointments.patient_id = patients.id
            JOIN doctors ON appointments.doctor_id = doctors.id
        """
        self.cursor.execute(query)
        appointments = self.cursor.fetchall()
        
        print("\n--- CLINIC APPOINTMENTS ---")
        for appt in appointments:
            print(f"ID: {appt[0]} | Patient: {appt[1]} | Doctor: {appt[2]} | Date: {appt[3]} | Status: {appt[4]}")

    # 2. Update an appointment status (e.g., Scheduled -> Completed / Cancelled)
    def update_appointment_status(self, appointment_id, new_status):
        query = "UPDATE appointments SET status = ? WHERE id = ?"
        self.cursor.execute(query, (new_status, appointment_id))
        self.conn.commit()
        print(f"\n[Success] Appointment ID {appointment_id} updated to '{new_status}'.")

    # 3. Add a new doctor to the clinic panel
    def add_doctor(self, name, specialization):
        query = "INSERT INTO doctors (name, specialization) VALUES (?, ?)"
        self.cursor.execute(query, (name, specialization))
        self.conn.commit()
        print(f"\n[Success] Doctor {name} ({specialization}) added to system.")

    def close(self):
        self.conn.close()

# --- ADMIN MENU INTERFACE ---
if __name__ == "__main__":
    admin = ClinicalAdminSystem()
    
    while True:
        print("\n===== CLINICAL MANAGEMENT ADMIN SYSTEM =====")
        print("1. View All Appointments")
        print("2. Update Appointment Status")
        print("3. Add New Doctor")
        print("4. Exit")
        
        choice = input("Enter choices (1-4): ")
        
        if choice == "1":
            admin.view_all_appointments()
        elif choice == "2":
            appt_id = input("Enter Appointment ID: ")
            status = input("Enter New Status (Scheduled/Completed/Cancelled): ")
            admin.update_appointment_status(appt_id, status)
        elif choice == "3":
            doc_name = input("Enter Doctor's Name: ")
            spec = input("Enter Specialization: ")
            admin.add_doctor(doc_name, spec)
        elif choice == "4":
            admin.close()
            print("Exiting Admin System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
