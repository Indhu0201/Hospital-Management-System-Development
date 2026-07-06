import reflex as rx
from typing import TypedDict


class Doctor(TypedDict):
    id: int
    name: str
    specialty: str
    email: str
    department: str
    status: str
    phone: str


class Nurse(TypedDict):
    id: int
    name: str
    department: str
    shift: str
    status: str
    email: str
    tasks_done: int
    tasks_total: int


class Patient(TypedDict):
    id: int
    name: str
    email: str
    age: int
    gender: str
    blood_type: str
    phone: str
    disease: str
    admission_status: str
    admission_date: str
    room: str
    doctor_id: int
    nurse_id: int
    treatment_progress: int


class Appointment(TypedDict):
    id: int
    patient_id: int
    patient_name: str
    doctor_id: int
    doctor_name: str
    date: str
    time: str
    reason: str
    status: str


class Prescription(TypedDict):
    id: int
    patient_id: int
    patient_name: str
    doctor_name: str
    medicine: str
    dosage: str
    frequency: str
    duration: str
    date: str
    notes: str


class HistoryEntry(TypedDict):
    id: int
    patient_id: int
    date: str
    diagnosis: str
    doctor_name: str
    notes: str


class Vital(TypedDict):
    id: int
    patient_id: int
    patient_name: str
    date: str
    time: str
    bp: str
    hr: str
    temp: str
    spo2: str
    nurse_name: str


class NurseTask(TypedDict):
    id: int
    nurse_id: int
    patient_id: int
    patient_name: str
    task: str
    time: str
    status: str
    priority: str


class MedSchedule(TypedDict):
    id: int
    nurse_id: int
    patient_id: int
    patient_name: str
    medicine: str
    dosage: str
    time: str
    status: str


class ClinicalNote(TypedDict):
    id: int
    patient_id: int
    author: str
    role: str
    note: str
    date: str


class HealthcareState(rx.State):
    active_tab: str = "overview"
    selected_patient_id: int = 0
    filter_status: str = "all"
    search_query: str = ""

    doctors: list[Doctor] = [
        {
            "id": 1,
            "name": "Dr. Sarah Rivera",
            "specialty": "Cardiology",
            "email": "sarah.rivera@medicare.com",
            "department": "Cardiology",
            "status": "Available",
            "phone": "+1 555-0101",
        },
        {
            "id": 2,
            "name": "Dr. James Chen",
            "specialty": "Neurology",
            "email": "james.chen@medicare.com",
            "department": "Neurology",
            "status": "In Surgery",
            "phone": "+1 555-0102",
        },
        {
            "id": 3,
            "name": "Dr. Priya Patel",
            "specialty": "Pediatrics",
            "email": "priya.patel@medicare.com",
            "department": "Pediatrics",
            "status": "Available",
            "phone": "+1 555-0103",
        },
        {
            "id": 4,
            "name": "Dr. Marcus Lee",
            "specialty": "Orthopedics",
            "email": "marcus.lee@medicare.com",
            "department": "Orthopedics",
            "status": "On Rounds",
            "phone": "+1 555-0104",
        },
        {
            "id": 5,
            "name": "Dr. Elena Vasquez",
            "specialty": "Dermatology",
            "email": "elena.vasquez@medicare.com",
            "department": "Dermatology",
            "status": "Available",
            "phone": "+1 555-0105",
        },
    ]

    nurses: list[Nurse] = [
        {
            "id": 1,
            "name": "Nurse Amelia Foster",
            "department": "Cardiology",
            "shift": "Morning",
            "status": "On Duty",
            "email": "amelia.foster@medicare.com",
            "tasks_done": 8,
            "tasks_total": 12,
        },
        {
            "id": 2,
            "name": "Nurse David Kim",
            "department": "Neurology",
            "shift": "Evening",
            "status": "On Duty",
            "email": "david.kim@medicare.com",
            "tasks_done": 5,
            "tasks_total": 10,
        },
        {
            "id": 3,
            "name": "Nurse Rachel Green",
            "department": "Pediatrics",
            "shift": "Morning",
            "status": "Break",
            "email": "rachel.green@medicare.com",
            "tasks_done": 6,
            "tasks_total": 9,
        },
        {
            "id": 4,
            "name": "Nurse Omar Hassan",
            "department": "Orthopedics",
            "shift": "Night",
            "status": "On Duty",
            "email": "omar.hassan@medicare.com",
            "tasks_done": 4,
            "tasks_total": 8,
        },
        {
            "id": 5,
            "name": "Nurse Lily Zhang",
            "department": "ICU",
            "shift": "Morning",
            "status": "On Duty",
            "email": "lily.zhang@medicare.com",
            "tasks_done": 10,
            "tasks_total": 15,
        },
    ]

    patients: list[Patient] = [
        {
            "id": 1,
            "name": "John Anderson",
            "email": "john.anderson@email.com",
            "age": 54,
            "gender": "Male",
            "blood_type": "O+",
            "phone": "+1 555-1001",
            "disease": "Hypertension",
            "admission_status": "Admitted",
            "admission_date": "2024-11-14",
            "room": "302-A",
            "doctor_id": 1,
            "nurse_id": 1,
            "treatment_progress": 65,
        },
        {
            "id": 2,
            "name": "Maria Gonzalez",
            "email": "maria.g@email.com",
            "age": 38,
            "gender": "Female",
            "blood_type": "A+",
            "phone": "+1 555-1002",
            "disease": "Migraine",
            "admission_status": "Outpatient",
            "admission_date": "2024-11-18",
            "room": "-",
            "doctor_id": 2,
            "nurse_id": 2,
            "treatment_progress": 40,
        },
        {
            "id": 3,
            "name": "Ethan Brooks",
            "email": "ethan.b@email.com",
            "age": 8,
            "gender": "Male",
            "blood_type": "B+",
            "phone": "+1 555-1003",
            "disease": "Asthma",
            "admission_status": "Admitted",
            "admission_date": "2024-11-16",
            "room": "108-B",
            "doctor_id": 3,
            "nurse_id": 3,
            "treatment_progress": 80,
        },
        {
            "id": 4,
            "name": "Sophia Carter",
            "email": "sophia.c@email.com",
            "age": 45,
            "gender": "Female",
            "blood_type": "AB-",
            "phone": "+1 555-1004",
            "disease": "Fractured Femur",
            "admission_status": "Admitted",
            "admission_date": "2024-11-12",
            "room": "205-C",
            "doctor_id": 4,
            "nurse_id": 4,
            "treatment_progress": 55,
        },
        {
            "id": 5,
            "name": "William Zhang",
            "email": "will.z@email.com",
            "age": 62,
            "gender": "Male",
            "blood_type": "O-",
            "phone": "+1 555-1005",
            "disease": "Coronary Artery Disease",
            "admission_status": "Admitted",
            "admission_date": "2024-11-10",
            "room": "301-B",
            "doctor_id": 1,
            "nurse_id": 1,
            "treatment_progress": 70,
        },
        {
            "id": 6,
            "name": "Isabella Nguyen",
            "email": "bella.n@email.com",
            "age": 29,
            "gender": "Female",
            "blood_type": "A-",
            "phone": "+1 555-1006",
            "disease": "Anxiety Disorder",
            "admission_status": "Outpatient",
            "admission_date": "2024-11-19",
            "room": "-",
            "doctor_id": 2,
            "nurse_id": 2,
            "treatment_progress": 30,
        },
        {
            "id": 7,
            "name": "Liam O'Brien",
            "email": "liam.o@email.com",
            "age": 71,
            "gender": "Male",
            "blood_type": "B-",
            "phone": "+1 555-1007",
            "disease": "Post-Op Recovery",
            "admission_status": "Admitted",
            "admission_date": "2024-11-15",
            "room": "402-A",
            "doctor_id": 4,
            "nurse_id": 5,
            "treatment_progress": 85,
        },
    ]

    appointments: list[Appointment] = [
        {
            "id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "doctor_id": 1,
            "doctor_name": "Dr. Sarah Rivera",
            "date": "2024-11-20",
            "time": "09:00 AM",
            "reason": "Follow-up Cardiology",
            "status": "Confirmed",
        },
        {
            "id": 2,
            "patient_id": 2,
            "patient_name": "Maria Gonzalez",
            "doctor_id": 2,
            "doctor_name": "Dr. James Chen",
            "date": "2024-11-20",
            "time": "10:30 AM",
            "reason": "Migraine Consultation",
            "status": "Pending",
        },
        {
            "id": 3,
            "patient_id": 3,
            "patient_name": "Ethan Brooks",
            "doctor_id": 3,
            "doctor_name": "Dr. Priya Patel",
            "date": "2024-11-20",
            "time": "11:00 AM",
            "reason": "Asthma Check",
            "status": "Confirmed",
        },
        {
            "id": 4,
            "patient_id": 4,
            "patient_name": "Sophia Carter",
            "doctor_id": 4,
            "doctor_name": "Dr. Marcus Lee",
            "date": "2024-11-20",
            "time": "02:00 PM",
            "reason": "Post-Op Review",
            "status": "Confirmed",
        },
        {
            "id": 5,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "doctor_id": 1,
            "doctor_name": "Dr. Sarah Rivera",
            "date": "2024-11-21",
            "time": "09:30 AM",
            "reason": "CAD Monitoring",
            "status": "Pending",
        },
        {
            "id": 6,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "doctor_id": 1,
            "doctor_name": "Dr. Sarah Rivera",
            "date": "2024-11-25",
            "time": "10:00 AM",
            "reason": "Blood Pressure Review",
            "status": "Confirmed",
        },
        {
            "id": 7,
            "patient_id": 6,
            "patient_name": "Isabella Nguyen",
            "doctor_id": 2,
            "doctor_name": "Dr. James Chen",
            "date": "2024-11-22",
            "time": "03:00 PM",
            "reason": "Therapy Session",
            "status": "Completed",
        },
    ]

    prescriptions: list[Prescription] = [
        {
            "id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "doctor_name": "Dr. Sarah Rivera",
            "medicine": "Lisinopril",
            "dosage": "10mg",
            "frequency": "Once daily",
            "duration": "30 days",
            "date": "2024-11-14",
            "notes": "Take with morning meal",
        },
        {
            "id": 2,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "doctor_name": "Dr. Sarah Rivera",
            "medicine": "Atorvastatin",
            "dosage": "20mg",
            "frequency": "Nightly",
            "duration": "60 days",
            "date": "2024-11-14",
            "notes": "Take at bedtime",
        },
        {
            "id": 3,
            "patient_id": 2,
            "patient_name": "Maria Gonzalez",
            "doctor_name": "Dr. James Chen",
            "medicine": "Sumatriptan",
            "dosage": "50mg",
            "frequency": "As needed",
            "duration": "14 days",
            "date": "2024-11-18",
            "notes": "For acute migraine attacks",
        },
        {
            "id": 4,
            "patient_id": 3,
            "patient_name": "Ethan Brooks",
            "doctor_name": "Dr. Priya Patel",
            "medicine": "Albuterol Inhaler",
            "dosage": "2 puffs",
            "frequency": "Every 4-6 hours",
            "duration": "Ongoing",
            "date": "2024-11-16",
            "notes": "Rescue inhaler",
        },
        {
            "id": 5,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "doctor_name": "Dr. Sarah Rivera",
            "medicine": "Metoprolol",
            "dosage": "25mg",
            "frequency": "Twice daily",
            "duration": "90 days",
            "date": "2024-11-10",
            "notes": "Monitor heart rate",
        },
    ]

    medical_history: list[HistoryEntry] = [
        {
            "id": 1,
            "patient_id": 1,
            "date": "2024-06-12",
            "diagnosis": "Stage 1 Hypertension",
            "doctor_name": "Dr. Sarah Rivera",
            "notes": "BP consistently elevated. Started on Lisinopril.",
        },
        {
            "id": 2,
            "patient_id": 1,
            "date": "2024-09-04",
            "diagnosis": "High Cholesterol",
            "doctor_name": "Dr. Sarah Rivera",
            "notes": "LDL 165 mg/dL. Started statin therapy.",
        },
        {
            "id": 3,
            "patient_id": 1,
            "date": "2024-11-14",
            "diagnosis": "Cardiology Follow-up",
            "doctor_name": "Dr. Sarah Rivera",
            "notes": "BP improving. Continue current regimen.",
        },
        {
            "id": 4,
            "patient_id": 2,
            "date": "2024-08-22",
            "diagnosis": "Chronic Migraine",
            "doctor_name": "Dr. James Chen",
            "notes": "Frequency 4-5/month. Trigger identification advised.",
        },
        {
            "id": 5,
            "patient_id": 3,
            "date": "2024-05-10",
            "diagnosis": "Persistent Asthma",
            "doctor_name": "Dr. Priya Patel",
            "notes": "Well controlled with inhaler.",
        },
    ]

    vitals: list[Vital] = [
        {
            "id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "date": "2024-11-19",
            "time": "08:00 AM",
            "bp": "138/86",
            "hr": "76",
            "temp": "98.4°F",
            "spo2": "97%",
            "nurse_name": "Nurse Amelia Foster",
        },
        {
            "id": 2,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "date": "2024-11-19",
            "time": "02:00 PM",
            "bp": "134/82",
            "hr": "72",
            "temp": "98.6°F",
            "spo2": "98%",
            "nurse_name": "Nurse Amelia Foster",
        },
        {
            "id": 3,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "date": "2024-11-19",
            "time": "09:00 AM",
            "bp": "142/90",
            "hr": "80",
            "temp": "98.2°F",
            "spo2": "96%",
            "nurse_name": "Nurse Amelia Foster",
        },
        {
            "id": 4,
            "patient_id": 3,
            "patient_name": "Ethan Brooks",
            "date": "2024-11-19",
            "time": "10:00 AM",
            "bp": "108/70",
            "hr": "88",
            "temp": "99.1°F",
            "spo2": "95%",
            "nurse_name": "Nurse Rachel Green",
        },
        {
            "id": 5,
            "patient_id": 4,
            "patient_name": "Sophia Carter",
            "date": "2024-11-19",
            "time": "11:00 AM",
            "bp": "120/78",
            "hr": "74",
            "temp": "98.6°F",
            "spo2": "98%",
            "nurse_name": "Nurse Omar Hassan",
        },
    ]

    nurse_tasks: list[NurseTask] = [
        {
            "id": 1,
            "nurse_id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "task": "Record morning vitals",
            "time": "08:00 AM",
            "status": "Completed",
            "priority": "High",
        },
        {
            "id": 2,
            "nurse_id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "task": "Administer Lisinopril 10mg",
            "time": "08:30 AM",
            "status": "Completed",
            "priority": "High",
        },
        {
            "id": 3,
            "nurse_id": 1,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "task": "Check IV drip",
            "time": "09:00 AM",
            "status": "Completed",
            "priority": "Medium",
        },
        {
            "id": 4,
            "nurse_id": 1,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "task": "Administer Metoprolol 25mg",
            "time": "10:00 AM",
            "status": "Pending",
            "priority": "High",
        },
        {
            "id": 5,
            "nurse_id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "task": "Afternoon vitals check",
            "time": "02:00 PM",
            "status": "Pending",
            "priority": "Medium",
        },
        {
            "id": 6,
            "nurse_id": 1,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "task": "Wound dressing change",
            "time": "03:00 PM",
            "status": "Pending",
            "priority": "High",
        },
        {
            "id": 7,
            "nurse_id": 2,
            "patient_id": 2,
            "patient_name": "Maria Gonzalez",
            "task": "Neurological assessment",
            "time": "10:30 AM",
            "status": "Completed",
            "priority": "Medium",
        },
        {
            "id": 8,
            "nurse_id": 3,
            "patient_id": 3,
            "patient_name": "Ethan Brooks",
            "task": "Nebulizer treatment",
            "time": "11:00 AM",
            "status": "Completed",
            "priority": "High",
        },
    ]

    med_schedule: list[MedSchedule] = [
        {
            "id": 1,
            "nurse_id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "medicine": "Lisinopril",
            "dosage": "10mg",
            "time": "08:30 AM",
            "status": "Administered",
        },
        {
            "id": 2,
            "nurse_id": 1,
            "patient_id": 1,
            "patient_name": "John Anderson",
            "medicine": "Atorvastatin",
            "dosage": "20mg",
            "time": "09:00 PM",
            "status": "Pending",
        },
        {
            "id": 3,
            "nurse_id": 1,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "medicine": "Metoprolol",
            "dosage": "25mg",
            "time": "10:00 AM",
            "status": "Pending",
        },
        {
            "id": 4,
            "nurse_id": 1,
            "patient_id": 5,
            "patient_name": "William Zhang",
            "medicine": "Metoprolol",
            "dosage": "25mg",
            "time": "10:00 PM",
            "status": "Pending",
        },
        {
            "id": 5,
            "nurse_id": 3,
            "patient_id": 3,
            "patient_name": "Ethan Brooks",
            "medicine": "Albuterol",
            "dosage": "2 puffs",
            "time": "12:00 PM",
            "status": "Pending",
        },
    ]

    clinical_notes: list[ClinicalNote] = [
        {
            "id": 1,
            "patient_id": 1,
            "author": "Dr. Sarah Rivera",
            "role": "Doctor",
            "note": "Patient responding well to medication. Continue current regimen and re-evaluate in 2 weeks.",
            "date": "2024-11-19",
        },
        {
            "id": 2,
            "patient_id": 1,
            "author": "Nurse Amelia Foster",
            "role": "Nurse",
            "note": "Patient reports mild headache. BP stable. Encouraged fluid intake.",
            "date": "2024-11-19",
        },
        {
            "id": 3,
            "patient_id": 5,
            "author": "Dr. Sarah Rivera",
            "role": "Doctor",
            "note": "ECG shows improvement. Consider discharge next week if trend continues.",
            "date": "2024-11-18",
        },
        {
            "id": 4,
            "patient_id": 3,
            "author": "Dr. Priya Patel",
            "role": "Doctor",
            "note": "Asthma well-controlled. Peak flow improved.",
            "date": "2024-11-18",
        },
    ]

    _next_appointment_id: int = 100
    _next_prescription_id: int = 100
    _next_note_id: int = 100
    _next_vital_id: int = 100
    _next_history_id: int = 100

    @rx.event
    def set_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def select_patient(self, patient_id: int):
        self.selected_patient_id = patient_id
        self.active_tab = "patient_detail"

    @rx.event
    def clear_selected_patient(self):
        self.selected_patient_id = 0

    @rx.event
    def set_filter(self, status: str):
        self.filter_status = status

    @rx.event
    def set_search(self, query: str):
        self.search_query = query

    @rx.var
    def current_patient(self) -> Patient:
        if self.patients:
            return self.patients[0]
        return {
            "id": 0,
            "name": "",
            "email": "",
            "age": 0,
            "gender": "",
            "blood_type": "",
            "phone": "",
            "disease": "",
            "admission_status": "",
            "admission_date": "",
            "room": "",
            "doctor_id": 0,
            "nurse_id": 0,
            "treatment_progress": 0,
        }

    @rx.var
    def current_doctor(self) -> Doctor:
        if self.doctors:
            return self.doctors[0]
        return {
            "id": 0,
            "name": "",
            "specialty": "",
            "email": "",
            "department": "",
            "status": "",
            "phone": "",
        }

    @rx.var
    def current_nurse(self) -> Nurse:
        if self.nurses:
            return self.nurses[0]
        return {
            "id": 0,
            "name": "",
            "department": "",
            "shift": "",
            "status": "",
            "email": "",
            "tasks_done": 0,
            "tasks_total": 0,
        }

    @rx.var
    def patient_appointments(self) -> list[Appointment]:
        pid = self.current_patient["id"]
        return [a for a in self.appointments if a["patient_id"] == pid]

    @rx.var
    def patient_prescriptions(self) -> list[Prescription]:
        pid = self.current_patient["id"]
        return [p for p in self.prescriptions if p["patient_id"] == pid]

    @rx.var
    def patient_history(self) -> list[HistoryEntry]:
        pid = self.current_patient["id"]
        return [h for h in self.medical_history if h["patient_id"] == pid]

    @rx.var
    def patient_assigned_doctor(self) -> Doctor:
        did = self.current_patient["doctor_id"]
        for d in self.doctors:
            if d["id"] == did:
                return d
        return {
            "id": 0,
            "name": "Unassigned",
            "specialty": "",
            "email": "",
            "department": "",
            "status": "",
            "phone": "",
        }

    @rx.var
    def doctor_patients(self) -> list[Patient]:
        did = self.current_doctor["id"]
        return [p for p in self.patients if p["doctor_id"] == did]

    @rx.var
    def doctor_admitted_patients(self) -> list[Patient]:
        return [
            p
            for p in self.doctor_patients
            if p["admission_status"] == "Admitted"
        ]

    @rx.var
    def doctor_today_appointments(self) -> list[Appointment]:
        did = self.current_doctor["id"]
        return [
            a
            for a in self.appointments
            if a["doctor_id"] == did and a["date"] == "2024-11-20"
        ]

    @rx.var
    def doctor_pending_appointments(self) -> list[Appointment]:
        did = self.current_doctor["id"]
        return [
            a
            for a in self.appointments
            if a["doctor_id"] == did and a["status"] == "Pending"
        ]

    @rx.var
    def doctor_all_appointments(self) -> list[Appointment]:
        did = self.current_doctor["id"]
        return [a for a in self.appointments if a["doctor_id"] == did]

    @rx.var
    def doctor_prescriptions(self) -> list[Prescription]:
        patient_ids = [p["id"] for p in self.doctor_patients]
        return [
            pr for pr in self.prescriptions if pr["patient_id"] in patient_ids
        ]

    @rx.var
    def doctor_notes(self) -> list[ClinicalNote]:
        patient_ids = [p["id"] for p in self.doctor_patients]
        return [
            n for n in self.clinical_notes if n["patient_id"] in patient_ids
        ]

    @rx.var
    def selected_patient(self) -> Patient:
        for p in self.patients:
            if p["id"] == self.selected_patient_id:
                return p
        return {
            "id": 0,
            "name": "",
            "email": "",
            "age": 0,
            "gender": "",
            "blood_type": "",
            "phone": "",
            "disease": "",
            "admission_status": "",
            "admission_date": "",
            "room": "",
            "doctor_id": 0,
            "nurse_id": 0,
            "treatment_progress": 0,
        }

    @rx.var
    def selected_patient_prescriptions(self) -> list[Prescription]:
        return [
            p
            for p in self.prescriptions
            if p["patient_id"] == self.selected_patient_id
        ]

    @rx.var
    def selected_patient_history(self) -> list[HistoryEntry]:
        return [
            h
            for h in self.medical_history
            if h["patient_id"] == self.selected_patient_id
        ]

    @rx.var
    def selected_patient_notes(self) -> list[ClinicalNote]:
        return [
            n
            for n in self.clinical_notes
            if n["patient_id"] == self.selected_patient_id
        ]

    @rx.var
    def selected_patient_vitals(self) -> list[Vital]:
        return [
            v
            for v in self.vitals
            if v["patient_id"] == self.selected_patient_id
        ]

    @rx.var
    def nurse_assigned_patients(self) -> list[Patient]:
        nid = self.current_nurse["id"]
        return [p for p in self.patients if p["nurse_id"] == nid]

    @rx.var
    def nurse_today_tasks(self) -> list[NurseTask]:
        nid = self.current_nurse["id"]
        return [t for t in self.nurse_tasks if t["nurse_id"] == nid]

    @rx.var
    def nurse_pending_tasks(self) -> list[NurseTask]:
        return [t for t in self.nurse_today_tasks if t["status"] == "Pending"]

    @rx.var
    def nurse_completed_tasks(self) -> list[NurseTask]:
        return [t for t in self.nurse_today_tasks if t["status"] == "Completed"]

    @rx.var
    def nurse_med_schedule(self) -> list[MedSchedule]:
        nid = self.current_nurse["id"]
        return [m for m in self.med_schedule if m["nurse_id"] == nid]

    @rx.var
    def nurse_upcoming_appointments(self) -> list[Appointment]:
        patient_ids = [p["id"] for p in self.nurse_assigned_patients]
        return [
            a
            for a in self.appointments
            if a["patient_id"] in patient_ids and a["status"] != "Completed"
        ]

    @rx.var
    def nurse_vitals_recorded(self) -> list[Vital]:
        nid = self.current_nurse["id"]
        nurse_name = ""
        for n in self.nurses:
            if n["id"] == nid:
                nurse_name = n["name"]
        return [v for v in self.vitals if v["nurse_name"] == nurse_name]

    @rx.event
    def book_appointment(self, form_data: dict):
        doctor_id = int(form_data.get("doctor_id", "1"))
        date = form_data.get("date", "")
        time = form_data.get("time", "")
        reason = form_data.get("reason", "").strip()
        if not date or not time or not reason:
            return rx.toast(
                "Please fill all appointment fields.", duration=3000
            )
        doctor_name = "Unknown"
        for d in self.doctors:
            if d["id"] == doctor_id:
                doctor_name = d["name"]
        patient = self.current_patient
        self._next_appointment_id += 1
        self.appointments.append(
            {
                "id": self._next_appointment_id,
                "patient_id": patient["id"],
                "patient_name": patient["name"],
                "doctor_id": doctor_id,
                "doctor_name": doctor_name,
                "date": date,
                "time": time,
                "reason": reason,
                "status": "Pending",
            }
        )
        return rx.toast(
            f"Appointment booked with {doctor_name}!", duration=3000
        )

    @rx.event
    def add_diagnosis(self, form_data: dict):
        patient_id = self.selected_patient_id
        diagnosis = form_data.get("diagnosis", "").strip()
        notes = form_data.get("notes", "").strip()
        if not diagnosis or patient_id == 0:
            return rx.toast("Please enter a diagnosis.", duration=3000)
        self._next_history_id += 1
        self.medical_history.append(
            {
                "id": self._next_history_id,
                "patient_id": patient_id,
                "date": "2024-11-20",
                "diagnosis": diagnosis,
                "doctor_name": self.current_doctor["name"],
                "notes": notes,
            }
        )
        return rx.toast("Diagnosis recorded!", duration=3000)

    @rx.event
    def prescribe_medicine(self, form_data: dict):
        patient_id = self.selected_patient_id
        medicine = form_data.get("medicine", "").strip()
        dosage = form_data.get("dosage", "").strip()
        frequency = form_data.get("frequency", "").strip()
        duration = form_data.get("duration", "").strip()
        notes = form_data.get("notes", "").strip()
        if not medicine or not dosage or patient_id == 0:
            return rx.toast("Please fill medicine and dosage.", duration=3000)
        patient_name = self.selected_patient["name"]
        self._next_prescription_id += 1
        self.prescriptions.append(
            {
                "id": self._next_prescription_id,
                "patient_id": patient_id,
                "patient_name": patient_name,
                "doctor_name": self.current_doctor["name"],
                "medicine": medicine,
                "dosage": dosage,
                "frequency": frequency or "As directed",
                "duration": duration or "As directed",
                "date": "2024-11-20",
                "notes": notes,
            }
        )
        return rx.toast(
            f"Prescribed {medicine} to {patient_name}", duration=3000
        )

    @rx.event
    def add_doctor_note(self, form_data: dict):
        patient_id = self.selected_patient_id
        note = form_data.get("note", "").strip()
        if not note or patient_id == 0:
            return rx.toast("Please write a note.", duration=3000)
        self._next_note_id += 1
        self.clinical_notes.append(
            {
                "id": self._next_note_id,
                "patient_id": patient_id,
                "author": self.current_doctor["name"],
                "role": "Doctor",
                "note": note,
                "date": "2024-11-20",
            }
        )
        return rx.toast("Medical note added!", duration=3000)

    @rx.event
    def add_nurse_note(self, form_data: dict):
        patient_id = self.selected_patient_id
        note = form_data.get("note", "").strip()
        if not note or patient_id == 0:
            return rx.toast("Please write a note.", duration=3000)
        self._next_note_id += 1
        self.clinical_notes.append(
            {
                "id": self._next_note_id,
                "patient_id": patient_id,
                "author": self.current_nurse["name"],
                "role": "Nurse",
                "note": note,
                "date": "2024-11-20",
            }
        )
        return rx.toast("Nursing note added!", duration=3000)

    @rx.event
    def complete_appointment(self, appt_id: int):
        for i, a in enumerate(self.appointments):
            if a["id"] == appt_id:
                self.appointments[i] = {**a, "status": "Completed"}
                return rx.toast(
                    "Appointment marked as completed.", duration=2000
                )

    @rx.event
    def confirm_appointment(self, appt_id: int):
        for i, a in enumerate(self.appointments):
            if a["id"] == appt_id:
                self.appointments[i] = {**a, "status": "Confirmed"}
                return rx.toast("Appointment confirmed.", duration=2000)

    @rx.event
    def update_patient_status(self, patient_id: int, status: str):
        for i, p in enumerate(self.patients):
            if p["id"] == patient_id:
                self.patients[i] = {**p, "admission_status": status}
                return rx.toast(f"Status updated to {status}.", duration=2000)

    @rx.event
    def update_treatment_progress(self, patient_id: int, delta: int):
        for i, p in enumerate(self.patients):
            if p["id"] == patient_id:
                new_val = max(0, min(100, p["treatment_progress"] + delta))
                self.patients[i] = {**p, "treatment_progress": new_val}
                return rx.toast(
                    f"Progress updated to {new_val}%.", duration=2000
                )

    @rx.event
    def assign_nurse(self, form_data: dict):
        patient_id = self.selected_patient_id
        nurse_id = int(form_data.get("nurse_id", "0"))
        if patient_id == 0 or nurse_id == 0:
            return rx.toast("Select a nurse.", duration=3000)
        nurse_name = ""
        for n in self.nurses:
            if n["id"] == nurse_id:
                nurse_name = n["name"]
        for i, p in enumerate(self.patients):
            if p["id"] == patient_id:
                self.patients[i] = {**p, "nurse_id": nurse_id}
                return rx.toast(
                    f"{nurse_name} assigned to patient.", duration=3000
                )

    @rx.event
    def record_vital(self, form_data: dict):
        patient_id = int(form_data.get("patient_id", "0"))
        bp = form_data.get("bp", "").strip()
        hr = form_data.get("hr", "").strip()
        temp = form_data.get("temp", "").strip()
        spo2 = form_data.get("spo2", "").strip()
        if patient_id == 0 or not bp or not hr:
            return rx.toast("Please fill patient, BP and HR.", duration=3000)
        patient_name = ""
        for p in self.patients:
            if p["id"] == patient_id:
                patient_name = p["name"]
        self._next_vital_id += 1
        self.vitals.append(
            {
                "id": self._next_vital_id,
                "patient_id": patient_id,
                "patient_name": patient_name,
                "date": "2024-11-20",
                "time": "Now",
                "bp": bp,
                "hr": hr,
                "temp": temp or "N/A",
                "spo2": spo2 or "N/A",
                "nurse_name": self.current_nurse["name"],
            }
        )
        return rx.toast(f"Vitals recorded for {patient_name}.", duration=3000)

    @rx.event
    def administer_medicine(self, med_id: int):
        for i, m in enumerate(self.med_schedule):
            if m["id"] == med_id:
                self.med_schedule[i] = {**m, "status": "Administered"}
                return rx.toast(f"{m['medicine']} administered.", duration=2000)

    @rx.event
    def complete_task(self, task_id: int):
        for i, t in enumerate(self.nurse_tasks):
            if t["id"] == task_id:
                self.nurse_tasks[i] = {**t, "status": "Completed"}
                return rx.toast("Task completed!", duration=2000)
