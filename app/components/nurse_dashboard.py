import reflex as rx
from app.states.healthcare_state import (
    HealthcareState,
    Patient,
    NurseTask,
    MedSchedule,
    Vital,
    Appointment,
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


def nurse_patient_card(p: Patient) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.icon("user", class_name="h-5 w-5 text-white"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-rose-500 to-rose-700 flex items-center justify-center shadow-sm shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    p["name"],
                    class_name="text-sm font-bold text-gray-900 text-left",
                ),
                rx.el.p(
                    f"Room {p['room']} • {p['disease']}",
                    class_name="text-xs text-gray-500 text-left",
                ),
            ),
            class_name="flex items-center gap-3 mb-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Progress",
                    class_name="text-[10px] font-semibold text-gray-500",
                ),
                rx.el.p(
                    f"{p['treatment_progress']}%",
                    class_name="text-xs font-bold text-blue-600",
                ),
                class_name="flex items-center justify-between mb-1",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-blue-500 rounded-full",
                    style={"width": p["treatment_progress"].to_string() + "%"},
                ),
                class_name="h-1.5 bg-gray-100 rounded-full overflow-hidden",
            ),
            class_name="mb-3",
        ),
        rx.el.div(
            status_badge(p["admission_status"]),
            rx.el.button(
                rx.icon("plus", class_name="h-3 w-3"),
                "5%",
                on_click=lambda: HealthcareState.update_treatment_progress(
                    p["id"], 5
                ),
                class_name="ml-auto flex items-center gap-1 px-2 py-1 bg-emerald-100 text-emerald-700 text-[10px] font-semibold rounded-md hover:bg-emerald-200 transition-all",
            ),
            class_name="flex items-center gap-2",
        ),
        on_click=lambda: HealthcareState.select_patient(p["id"]),
        class_name="w-full text-left bg-white/80 backdrop-blur-sm p-4 rounded-2xl border border-white/60 shadow-sm hover:shadow-md hover:border-rose-300 transition-all cursor-pointer",
    )


def task_row(t: NurseTask) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    rx.cond(
                        t["status"] == "Completed", "check-circle-2", "circle"
                    ),
                    class_name=rx.cond(
                        t["status"] == "Completed",
                        "h-5 w-5 text-emerald-500",
                        "h-5 w-5 text-gray-400",
                    ),
                ),
                class_name="shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    t["task"],
                    class_name=rx.cond(
                        t["status"] == "Completed",
                        "text-sm font-semibold text-gray-500 line-through",
                        "text-sm font-semibold text-gray-900",
                    ),
                ),
                rx.el.p(
                    f"{t['patient_name']} • {t['time']}",
                    class_name="text-xs text-gray-500 mt-0.5",
                ),
            ),
            class_name="flex items-center gap-3 flex-1 min-w-0",
        ),
        rx.el.div(
            status_badge(t["priority"]),
            rx.cond(
                t["status"] == "Pending",
                rx.el.button(
                    rx.icon("check", class_name="h-3.5 w-3.5"),
                    "Done",
                    on_click=lambda: HealthcareState.complete_task(t["id"]),
                    class_name="flex items-center gap-1 px-3 py-1.5 bg-emerald-600 text-white text-xs font-semibold rounded-lg hover:bg-emerald-700 transition-all",
                ),
                status_badge(t["status"]),
            ),
            class_name="flex items-center gap-2",
        ),
        class_name="flex items-center justify-between gap-3 p-3 bg-white/80 rounded-xl border border-white/60 hover:shadow-sm transition-all",
    )


def med_row(m: MedSchedule) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("pill", class_name="h-4 w-4 text-purple-600"),
                class_name="w-9 h-9 rounded-lg bg-purple-100 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    f"{m['medicine']} - {m['dosage']}",
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.p(
                    f"{m['patient_name']} • {m['time']}",
                    class_name="text-xs text-gray-500 mt-0.5",
                ),
            ),
            class_name="flex items-center gap-3 flex-1 min-w-0",
        ),
        rx.cond(
            m["status"] == "Pending",
            rx.el.button(
                rx.icon("syringe", class_name="h-3.5 w-3.5"),
                "Administer",
                on_click=lambda: HealthcareState.administer_medicine(m["id"]),
                class_name="flex items-center gap-1 px-3 py-1.5 bg-purple-600 text-white text-xs font-semibold rounded-lg hover:bg-purple-700 transition-all",
            ),
            status_badge(m["status"]),
        ),
        class_name="flex items-center justify-between gap-3 p-3 bg-white/80 rounded-xl border border-white/60 hover:shadow-sm transition-all",
    )


def vital_row(v: Vital) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                v["patient_name"], class_name="text-sm font-bold text-gray-900"
            ),
            rx.el.p(
                f"{v['date']} • {v['time']}", class_name="text-xs text-gray-500"
            ),
            class_name="mb-3",
        ),
        rx.el.div(
            vital_stat("BP", v["bp"], "activity", "rose"),
            vital_stat("HR", v["hr"], "heart", "red"),
            vital_stat("Temp", v["temp"], "thermometer", "amber"),
            vital_stat("SpO2", v["spo2"], "wind", "blue"),
            class_name="grid grid-cols-4 gap-2",
        ),
        class_name="p-4 bg-white/80 rounded-2xl border border-white/60 shadow-sm",
    )


def vital_stat(label: str, value, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-3 w-3 text-{color}-600"),
            rx.el.p(
                label, class_name="text-[10px] font-semibold text-gray-500"
            ),
            class_name="flex items-center gap-1 mb-1",
        ),
        rx.el.p(value, class_name="text-sm font-bold text-gray-900"),
        class_name="p-2 bg-gray-50/60 rounded-lg",
    )


def upcoming_appt_row(a: Appointment) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(a["time"], class_name="text-xs font-bold text-blue-600"),
            rx.el.p(a["date"], class_name="text-[10px] text-gray-500"),
            class_name="w-16 shrink-0 text-center py-2 bg-blue-50 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(
                a["patient_name"],
                class_name="text-sm font-semibold text-gray-900",
            ),
            rx.el.p(
                f"{a['reason']} • {a['doctor_name']}",
                class_name="text-xs text-gray-500 mt-0.5",
            ),
        ),
        status_badge(a["status"]),
        class_name="flex items-center gap-3 p-3 bg-white/80 rounded-xl border border-white/60",
    )


def overview_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            stat_card(
                "Assigned Patients",
                HealthcareState.nurse_assigned_patients.length().to_string(),
                "users",
                "blue",
            ),
            stat_card(
                "Today's Tasks",
                HealthcareState.nurse_today_tasks.length().to_string(),
                "list-checks",
                "emerald",
            ),
            stat_card(
                "Medicine Schedule",
                HealthcareState.nurse_med_schedule.length().to_string(),
                "pill",
                "purple",
            ),
            stat_card(
                "Upcoming Appointments",
                HealthcareState.nurse_upcoming_appointments.length().to_string(),
                "calendar",
                "amber",
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "My Patients",
                    class_name="text-base font-bold text-gray-900 mb-3",
                ),
                rx.cond(
                    HealthcareState.nurse_assigned_patients.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.nurse_assigned_patients,
                            nurse_patient_card,
                        ),
                        class_name="grid grid-cols-1 gap-3",
                    ),
                    empty_state(
                        "users",
                        "No assigned patients",
                        "You have no patients assigned yet.",
                    ),
                ),
            ),
            rx.el.div(
                rx.el.h3(
                    "Pending Tasks",
                    class_name="text-base font-bold text-gray-900 mb-3",
                ),
                rx.cond(
                    HealthcareState.nurse_pending_tasks.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.nurse_pending_tasks, task_row
                        ),
                        class_name="space-y-2",
                    ),
                    empty_state(
                        "check-check",
                        "All caught up!",
                        "No pending tasks right now.",
                    ),
                ),
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
    )


def tasks_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Today's Tasks", class_name="text-base font-bold text-gray-900"
            ),
            rx.el.p(
                f"{HealthcareState.nurse_completed_tasks.length()} of {HealthcareState.nurse_today_tasks.length()} completed",
                class_name="text-xs text-gray-500",
            ),
            class_name="mb-4",
        ),
        rx.cond(
            HealthcareState.nurse_today_tasks.length() > 0,
            rx.el.div(
                rx.foreach(HealthcareState.nurse_today_tasks, task_row),
                class_name="space-y-2",
            ),
            empty_state("list-checks", "No tasks", "Your task list is empty."),
        ),
    )


def medicine_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Medicine Schedule",
            class_name="text-base font-bold text-gray-900 mb-3",
        ),
        rx.cond(
            HealthcareState.nurse_med_schedule.length() > 0,
            rx.el.div(
                rx.foreach(HealthcareState.nurse_med_schedule, med_row),
                class_name="space-y-2",
            ),
            empty_state(
                "pill",
                "No scheduled medicines",
                "The medicine schedule is empty.",
            ),
        ),
    )


def vitals_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label(
                "Patient",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("Select patient", value="0"),
                    rx.foreach(
                        HealthcareState.nurse_assigned_patients,
                        lambda p: rx.el.option(
                            p["name"], value=p["id"].to_string()
                        ),
                    ),
                    name="patient_id",
                    class_name="w-full px-3 py-2 pr-8 bg-white border border-gray-200 rounded-xl text-sm text-gray-900 appearance-none cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-blue-500",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                ),
                class_name="relative",
            ),
        ),
        rx.el.div(
            form_input("Blood Pressure", "bp", "e.g., 120/80"),
            form_input("Heart Rate", "hr", "e.g., 72"),
            class_name="grid grid-cols-2 gap-3",
        ),
        rx.el.div(
            form_input("Temperature", "temp", "e.g., 98.6°F", required=False),
            form_input("SpO2", "spo2", "e.g., 98%", required=False),
            class_name="grid grid-cols-2 gap-3",
        ),
        rx.el.button(
            rx.icon("activity", class_name="h-4 w-4"),
            "Record Vitals",
            type="submit",
            class_name="flex items-center gap-2 px-5 py-2.5 bg-rose-600 text-white text-sm font-semibold rounded-xl hover:bg-rose-700 transition-all",
        ),
        on_submit=HealthcareState.record_vital,
        reset_on_submit=True,
        class_name="space-y-3",
    )


def vitals_tab() -> rx.Component:
    return rx.el.div(
        section_card(
            "Record New Vitals", "Enter patient vital signs", vitals_form()
        ),
        rx.el.div(
            rx.el.h3(
                "Recorded Vitals",
                class_name="text-base font-bold text-gray-900 mb-3 mt-6",
            ),
            rx.cond(
                HealthcareState.nurse_vitals_recorded.length() > 0,
                rx.el.div(
                    rx.foreach(
                        HealthcareState.nurse_vitals_recorded, vital_row
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-3",
                ),
                empty_state(
                    "activity",
                    "No vitals recorded",
                    "Record patient vitals using the form above.",
                ),
            ),
        ),
    )


def appointments_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Upcoming Appointments",
            class_name="text-base font-bold text-gray-900 mb-3",
        ),
        rx.cond(
            HealthcareState.nurse_upcoming_appointments.length() > 0,
            rx.el.div(
                rx.foreach(
                    HealthcareState.nurse_upcoming_appointments,
                    upcoming_appt_row,
                ),
                class_name="space-y-2",
            ),
            empty_state(
                "calendar",
                "No upcoming appointments",
                "Your patients have no scheduled appointments.",
            ),
        ),
    )


def nurse_note_form() -> rx.Component:
    return rx.el.form(
        form_textarea(
            "Nursing Note", "note", "Document care progress and observations..."
        ),
        rx.el.button(
            rx.icon("pen-line", class_name="h-4 w-4"),
            "Add Note",
            type="submit",
            class_name="flex items-center gap-2 px-4 py-2 bg-emerald-600 text-white text-sm font-semibold rounded-xl hover:bg-emerald-700 mt-3",
        ),
        on_submit=HealthcareState.add_nurse_note,
        reset_on_submit=True,
        class_name="space-y-3",
    )


def n_prescription_row(p) -> rx.Component:
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
                f"{p['frequency']} • Prescribed by {p['doctor_name']}",
                class_name="text-xs text-gray-500",
            ),
        ),
        class_name="flex items-center gap-3 p-2.5 bg-gray-50/60 rounded-xl",
    )


def n_note_row(n) -> rx.Component:
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


def n_vital_row(v: Vital) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                f"{v['date']} • {v['time']}",
                class_name="text-xs text-gray-500 mb-2",
            ),
            class_name="",
        ),
        rx.el.div(
            vital_stat("BP", v["bp"], "activity", "rose"),
            vital_stat("HR", v["hr"], "heart", "red"),
            vital_stat("Temp", v["temp"], "thermometer", "amber"),
            vital_stat("SpO2", v["spo2"], "wind", "blue"),
            class_name="grid grid-cols-4 gap-2",
        ),
        class_name="p-3 bg-gray-50/60 rounded-xl",
    )


def patient_detail_tab() -> rx.Component:
    p = HealthcareState.selected_patient
    return rx.el.div(
        rx.el.button(
            rx.icon("arrow-left", class_name="h-4 w-4"),
            "Back",
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
                    class_name="w-14 h-14 rounded-2xl bg-gradient-to-br from-rose-500 to-rose-700 flex items-center justify-center shadow-md",
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
                        status_badge(p["admission_status"]), class_name="mt-1"
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Condition",
                        class_name="text-[10px] font-semibold text-gray-500 uppercase",
                    ),
                    rx.el.p(
                        p["disease"],
                        class_name="text-sm font-bold text-gray-900",
                    ),
                ),
                rx.el.div(
                    rx.el.p(
                        "Progress",
                        class_name="text-[10px] font-semibold text-gray-500 uppercase",
                    ),
                    rx.el.div(
                        rx.el.p(
                            f"{p['treatment_progress']}%",
                            class_name="text-sm font-bold text-blue-600",
                        ),
                        rx.el.button(
                            rx.icon("plus", class_name="h-3 w-3"),
                            on_click=lambda: (
                                HealthcareState.update_treatment_progress(
                                    p["id"], 5
                                )
                            ),
                            class_name="ml-2 p-1 bg-emerald-100 text-emerald-700 rounded",
                        ),
                        rx.el.button(
                            rx.icon("minus", class_name="h-3 w-3"),
                            on_click=lambda: (
                                HealthcareState.update_treatment_progress(
                                    p["id"], -5
                                )
                            ),
                            class_name="ml-1 p-1 bg-amber-100 text-amber-700 rounded",
                        ),
                        class_name="flex items-center",
                    ),
                ),
                class_name="grid grid-cols-2 gap-4 mt-4 pt-4 border-t border-gray-100",
            ),
            class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm mb-4",
        ),
        section_card(
            "Add Nursing Note", "Document observations", nurse_note_form()
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h4(
                    "Vitals History",
                    class_name="text-sm font-bold text-gray-900 mb-2",
                ),
                rx.cond(
                    HealthcareState.selected_patient_vitals.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            HealthcareState.selected_patient_vitals, n_vital_row
                        ),
                        class_name="space-y-2",
                    ),
                    rx.el.p(
                        "No vitals recorded.",
                        class_name="text-xs text-gray-500 italic",
                    ),
                ),
                class_name="bg-white/80 p-4 rounded-2xl border border-white/60",
            ),
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
                            n_prescription_row,
                        ),
                        class_name="space-y-2",
                    ),
                    rx.el.p(
                        "No prescriptions.",
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
                            HealthcareState.selected_patient_notes, n_note_row
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
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 mt-4",
        ),
    )


def nurse_dashboard_content() -> rx.Component:
    return rx.el.div(
        welcome_banner(
            HealthcareState.current_nurse["name"],
            "nurse",
            f"You have {HealthcareState.nurse_pending_tasks.length()} pending tasks today.",
        ),
        tab_bar(
            [
                ("Overview", "overview", "layout-dashboard"),
                ("Tasks", "tasks", "list-checks"),
                ("Medicines", "medicines", "pill"),
                ("Vitals", "vitals", "activity"),
                ("Appointments", "appointments", "calendar"),
            ]
        ),
        rx.match(
            HealthcareState.active_tab,
            ("tasks", tasks_tab()),
            ("medicines", medicine_tab()),
            ("vitals", vitals_tab()),
            ("appointments", appointments_tab()),
            ("patient_detail", patient_detail_tab()),
            overview_tab(),
        ),
        class_name="max-w-7xl mx-auto",
    )
