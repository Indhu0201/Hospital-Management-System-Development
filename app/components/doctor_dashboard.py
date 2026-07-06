import reflex as rx
from app.states.healthcare_state import (
    HealthcareState,
    Patient,
    Appointment,
    Nurse,
    Prescription,
    ClinicalNote,
    HistoryEntry,
)
from app.components.dashboard_ui import (
    stat_card,
    status_badge,
    tab_bar,
    welcome_banner,
    empty_state,
    section_card,
    form_input,
    form_textarea,
)


def welcome_message() -> rx.Component:
    return welcome_banner(
        HealthcareState.current_doctor["name"],
        "doctor",
        f"You have {HealthcareState.doctor_today_appointments.length()} appointments today.",
    )


def patient_card(p: Patient) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.icon("user", class_name="h-5 w-5 text-white"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-sm shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    p["name"],
                    class_name="text-sm font-bold text-gray-900 text-left",
                ),
                rx.el.p(
                    f"{p['age']}y • {p['gender']} • {p['blood_type']}",
                    class_name="text-xs text-gray-500 text-left",
                ),
            ),
            class_name="flex items-center gap-3 mb-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Condition",
                    class_name="text-[10px] font-semibold text-gray-400 uppercase",
                ),
                rx.el.p(
                    p["disease"],
                    class_name="text-xs font-semibold text-gray-900",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "Room",
                    class_name="text-[10px] font-semibold text-gray-400 uppercase",
                ),
                rx.el.p(
                    p["room"], class_name="text-xs font-semibold text-gray-900"
                ),
            ),
            class_name="grid grid-cols-2 gap-3 mb-3 text-left",
        ),
        rx.el.div(
            status_badge(p["admission_status"]),
            rx.el.div(
                rx.el.p(
                    f"{p['treatment_progress']}%",
                    class_name="text-xs font-bold text-blue-600",
                ),
                class_name="ml-auto",
            ),
            class_name="flex items-center gap-2",
        ),
        on_click=lambda: HealthcareState.select_patient(p["id"]),
        class_name="w-full text-left bg-white/80 backdrop-blur-sm p-4 rounded-2xl border border-white/60 shadow-sm hover:shadow-md hover:border-blue-300 transition-all cursor-pointer",
    )


def appointment_action_row(a: Appointment) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    a["time"], class_name="text-xs font-bold text-blue-600"
                ),
                rx.el.p(a["date"], class_name="text-[10px] text-gray-500"),
                class_name="w-16 shrink-0 text-center py-2 bg-blue-50 rounded-lg",
            ),
            rx.el.div(
                rx.el.p(
                    a["patient_name"],
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.p(a["reason"], class_name="text-xs text-gray-500 mt-0.5"),
                rx.el.div(status_badge(a["status"]), class_name="mt-1"),
            ),
            class_name="flex items-center gap-3 flex-1 min-w-0",
        ),
        rx.el.div(
            rx.cond(
                a["status"] == "Pending",
                rx.el.button(
                    rx.icon("check", class_name="h-3.5 w-3.5"),
                    "Confirm",
                    on_click=lambda: HealthcareState.confirm_appointment(
                        a["id"]
                    ),
                    class_name="flex items-center gap-1 px-3 py-1.5 bg-blue-600 text-white text-xs font-semibold rounded-lg hover:bg-blue-700 transition-all",
                ),
                rx.el.div(),
            ),
            rx.cond(
                a["status"] != "Completed",
                rx.el.button(
                    rx.icon("check-check", class_name="h-3.5 w-3.5"),
                    "Complete",
                    on_click=lambda: HealthcareState.complete_appointment(
                        a["id"]
                    ),
                    class_name="flex items-center gap-1 px-3 py-1.5 bg-emerald-600 text-white text-xs font-semibold rounded-lg hover:bg-emerald-700 transition-all",
                ),
                rx.el.div(),
            ),
            class_name="flex items-center gap-2",
        ),
        class_name="flex items-center justify-between gap-3 p-3 bg-white/80 rounded-xl border border-white/60 hover:shadow-sm transition-all",
    )


def nurse_card(n: Nurse) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("heart-pulse", class_name="h-5 w-5 text-rose-600"),
                class_name="w-11 h-11 rounded-xl bg-rose-100 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    n["name"], class_name="text-sm font-bold text-gray-900"
                ),
                rx.el.p(
                    f"{n['department']} • {n['shift']} shift",
                    class_name="text-xs text-gray-500",
                ),
            ),
            class_name="flex items-center gap-3 mb-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Tasks Progress",
                        class_name="text-[10px] font-semibold text-gray-500",
                    ),
                    rx.el.p(
                        f"{n['tasks_done']}/{n['tasks_total']}",
                        class_name="text-xs font-bold text-gray-900",
                    ),
                    class_name="flex items-center justify-between mb-1",
                ),
                rx.el.div(
                    rx.el.div(
                        class_name="h-full bg-emerald-500 rounded-full",
                        style={
                            "width": (
                                n["tasks_done"] * 100 / n["tasks_total"]
                            ).to_string()
                            + "%"
                        },
                    ),
                    class_name="h-1.5 bg-gray-100 rounded-full overflow-hidden",
                ),
            ),
            class_name="mb-3",
        ),
        status_badge(n["status"]),
        class_name="bg-white/80 backdrop-blur-sm p-4 rounded-2xl border border-white/60 shadow-sm hover:shadow-md transition-all",
    )


def overview_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            stat_card(
                "Total Patients",
                HealthcareState.doctor_patients.length().to_string(),
                "users",
                "blue",
            ),
            stat_card(
                "Today's Appointments",
                HealthcareState.doctor_today_appointments.length().to_string(),
                "calendar",
                "emerald",
            ),
            stat_card(
                "Total Nurses",
                HealthcareState.nurses.length().to_string(),
                "heart-pulse",
                "rose",
            ),
            stat_card(
                "Admitted Patients",
                HealthcareState.doctor_admitted_patients.length().to_string(),
                "bed",
                "purple",
            ),
            stat_card(
                "Pending Appointments",
                HealthcareState.doctor_pending_appointments.length().to_string(),
                "clock",
                "amber",
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Today's Schedule",
                    class_name="text-base font-bold text-gray-900 mb-3",
                ),
                rx.cond(
                    HealthcareState.doctor_today_appointments.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.doctor_today_appointments,
                            appointment_action_row,
                        ),
                        class_name="space-y-2",
                    ),
                    empty_state(
                        "calendar-x",
                        "No appointments today",
                        "Enjoy your free schedule.",
                    ),
                ),
            ),
            rx.el.div(
                rx.el.h3(
                    "Recent Patients",
                    class_name="text-base font-bold text-gray-900 mb-3",
                ),
                rx.el.div(
                    rx.foreach(HealthcareState.doctor_patients, patient_card),
                    class_name="grid grid-cols-1 gap-3",
                ),
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
    )


def patients_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "My Patients", class_name="text-base font-bold text-gray-900"
            ),
            rx.el.p(
                f"{HealthcareState.doctor_patients.length()} patients under your care",
                class_name="text-xs text-gray-500",
            ),
            class_name="mb-4",
        ),
        rx.cond(
            HealthcareState.doctor_patients.length() > 0,
            rx.el.div(
                rx.foreach(HealthcareState.doctor_patients, patient_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
            ),
            empty_state(
                "users",
                "No assigned patients",
                "Patients will appear here when assigned.",
            ),
        ),
    )


def appointments_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "All Appointments",
            class_name="text-base font-bold text-gray-900 mb-3",
        ),
        rx.cond(
            HealthcareState.doctor_all_appointments.length() > 0,
            rx.el.div(
                rx.foreach(
                    HealthcareState.doctor_all_appointments,
                    appointment_action_row,
                ),
                class_name="space-y-2",
            ),
            empty_state(
                "calendar", "No appointments", "Your schedule is clear."
            ),
        ),
    )


def nurses_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Nursing Staff", class_name="text-base font-bold text-gray-900 mb-3"
        ),
        rx.el.div(
            rx.foreach(HealthcareState.nurses, nurse_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4",
        ),
    )


def diagnosis_form() -> rx.Component:
    return rx.el.form(
        form_input("Diagnosis", "diagnosis", "e.g., Hypertension Stage 2"),
        form_textarea("Clinical Notes", "notes", "Detailed diagnosis notes..."),
        rx.el.button(
            rx.icon("clipboard-check", class_name="h-4 w-4"),
            "Save Diagnosis",
            type="submit",
            class_name="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 mt-3",
        ),
        on_submit=HealthcareState.add_diagnosis,
        reset_on_submit=True,
        class_name="space-y-3",
    )


def prescription_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            form_input("Medicine", "medicine", "e.g., Amoxicillin"),
            form_input("Dosage", "dosage", "e.g., 500mg"),
            class_name="grid grid-cols-2 gap-3",
        ),
        rx.el.div(
            form_input(
                "Frequency", "frequency", "e.g., Twice daily", required=False
            ),
            form_input("Duration", "duration", "e.g., 7 days", required=False),
            class_name="grid grid-cols-2 gap-3",
        ),
        form_textarea(
            "Instructions", "notes", "Additional instructions...", False
        ),
        rx.el.button(
            rx.icon("pill", class_name="h-4 w-4"),
            "Prescribe",
            type="submit",
            class_name="flex items-center gap-2 px-4 py-2 bg-purple-600 text-white text-sm font-semibold rounded-xl hover:bg-purple-700 mt-3",
        ),
        on_submit=HealthcareState.prescribe_medicine,
        reset_on_submit=True,
        class_name="space-y-3",
    )


def note_form() -> rx.Component:
    return rx.el.form(
        form_textarea("Medical Note", "note", "Write clinical observations..."),
        rx.el.button(
            rx.icon("pen-line", class_name="h-4 w-4"),
            "Add Note",
            type="submit",
            class_name="flex items-center gap-2 px-4 py-2 bg-emerald-600 text-white text-sm font-semibold rounded-xl hover:bg-emerald-700 mt-3",
        ),
        on_submit=HealthcareState.add_doctor_note,
        reset_on_submit=True,
        class_name="space-y-3",
    )


def assign_nurse_form() -> rx.Component:
    return rx.el.form(
        rx.el.label(
            "Select Nurse",
            class_name="block text-xs font-semibold text-gray-700 mb-1.5",
        ),
        rx.el.div(
            rx.el.select(
                rx.foreach(
                    HealthcareState.nurses,
                    lambda n: rx.el.option(
                        f"{n['name']} - {n['department']}",
                        value=n["id"].to_string(),
                    ),
                ),
                name="nurse_id",
                class_name="w-full px-3 py-2 pr-8 bg-white border border-gray-200 rounded-xl text-sm text-gray-900 appearance-none cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-blue-500",
            ),
            rx.icon(
                "chevron-down",
                class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
            ),
            class_name="relative",
        ),
        rx.el.button(
            rx.icon("user-plus", class_name="h-4 w-4"),
            "Assign Nurse",
            type="submit",
            class_name="flex items-center gap-2 px-4 py-2 bg-rose-600 text-white text-sm font-semibold rounded-xl hover:bg-rose-700 mt-3",
        ),
        on_submit=HealthcareState.assign_nurse,
        class_name="space-y-2",
    )


def status_actions() -> rx.Component:
    p = HealthcareState.selected_patient
    return rx.el.div(
        rx.el.button(
            "Mark Admitted",
            on_click=lambda: HealthcareState.update_patient_status(
                p["id"], "Admitted"
            ),
            class_name="px-3 py-1.5 bg-blue-100 text-blue-700 text-xs font-semibold rounded-lg hover:bg-blue-200 transition-all",
        ),
        rx.el.button(
            "Mark Outpatient",
            on_click=lambda: HealthcareState.update_patient_status(
                p["id"], "Outpatient"
            ),
            class_name="px-3 py-1.5 bg-purple-100 text-purple-700 text-xs font-semibold rounded-lg hover:bg-purple-200 transition-all",
        ),
        rx.el.button(
            "Discharge",
            on_click=lambda: HealthcareState.update_patient_status(
                p["id"], "Discharged"
            ),
            class_name="px-3 py-1.5 bg-gray-100 text-gray-700 text-xs font-semibold rounded-lg hover:bg-gray-200 transition-all",
        ),
        rx.el.button(
            rx.icon("plus", class_name="h-3 w-3"),
            "10%",
            on_click=lambda: HealthcareState.update_treatment_progress(
                p["id"], 10
            ),
            class_name="flex items-center gap-1 px-3 py-1.5 bg-emerald-100 text-emerald-700 text-xs font-semibold rounded-lg hover:bg-emerald-200 transition-all",
        ),
        rx.el.button(
            rx.icon("minus", class_name="h-3 w-3"),
            "10%",
            on_click=lambda: HealthcareState.update_treatment_progress(
                p["id"], -10
            ),
            class_name="flex items-center gap-1 px-3 py-1.5 bg-amber-100 text-amber-700 text-xs font-semibold rounded-lg hover:bg-amber-200 transition-all",
        ),
        class_name="flex items-center gap-2 flex-wrap",
    )


def rx_prescription_row(p: Prescription) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("pill", class_name="h-4 w-4 text-purple-600"),
            class_name="w-8 h-8 rounded-lg bg-purple-100 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(
                f"{p['medicine']} - {p['dosage']}",
                class_name="text-sm font-semibold text-gray-900",
            ),
            rx.el.p(
                f"{p['frequency']} • {p['duration']}",
                class_name="text-xs text-gray-500",
            ),
        ),
        class_name="flex items-center gap-3 p-2.5 bg-gray-50/60 rounded-xl",
    )


def rx_history_row(h: HistoryEntry) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            h["diagnosis"], class_name="text-sm font-semibold text-gray-900"
        ),
        rx.el.p(h["notes"], class_name="text-xs text-gray-600 mt-1"),
        rx.el.p(
            f"{h['doctor_name']} • {h['date']}",
            class_name="text-xs text-gray-400 mt-1",
        ),
        class_name="p-3 bg-gray-50/60 rounded-xl",
    )


def rx_note_row(n: ClinicalNote) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                n["role"],
                class_name=rx.cond(
                    n["role"] == "Doctor",
                    "text-[10px] font-bold px-2 py-0.5 rounded-md bg-blue-100 text-blue-700 w-fit",
                    "text-[10px] font-bold px-2 py-0.5 rounded-md bg-rose-100 text-rose-700 w-fit",
                ),
            ),
            rx.el.p(n["date"], class_name="text-[10px] text-gray-400 ml-auto"),
            class_name="flex items-center gap-2 mb-1",
        ),
        rx.el.p(n["note"], class_name="text-sm text-gray-800"),
        rx.el.p(f"— {n['author']}", class_name="text-xs text-gray-500 mt-1"),
        class_name="p-3 bg-gray-50/60 rounded-xl",
    )


def patient_detail_tab() -> rx.Component:
    p = HealthcareState.selected_patient
    return rx.el.div(
        rx.el.button(
            rx.icon("arrow-left", class_name="h-4 w-4"),
            "Back to Overview",
            on_click=[
                HealthcareState.clear_selected_patient,
                lambda: HealthcareState.set_tab("overview"),
            ],
            class_name="flex items-center gap-2 px-3 py-1.5 bg-white text-gray-700 text-xs font-semibold rounded-lg border border-gray-200 hover:border-blue-300 mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="h-6 w-6 text-white"),
                    class_name="w-14 h-14 rounded-2xl bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-md",
                ),
                rx.el.div(
                    rx.el.h3(
                        p["name"], class_name="text-lg font-bold text-gray-900"
                    ),
                    rx.el.p(
                        f"{p['age']}y • {p['gender']} • {p['blood_type']} • Room {p['room']}",
                        class_name="text-xs text-gray-500",
                    ),
                    rx.el.div(
                        status_badge(p["admission_status"]),
                        rx.el.span(
                            f"Admitted: {p['admission_date']}",
                            class_name="text-xs text-gray-500 ml-2",
                        ),
                        class_name="flex items-center mt-1",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Condition / Disease",
                        class_name="text-[10px] font-semibold text-gray-500 uppercase",
                    ),
                    rx.el.p(
                        p["disease"],
                        class_name="text-sm font-bold text-gray-900",
                    ),
                ),
                rx.el.div(
                    rx.el.p(
                        "Treatment Progress",
                        class_name="text-[10px] font-semibold text-gray-500 uppercase",
                    ),
                    rx.el.p(
                        f"{p['treatment_progress']}%",
                        class_name="text-sm font-bold text-blue-600",
                    ),
                ),
                class_name="grid grid-cols-2 gap-4 mt-4 pt-4 border-t border-gray-100",
            ),
            rx.el.div(
                rx.el.p(
                    "Update Status",
                    class_name="text-xs font-semibold text-gray-700 mb-2",
                ),
                status_actions(),
                class_name="mt-4 pt-4 border-t border-gray-100",
            ),
            class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm mb-4",
        ),
        rx.el.div(
            section_card(
                "Add Diagnosis", "Record a new diagnosis", diagnosis_form()
            ),
            section_card(
                "Prescribe Medicine",
                "Add a new prescription",
                prescription_form(),
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        rx.el.div(
            section_card(
                "Medical Note", "Add clinical observations", note_form()
            ),
            section_card(
                "Assign Nurse", "Delegate patient care", assign_nurse_form()
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h4(
                    "Prescriptions",
                    class_name="text-sm font-bold text-gray-900 mb-2",
                ),
                rx.cond(
                    HealthcareState.selected_patient_prescriptions.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.selected_patient_prescriptions,
                            rx_prescription_row,
                        ),
                        class_name="space-y-2",
                    ),
                    rx.el.p(
                        "No prescriptions yet.",
                        class_name="text-xs text-gray-500 italic",
                    ),
                ),
                class_name="bg-white/80 p-4 rounded-2xl border border-white/60",
            ),
            rx.el.div(
                rx.el.h4(
                    "Medical History",
                    class_name="text-sm font-bold text-gray-900 mb-2",
                ),
                rx.cond(
                    HealthcareState.selected_patient_history.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.selected_patient_history,
                            rx_history_row,
                        ),
                        class_name="space-y-2",
                    ),
                    rx.el.p(
                        "No history recorded.",
                        class_name="text-xs text-gray-500 italic",
                    ),
                ),
                class_name="bg-white/80 p-4 rounded-2xl border border-white/60",
            ),
            rx.el.div(
                rx.el.h4(
                    "Clinical Notes",
                    class_name="text-sm font-bold text-gray-900 mb-2",
                ),
                rx.cond(
                    HealthcareState.selected_patient_notes.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.selected_patient_notes, rx_note_row
                        ),
                        class_name="space-y-2",
                    ),
                    rx.el.p(
                        "No notes yet.",
                        class_name="text-xs text-gray-500 italic",
                    ),
                ),
                class_name="bg-white/80 p-4 rounded-2xl border border-white/60",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4",
        ),
    )


def doctor_dashboard_content() -> rx.Component:
    return rx.el.div(
        welcome_message(),
        tab_bar(
            [
                ("Overview", "overview", "layout-dashboard"),
                ("My Patients", "patients", "users"),
                ("Appointments", "appointments", "calendar"),
                ("Nurses", "nurses", "heart-pulse"),
            ]
        ),
        rx.match(
            HealthcareState.active_tab,
            ("patients", patients_tab()),
            ("appointments", appointments_tab()),
            ("nurses", nurses_tab()),
            ("patient_detail", patient_detail_tab()),
            overview_tab(),
        ),
        class_name="max-w-7xl mx-auto",
    )
