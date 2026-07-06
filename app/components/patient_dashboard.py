import reflex as rx
from app.states.healthcare_state import (
    HealthcareState,
    Appointment,
    Prescription,
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


def profile_card() -> rx.Component:
    p = HealthcareState.current_patient
    d = HealthcareState.patient_assigned_doctor
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("user", class_name="h-8 w-8 text-white"),
                class_name="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-md",
            ),
            rx.el.div(
                rx.el.h3(
                    p["name"], class_name="text-lg font-bold text-gray-900"
                ),
                rx.el.p(p["email"], class_name="text-sm text-gray-500"),
                rx.el.div(
                    status_badge(p["admission_status"]),
                    class_name="mt-2",
                ),
            ),
            class_name="flex items-center gap-4 mb-5",
        ),
        rx.el.div(
            info_row("cake", "Age", f"{p['age']} years"),
            info_row("venus-and-mars", "Gender", p["gender"]),
            info_row("droplet", "Blood Type", p["blood_type"]),
            info_row("phone", "Phone", p["phone"]),
            info_row("bed", "Room", p["room"]),
            info_row("stethoscope", "Assigned Doctor", d["name"]),
            class_name="grid grid-cols-1 sm:grid-cols-2 gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Treatment Progress",
                    class_name="text-xs font-semibold text-gray-700",
                ),
                rx.el.p(
                    f"{p['treatment_progress']}%",
                    class_name="text-xs font-bold text-blue-600",
                ),
                class_name="flex items-center justify-between mb-2",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-gradient-to-r from-blue-500 to-blue-600 rounded-full transition-all",
                    style={"width": p["treatment_progress"].to_string() + "%"},
                ),
                class_name="h-2 bg-gray-100 rounded-full overflow-hidden",
            ),
            class_name="mt-5 pt-5 border-t border-gray-100",
        ),
        class_name="bg-white/80 backdrop-blur-sm p-6 rounded-2xl border border-white/60 shadow-sm",
    )


def info_row(icon: str, label: str, value) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-4 w-4 text-blue-600"),
            class_name="w-8 h-8 rounded-lg bg-blue-50 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(label, class_name="text-xs text-gray-500"),
            rx.el.p(
                value, class_name="text-sm font-semibold text-gray-900 truncate"
            ),
        ),
        class_name="flex items-center gap-3 p-2.5 bg-gray-50/60 rounded-xl",
    )


def assigned_doctor_card() -> rx.Component:
    d = HealthcareState.patient_assigned_doctor
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("stethoscope", class_name="h-6 w-6 text-emerald-600"),
                class_name="w-12 h-12 rounded-xl bg-emerald-100 flex items-center justify-center",
            ),
            rx.el.div(
                rx.el.p(
                    d["name"], class_name="text-base font-bold text-gray-900"
                ),
                rx.el.p(
                    d["specialty"],
                    class_name="text-sm text-emerald-600 font-medium",
                ),
                rx.el.div(status_badge(d["status"]), class_name="mt-1"),
            ),
            class_name="flex items-center gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("mail", class_name="h-3.5 w-3.5 text-gray-400"),
                rx.el.span(d["email"], class_name="text-xs text-gray-600"),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.icon("phone", class_name="h-3.5 w-3.5 text-gray-400"),
                rx.el.span(d["phone"], class_name="text-xs text-gray-600"),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.icon("building-2", class_name="h-3.5 w-3.5 text-gray-400"),
                rx.el.span(d["department"], class_name="text-xs text-gray-600"),
                class_name="flex items-center gap-2",
            ),
            class_name="mt-4 pt-4 border-t border-gray-100 space-y-1.5",
        ),
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
    )


def appointment_row(a: Appointment) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("calendar", class_name="h-4 w-4 text-blue-600"),
                class_name="w-9 h-9 rounded-lg bg-blue-100 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    a["reason"],
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.p(
                    f"{a['doctor_name']} • {a['date']} at {a['time']}",
                    class_name="text-xs text-gray-500 mt-0.5",
                ),
            ),
            class_name="flex items-center gap-3 flex-1 min-w-0",
        ),
        status_badge(a["status"]),
        class_name="flex items-center justify-between p-3 bg-gray-50/60 rounded-xl hover:bg-blue-50/50 transition-colors",
    )


def prescription_row(p: Prescription) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("pill", class_name="h-4 w-4 text-purple-600"),
                class_name="w-9 h-9 rounded-lg bg-purple-100 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    p["medicine"],
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.p(
                    f"{p['dosage']} • {p['frequency']} • {p['duration']}",
                    class_name="text-xs text-gray-500 mt-0.5",
                ),
                rx.el.p(
                    f"Prescribed by {p['doctor_name']} on {p['date']}",
                    class_name="text-xs text-gray-400 mt-0.5",
                ),
            ),
            class_name="flex items-start gap-3 flex-1 min-w-0",
        ),
        class_name="p-3 bg-gray-50/60 rounded-xl hover:bg-purple-50/40 transition-colors",
    )


def history_row(h: HistoryEntry) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("file-text", class_name="h-4 w-4 text-blue-600"),
                class_name="w-9 h-9 rounded-lg bg-blue-100 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    h["diagnosis"],
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.p(h["notes"], class_name="text-xs text-gray-600 mt-1"),
                rx.el.p(
                    f"{h['doctor_name']} • {h['date']}",
                    class_name="text-xs text-gray-400 mt-1",
                ),
            ),
            class_name="flex items-start gap-3",
        ),
        class_name="p-3 bg-gray-50/60 rounded-xl",
    )


def overview_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            stat_card(
                "Upcoming Visits",
                HealthcareState.patient_appointments.length().to_string(),
                "calendar",
                "blue",
            ),
            stat_card(
                "Prescriptions",
                HealthcareState.patient_prescriptions.length().to_string(),
                "pill",
                "purple",
            ),
            stat_card(
                "Medical Records",
                HealthcareState.patient_history.length().to_string(),
                "file-text",
                "emerald",
            ),
            stat_card(
                "Progress",
                HealthcareState.current_patient[
                    "treatment_progress"
                ].to_string()
                + "%",
                "trending-up",
                "amber",
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(profile_card(), class_name="lg:col-span-2"),
            assigned_doctor_card(),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4",
        ),
    )


def appointments_tab() -> rx.Component:
    return rx.el.div(
        section_card(
            "Book New Appointment",
            "Select doctor, date, and time",
            rx.el.form(
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Select Doctor",
                            class_name="block text-xs font-semibold text-gray-700 mb-1.5",
                        ),
                        rx.el.div(
                            rx.el.select(
                                rx.foreach(
                                    HealthcareState.doctors,
                                    lambda d: rx.el.option(
                                        f"{d['name']} - {d['specialty']}",
                                        value=d["id"].to_string(),
                                    ),
                                ),
                                name="doctor_id",
                                class_name="w-full px-3 py-2 pr-8 bg-white border border-gray-200 rounded-xl text-sm text-gray-900 appearance-none cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.icon(
                                "chevron-down",
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                            ),
                            class_name="relative",
                        ),
                    ),
                    form_input("Date", "date", "", "date"),
                    form_input("Time", "time", "", "time"),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-3",
                ),
                form_textarea(
                    "Reason for Visit",
                    "reason",
                    "Describe the reason for appointment",
                    True,
                ),
                rx.el.button(
                    rx.icon("calendar-plus", class_name="h-4 w-4"),
                    "Book Appointment",
                    type="submit",
                    class_name="mt-4 flex items-center gap-2 px-5 py-2.5 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 transition-all shadow-sm",
                ),
                on_submit=HealthcareState.book_appointment,
                reset_on_submit=True,
                class_name="space-y-3",
            ),
        ),
        rx.el.div(
            rx.el.h3(
                "My Appointments",
                class_name="text-base font-bold text-gray-900 mb-3",
            ),
            rx.cond(
                HealthcareState.patient_appointments.length() > 0,
                rx.el.div(
                    rx.foreach(
                        HealthcareState.patient_appointments, appointment_row
                    ),
                    class_name="space-y-2",
                ),
                empty_state(
                    "calendar-x",
                    "No appointments yet",
                    "Book your first appointment above.",
                ),
            ),
            class_name="mt-6",
        ),
    )


def prescriptions_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Active Prescriptions",
            class_name="text-base font-bold text-gray-900 mb-3",
        ),
        rx.cond(
            HealthcareState.patient_prescriptions.length() > 0,
            rx.el.div(
                rx.foreach(
                    HealthcareState.patient_prescriptions, prescription_row
                ),
                class_name="space-y-2",
            ),
            empty_state(
                "pill",
                "No prescriptions",
                "Your doctor hasn't prescribed any medicines yet.",
            ),
        ),
    )


def history_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Medical History",
            class_name="text-base font-bold text-gray-900 mb-3",
        ),
        rx.cond(
            HealthcareState.patient_history.length() > 0,
            rx.el.div(
                rx.foreach(HealthcareState.patient_history, history_row),
                class_name="space-y-2",
            ),
            empty_state(
                "file-text",
                "No history yet",
                "Your medical records will appear here.",
            ),
        ),
    )


def notifications_tab() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Notifications", class_name="text-base font-bold text-gray-900 mb-3"
        ),
        rx.el.div(
            notif_item(
                "bell",
                "Upcoming appointment tomorrow at 09:00 AM with Dr. Sarah Rivera",
                "2 hours ago",
                "blue",
            ),
            notif_item(
                "pill",
                "Reminder: Take Atorvastatin 20mg tonight",
                "5 hours ago",
                "purple",
            ),
            notif_item(
                "flask-conical",
                "New lab results are ready to view",
                "1 day ago",
                "emerald",
            ),
            notif_item(
                "file-text",
                "Dr. Sarah Rivera added a note to your records",
                "2 days ago",
                "amber",
            ),
            notif_item(
                "calendar-check",
                "Your appointment on Nov 22 has been confirmed",
                "3 days ago",
                "blue",
            ),
            class_name="space-y-2",
        ),
    )


def notif_item(icon: str, msg: str, time: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-4 w-4 text-{color}-600"),
            class_name=f"w-9 h-9 rounded-lg bg-{color}-100 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(msg, class_name="text-sm text-gray-900 font-medium"),
            rx.el.p(time, class_name="text-xs text-gray-500 mt-0.5"),
        ),
        class_name="flex items-start gap-3 p-3 bg-white/80 rounded-xl border border-white/60 hover:shadow-sm transition-all",
    )


def patient_dashboard_content() -> rx.Component:
    return rx.el.div(
        welcome_banner(
            HealthcareState.current_patient["name"],
            "patient",
            "Manage your appointments, prescriptions, and health records.",
        ),
        tab_bar(
            [
                ("Overview", "overview", "layout-dashboard"),
                ("Appointments", "appointments", "calendar"),
                ("Prescriptions", "prescriptions", "pill"),
                ("Medical History", "history", "file-text"),
                ("Notifications", "notifications", "bell"),
            ]
        ),
        rx.match(
            HealthcareState.active_tab,
            ("appointments", appointments_tab()),
            ("prescriptions", prescriptions_tab()),
            ("history", history_tab()),
            ("notifications", notifications_tab()),
            overview_tab(),
        ),
        class_name="max-w-7xl mx-auto",
    )
