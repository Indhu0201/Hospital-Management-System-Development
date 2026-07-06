import reflex as rx
from app.states.admin_state import (
    AdminState,
    Department,
    ActivityLog,
    UserAccount,
)
from app.states.healthcare_state import (
    HealthcareState,
    Patient,
    Doctor,
    Nurse,
    Appointment,
)
from app.states.auth_state import AuthState
from app.components.dashboard_ui import (
    stat_card,
    status_badge,
    tab_bar,
    welcome_banner,
    empty_state,
)


TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "borderColor": "#E8E8E8",
        "borderRadius": "0.75rem",
        "boxShadow": "0px 8px 24px rgba(28, 32, 36, 0.08)",
        "fontFamily": "Inter, sans-serif",
        "fontSize": "0.8125rem",
        "fontWeight": "500",
        "padding": "0.5rem 0.75rem",
    },
    "item_style": {"color": "#111827"},
    "label_style": {"color": "#6B7280", "fontWeight": "600"},
    "separator": "",
}


def admin_welcome() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("shield", class_name="h-4 w-4 text-white"),
                    rx.el.span(
                        "System Administrator",
                        class_name="text-xs font-semibold text-white",
                    ),
                    class_name="inline-flex items-center gap-2 bg-white/20 backdrop-blur-sm px-3 py-1 rounded-full mb-3 w-fit",
                ),
                rx.el.h2(
                    f"Welcome, {AuthState.user_name}",
                    class_name="text-2xl md:text-3xl font-bold text-white",
                ),
                rx.el.p(
                    "Full oversight of hospital operations, staff, and patient care.",
                    class_name="text-blue-100 text-sm mt-2",
                ),
            ),
            rx.el.div(
                rx.icon(
                    "layout-dashboard", class_name="h-16 w-16 text-white/20"
                ),
                class_name="hidden md:block",
            ),
            class_name="flex items-center justify-between",
        ),
        class_name="bg-gradient-to-br from-blue-600 via-blue-700 to-blue-800 rounded-2xl p-6 md:p-8 shadow-lg mb-6",
    )


def metrics_grid() -> rx.Component:
    return rx.el.div(
        stat_card(
            "Total Patients",
            HealthcareState.patients.length().to_string(),
            "users",
            "blue",
            "+12%",
        ),
        stat_card(
            "Total Doctors",
            HealthcareState.doctors.length().to_string(),
            "stethoscope",
            "emerald",
            "+3%",
        ),
        stat_card(
            "Total Nurses",
            HealthcareState.nurses.length().to_string(),
            "heart-pulse",
            "rose",
            "+5%",
        ),
        stat_card(
            "Appointments",
            HealthcareState.appointments.length().to_string(),
            "calendar",
            "purple",
            "+18%",
        ),
        stat_card(
            "Departments",
            AdminState.total_departments.to_string(),
            "building-2",
            "amber",
        ),
        stat_card(
            "Active Users",
            AdminState.active_users_count.to_string(),
            "user-check",
            "cyan",
        ),
        class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 md:gap-4 mb-6",
    )


def appointment_trends_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Appointment Trends",
                    class_name="text-base font-bold text-gray-900",
                ),
                rx.el.p(
                    "Weekly overview of scheduled vs completed",
                    class_name="text-xs text-gray-500 mt-0.5",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        class_name="w-2.5 h-2.5 rounded-sm bg-blue-500 inline-block"
                    ),
                    rx.el.span(
                        "Scheduled",
                        class_name="text-xs font-medium text-gray-600",
                    ),
                    class_name="flex items-center gap-1.5",
                ),
                rx.el.div(
                    rx.el.span(
                        class_name="w-2.5 h-2.5 rounded-sm bg-emerald-500 inline-block"
                    ),
                    rx.el.span(
                        "Completed",
                        class_name="text-xs font-medium text-gray-600",
                    ),
                    class_name="flex items-center gap-1.5",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-start justify-between mb-4 flex-wrap gap-2",
        ),
        rx.recharts.line_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="opacity-30"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.line(
                data_key="scheduled",
                name="Scheduled",
                stroke="#2563EB",
                stroke_width=2,
                type_="natural",
            ),
            rx.recharts.line(
                data_key="completed",
                name="Completed",
                stroke="#10B981",
                stroke_width=2,
                type_="natural",
            ),
            rx.recharts.x_axis(
                data_key="day",
                axis_line=False,
                tick_line=False,
                tick_size=10,
                custom_attrs={"fontSize": "12px"},
            ),
            rx.recharts.y_axis(
                axis_line=False,
                tick_line=False,
                tick_size=10,
                custom_attrs={"fontSize": "12px"},
            ),
            data=AdminState.appointment_trends,
            width="100%",
            height=280,
            margin={"left": 0, "right": 20, "top": 10, "bottom": 10},
        ),
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
    )


def department_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Department Distribution",
                class_name="text-base font-bold text-gray-900",
            ),
            rx.el.p(
                "Staff and bed allocation by department",
                class_name="text-xs text-gray-500 mt-0.5",
            ),
            class_name="mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="opacity-30"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.bar(
                data_key="staff",
                name="Staff",
                fill="#3B82F6",
                radius=[6, 6, 0, 0],
            ),
            rx.recharts.bar(
                data_key="beds",
                name="Beds",
                fill="#06B6D4",
                radius=[6, 6, 0, 0],
            ),
            rx.recharts.x_axis(
                data_key="name",
                axis_line=False,
                tick_line=False,
                tick_size=10,
                custom_attrs={"fontSize": "10px"},
                interval=0,
                angle=-25,
                text_anchor="end",
                height=60,
            ),
            rx.recharts.y_axis(
                axis_line=False,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
            ),
            data=AdminState.department_distribution,
            width="100%",
            height=280,
            margin={"left": 0, "right": 20, "top": 10, "bottom": 10},
        ),
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
    )


def activity_row(log: ActivityLog) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                rx.match(
                    log["category"],
                    ("prescription", "pill"),
                    ("appointment", "calendar"),
                    ("vitals", "activity"),
                    ("medication", "syringe"),
                    ("user", "user-plus"),
                    ("department", "building-2"),
                    ("diagnosis", "clipboard-check"),
                    ("system", "server"),
                    ("task", "check-square"),
                    "circle",
                ),
                class_name="h-4 w-4 text-blue-600",
            ),
            class_name="w-9 h-9 rounded-lg bg-blue-50 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    log["user"],
                    class_name="text-sm font-semibold text-gray-900",
                ),
                rx.el.span(
                    log["role"],
                    class_name="text-[10px] font-bold px-1.5 py-0.5 rounded bg-gray-100 text-gray-600 ml-2",
                ),
                class_name="flex items-center flex-wrap",
            ),
            rx.el.p(
                f"{log['action']} • {log['target']}",
                class_name="text-xs text-gray-600 mt-0.5",
            ),
        ),
        rx.el.p(
            log["time"],
            class_name="text-xs text-gray-400 ml-auto shrink-0 hidden sm:block",
        ),
        class_name="flex items-center gap-3 p-3 bg-white/80 rounded-xl border border-white/60 hover:shadow-sm transition-all",
    )


def overview_tab() -> rx.Component:
    return rx.el.div(
        metrics_grid(),
        rx.el.div(
            appointment_trends_chart(),
            department_chart(),
            class_name="grid grid-cols-1 xl:grid-cols-2 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Recent Activity",
                    class_name="text-base font-bold text-gray-900",
                ),
                rx.el.button(
                    "View All",
                    on_click=lambda: AdminState.set_tab("activity"),
                    class_name="text-xs font-semibold text-blue-600 hover:text-blue-700",
                ),
                class_name="flex items-center justify-between mb-3",
            ),
            rx.el.div(
                rx.foreach(AdminState.activity_logs[:5], activity_row),
                class_name="space-y-2",
            ),
            class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
        ),
    )


def search_bar(placeholder: str = "Search...") -> rx.Component:
    return rx.el.div(
        rx.icon(
            "search",
            class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
        ),
        rx.el.input(
            placeholder=placeholder,
            default_value=AdminState.search_query,
            on_change=AdminState.set_search.debounce(300),
            class_name="w-full pl-10 pr-4 py-2.5 bg-white border border-gray-200 rounded-xl text-sm placeholder-gray-400 focus:outline-hidden focus:ring-2 focus:ring-blue-500 focus:border-transparent",
        ),
        class_name="relative flex-1 min-w-0",
    )


def doctor_row(d: Doctor) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "stethoscope", class_name="h-4 w-4 text-emerald-600"
                    ),
                    class_name="w-9 h-9 rounded-lg bg-emerald-100 flex items-center justify-center shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        d["name"],
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    rx.el.p(d["email"], class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(d["specialty"], class_name="px-4 py-3 text-sm text-gray-700"),
        rx.el.td(
            d["department"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden md:table-cell",
        ),
        rx.el.td(
            d["phone"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden lg:table-cell",
        ),
        rx.el.td(status_badge(d["status"]), class_name="px-4 py-3"),
        class_name="border-b border-gray-100 hover:bg-blue-50/40 transition-colors",
    )


def doctors_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            search_bar("Search doctors..."),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                "Add Doctor",
                on_click=lambda: AdminState.open_modal("user"),
                class_name="flex items-center gap-2 px-4 py-2.5 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 shadow-sm shrink-0",
            ),
            class_name="flex items-center gap-3 mb-4 flex-wrap",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Doctor",
                                class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Specialty",
                                class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Department",
                                class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider hidden md:table-cell",
                            ),
                            rx.el.th(
                                "Phone",
                                class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider hidden lg:table-cell",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider",
                            ),
                            class_name="bg-gray-50/60",
                        ),
                    ),
                    rx.el.tbody(
                        rx.foreach(HealthcareState.doctors, doctor_row)
                    ),
                    class_name="table-auto w-full",
                ),
                class_name="min-w-full",
            ),
            class_name="bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60 shadow-sm overflow-hidden overflow-x-auto",
        ),
    )


def nurse_row(n: Nurse) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.icon("heart-pulse", class_name="h-4 w-4 text-rose-600"),
                    class_name="w-9 h-9 rounded-lg bg-rose-100 flex items-center justify-center shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        n["name"],
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    rx.el.p(n["email"], class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(n["department"], class_name="px-4 py-3 text-sm text-gray-700"),
        rx.el.td(
            n["shift"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden md:table-cell",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.p(
                    f"{n['tasks_done']}/{n['tasks_total']}",
                    class_name="text-xs font-bold text-gray-900",
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
                    class_name="h-1.5 w-24 bg-gray-100 rounded-full overflow-hidden mt-1",
                ),
            ),
            class_name="px-4 py-3 hidden lg:table-cell",
        ),
        rx.el.td(status_badge(n["status"]), class_name="px-4 py-3"),
        class_name="border-b border-gray-100 hover:bg-blue-50/40 transition-colors",
    )


def nurses_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            search_bar("Search nurses..."),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                "Add Nurse",
                on_click=lambda: AdminState.open_modal("user"),
                class_name="flex items-center gap-2 px-4 py-2.5 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 shadow-sm shrink-0",
            ),
            class_name="flex items-center gap-3 mb-4 flex-wrap",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Nurse",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Department",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Shift",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Tasks",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden lg:table-cell",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        class_name="bg-gray-50/60",
                    ),
                ),
                rx.el.tbody(rx.foreach(HealthcareState.nurses, nurse_row)),
                class_name="table-auto w-full",
            ),
            class_name="bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60 shadow-sm overflow-hidden overflow-x-auto",
        ),
    )


def patient_row(p: Patient) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="h-4 w-4 text-blue-600"),
                    class_name="w-9 h-9 rounded-lg bg-blue-100 flex items-center justify-center shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        p["name"],
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    rx.el.p(p["email"], class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(p["disease"], class_name="px-4 py-3 text-sm text-gray-700"),
        rx.el.td(
            f"{p['age']}y • {p['gender']}",
            class_name="px-4 py-3 text-sm text-gray-700 hidden md:table-cell",
        ),
        rx.el.td(
            p["room"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden lg:table-cell",
        ),
        rx.el.td(
            f"{p['treatment_progress']}%",
            class_name="px-4 py-3 text-sm font-bold text-blue-600 hidden lg:table-cell",
        ),
        rx.el.td(status_badge(p["admission_status"]), class_name="px-4 py-3"),
        class_name="border-b border-gray-100 hover:bg-blue-50/40 transition-colors",
    )


def patients_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            search_bar("Search patients..."),
            class_name="flex items-center gap-3 mb-4",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Patient",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Condition",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Age/Gender",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Room",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden lg:table-cell",
                        ),
                        rx.el.th(
                            "Progress",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden lg:table-cell",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        class_name="bg-gray-50/60",
                    ),
                ),
                rx.el.tbody(rx.foreach(HealthcareState.patients, patient_row)),
                class_name="table-auto w-full",
            ),
            class_name="bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60 shadow-sm overflow-hidden overflow-x-auto",
        ),
    )


def appointment_row(a: Appointment) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.p(
                    a["time"], class_name="text-sm font-bold text-blue-600"
                ),
                rx.el.p(a["date"], class_name="text-xs text-gray-500"),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            a["patient_name"],
            class_name="px-4 py-3 text-sm font-semibold text-gray-900",
        ),
        rx.el.td(
            a["doctor_name"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden md:table-cell",
        ),
        rx.el.td(
            a["reason"],
            class_name="px-4 py-3 text-sm text-gray-600 hidden lg:table-cell",
        ),
        rx.el.td(status_badge(a["status"]), class_name="px-4 py-3"),
        class_name="border-b border-gray-100 hover:bg-blue-50/40 transition-colors",
    )


def appointments_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                f"All Appointments ({HealthcareState.appointments.length()})",
                class_name="text-base font-bold text-gray-900",
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "When",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Patient",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Doctor",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Reason",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden lg:table-cell",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        class_name="bg-gray-50/60",
                    ),
                ),
                rx.el.tbody(
                    rx.foreach(HealthcareState.appointments, appointment_row)
                ),
                class_name="table-auto w-full",
            ),
            class_name="bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60 shadow-sm overflow-hidden overflow-x-auto",
        ),
    )


def department_row(d: Department) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.icon("building-2", class_name="h-4 w-4 text-purple-600"),
                    class_name="w-9 h-9 rounded-lg bg-purple-100 flex items-center justify-center shrink-0",
                ),
                rx.el.p(
                    d["name"], class_name="text-sm font-bold text-gray-900"
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(d["head"], class_name="px-4 py-3 text-sm text-gray-700"),
        rx.el.td(
            d["staff_count"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden md:table-cell",
        ),
        rx.el.td(
            d["beds"],
            class_name="px-4 py-3 text-sm text-gray-700 hidden md:table-cell",
        ),
        rx.el.td(status_badge(d["status"]), class_name="px-4 py-3"),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("power", class_name="h-3.5 w-3.5"),
                    on_click=lambda: AdminState.toggle_department_status(
                        d["id"]
                    ),
                    class_name="p-1.5 bg-amber-100 text-amber-700 rounded-lg hover:bg-amber-200 transition-all",
                    title="Toggle status",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-3.5 w-3.5"),
                    on_click=lambda: AdminState.delete_department(d["id"]),
                    class_name="p-1.5 bg-red-100 text-red-700 rounded-lg hover:bg-red-200 transition-all",
                    title="Delete",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-gray-100 hover:bg-blue-50/40 transition-colors",
    )


def add_department_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label(
                "Department Name",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.input(
                name="name",
                placeholder="e.g., Oncology",
                required=True,
                class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm focus:outline-hidden focus:ring-2 focus:ring-blue-500",
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Department Head",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.input(
                name="head",
                placeholder="Dr. Full Name",
                required=True,
                class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm focus:outline-hidden focus:ring-2 focus:ring-blue-500",
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Number of Beds",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.input(
                name="beds",
                type="number",
                placeholder="0",
                default_value="0",
                class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm focus:outline-hidden focus:ring-2 focus:ring-blue-500",
            ),
        ),
        rx.el.div(
            rx.el.button(
                "Cancel",
                type="button",
                on_click=AdminState.close_modal,
                class_name="px-4 py-2 bg-white text-gray-700 border border-gray-200 text-sm font-semibold rounded-xl hover:border-gray-300",
            ),
            rx.el.button(
                "Add Department",
                type="submit",
                class_name="px-4 py-2 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700",
            ),
            class_name="flex items-center justify-end gap-2 pt-2",
        ),
        on_submit=AdminState.add_department,
        reset_on_submit=True,
        class_name="space-y-4",
    )


def add_user_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label(
                "Full Name",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.input(
                name="name",
                placeholder="Full Name",
                required=True,
                class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm focus:outline-hidden focus:ring-2 focus:ring-blue-500",
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Email",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.input(
                name="email",
                type="email",
                placeholder="user@medicare.com",
                required=True,
                class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm focus:outline-hidden focus:ring-2 focus:ring-blue-500",
            ),
        ),
        rx.el.div(
            rx.el.label(
                "Role",
                class_name="block text-xs font-semibold text-gray-700 mb-1.5",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("Doctor", value="Doctor"),
                    rx.el.option("Nurse", value="Nurse"),
                    rx.el.option("Patient", value="Patient"),
                    rx.el.option("Admin", value="Admin"),
                    name="role",
                    class_name="w-full px-3 py-2 pr-8 bg-white border border-gray-200 rounded-xl text-sm appearance-none cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-blue-500",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                ),
                class_name="relative",
            ),
        ),
        rx.el.div(
            rx.el.button(
                "Cancel",
                type="button",
                on_click=AdminState.close_modal,
                class_name="px-4 py-2 bg-white text-gray-700 border border-gray-200 text-sm font-semibold rounded-xl hover:border-gray-300",
            ),
            rx.el.button(
                "Add User",
                type="submit",
                class_name="px-4 py-2 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700",
            ),
            class_name="flex items-center justify-end gap-2 pt-2",
        ),
        on_submit=AdminState.add_user,
        reset_on_submit=True,
        class_name="space-y-4",
    )


def modal() -> rx.Component:
    return rx.cond(
        AdminState.show_add_modal,
        rx.el.div(
            rx.el.div(
                on_click=AdminState.close_modal,
                class_name="fixed inset-0 bg-black/40 backdrop-blur-sm z-50",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        rx.cond(
                            AdminState.modal_type == "department",
                            "Add Department",
                            "Add New User",
                        ),
                        class_name="text-lg font-bold text-gray-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-4 w-4"),
                        on_click=AdminState.close_modal,
                        class_name="p-1.5 hover:bg-gray-100 rounded-lg text-gray-500",
                    ),
                    class_name="flex items-center justify-between mb-4",
                ),
                rx.cond(
                    AdminState.modal_type == "department",
                    add_department_form(),
                    add_user_form(),
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-md bg-white rounded-2xl shadow-2xl border border-white/60 p-6",
            ),
        ),
        rx.el.div(),
    )


def departments_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            search_bar("Search departments..."),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                "Add Department",
                on_click=lambda: AdminState.open_modal("department"),
                class_name="flex items-center gap-2 px-4 py-2.5 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 shadow-sm shrink-0",
            ),
            class_name="flex items-center gap-3 mb-4 flex-wrap",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Department",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Head",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Staff",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Beds",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        class_name="bg-gray-50/60",
                    ),
                ),
                rx.el.tbody(
                    rx.foreach(AdminState.filtered_departments, department_row)
                ),
                class_name="table-auto w-full",
            ),
            class_name="bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60 shadow-sm overflow-hidden overflow-x-auto",
        ),
    )


def user_row(u: UserAccount) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="h-4 w-4 text-white"),
                    class_name="w-9 h-9 rounded-lg bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shrink-0",
                ),
                rx.el.div(
                    rx.el.p(
                        u["name"],
                        class_name="text-sm font-semibold text-gray-900",
                    ),
                    rx.el.p(u["email"], class_name="text-xs text-gray-500"),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                u["role"],
                class_name="text-xs font-bold px-2 py-1 rounded-lg bg-blue-100 text-blue-700 w-fit",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            u["last_login"],
            class_name="px-4 py-3 text-xs text-gray-600 hidden md:table-cell",
        ),
        rx.el.td(status_badge(u["status"]), class_name="px-4 py-3"),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("power", class_name="h-3.5 w-3.5"),
                    on_click=lambda: AdminState.toggle_user_status(u["id"]),
                    class_name="p-1.5 bg-amber-100 text-amber-700 rounded-lg hover:bg-amber-200",
                    title="Toggle Active/Inactive",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-3.5 w-3.5"),
                    on_click=lambda: AdminState.delete_user(u["id"]),
                    class_name="p-1.5 bg-red-100 text-red-700 rounded-lg hover:bg-red-200",
                    title="Delete",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-gray-100 hover:bg-blue-50/40 transition-colors",
    )


def users_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            search_bar("Search users by name, email, or role..."),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All Roles", value="all"),
                    rx.el.option("Doctor", value="Doctor"),
                    rx.el.option("Nurse", value="Nurse"),
                    rx.el.option("Patient", value="Patient"),
                    rx.el.option("Admin", value="Admin"),
                    on_change=AdminState.set_filter_role,
                    default_value=AdminState.filter_role,
                    class_name="px-3 py-2.5 pr-8 bg-white border border-gray-200 rounded-xl text-sm appearance-none cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-blue-500",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                ),
                class_name="relative shrink-0",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All Statuses", value="all"),
                    rx.el.option("Active", value="Active"),
                    rx.el.option("Inactive", value="Inactive"),
                    on_change=AdminState.set_filter_status,
                    default_value=AdminState.filter_status,
                    class_name="px-3 py-2.5 pr-8 bg-white border border-gray-200 rounded-xl text-sm appearance-none cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-blue-500",
                ),
                rx.icon(
                    "chevron-down",
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                ),
                class_name="relative shrink-0",
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4"),
                "Add User",
                on_click=lambda: AdminState.open_modal("user"),
                class_name="flex items-center gap-2 px-4 py-2.5 bg-blue-600 text-white text-sm font-semibold rounded-xl hover:bg-blue-700 shrink-0",
            ),
            class_name="flex items-center gap-2 mb-4 flex-wrap",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "User",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Role",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Last Login",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase hidden md:table-cell",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase",
                        ),
                        class_name="bg-gray-50/60",
                    ),
                ),
                rx.el.tbody(rx.foreach(AdminState.filtered_users, user_row)),
                class_name="table-auto w-full",
            ),
            class_name="bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60 shadow-sm overflow-hidden overflow-x-auto",
        ),
    )


def activity_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            search_bar("Search activity logs..."),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.foreach(AdminState.filtered_activity_logs, activity_row),
            class_name="space-y-2",
        ),
    )


def report_card(
    title: str, value, icon: str, color: str, desc: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-5 w-5 text-{color}-600"),
            class_name=f"w-11 h-11 rounded-xl bg-{color}-100 flex items-center justify-center mb-3",
        ),
        rx.el.p(
            title,
            class_name="text-xs font-semibold text-gray-500 uppercase tracking-wide",
        ),
        rx.el.p(value, class_name="text-2xl font-bold text-gray-900 mt-1"),
        rx.el.p(desc, class_name="text-xs text-gray-500 mt-1"),
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
    )


def reports_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            report_card(
                "Total Records",
                HealthcareState.medical_history.length().to_string(),
                "file-text",
                "blue",
                "All patient medical entries",
            ),
            report_card(
                "Prescriptions Issued",
                HealthcareState.prescriptions.length().to_string(),
                "pill",
                "purple",
                "Active + historical",
            ),
            report_card(
                "Vitals Recorded",
                HealthcareState.vitals.length().to_string(),
                "activity",
                "rose",
                "This period",
            ),
            report_card(
                "Clinical Notes",
                HealthcareState.clinical_notes.length().to_string(),
                "clipboard-list",
                "emerald",
                "Doctor & nurse notes",
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6",
        ),
        rx.el.div(
            appointment_trends_chart(),
            department_chart(),
            class_name="grid grid-cols-1 xl:grid-cols-2 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Available Reports",
                        class_name="text-base font-bold text-gray-900",
                    ),
                    rx.el.p(
                        "Download or view detailed reports",
                        class_name="text-xs text-gray-500 mt-0.5",
                    ),
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                report_link(
                    "Patient Census Report",
                    "PDF • Updated daily",
                    "users",
                    "blue",
                ),
                report_link(
                    "Doctor Performance",
                    "PDF • Weekly",
                    "stethoscope",
                    "emerald",
                ),
                report_link(
                    "Financial Summary",
                    "XLSX • Monthly",
                    "dollar-sign",
                    "amber",
                ),
                report_link(
                    "Medication Usage", "PDF • Weekly", "pill", "purple"
                ),
                report_link(
                    "Department Utilization",
                    "PDF • Monthly",
                    "building-2",
                    "cyan",
                ),
                report_link(
                    "Staff Attendance",
                    "XLSX • Weekly",
                    "calendar-check",
                    "rose",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3",
            ),
            class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
        ),
    )


def report_link(title: str, meta: str, icon: str, color: str) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.icon(icon, class_name=f"h-4 w-4 text-{color}-600"),
            class_name=f"w-9 h-9 rounded-lg bg-{color}-100 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(
                title,
                class_name="text-sm font-semibold text-gray-900 text-left",
            ),
            rx.el.p(meta, class_name="text-xs text-gray-500 text-left"),
        ),
        rx.icon("download", class_name="h-4 w-4 text-gray-400 ml-auto"),
        on_click=lambda: rx.toast(f"Preparing {title}...", duration=2000),
        class_name="flex items-center gap-3 p-3 bg-white rounded-xl border border-gray-100 hover:border-blue-300 hover:shadow-md transition-all cursor-pointer w-full",
    )


def admin_content() -> rx.Component:
    return rx.el.div(
        modal(),
        admin_welcome(),
        tab_bar(
            [
                ("Overview", "overview", "layout-dashboard"),
                ("Doctors", "doctors", "stethoscope"),
                ("Nurses", "nurses", "heart-pulse"),
                ("Patients", "patients", "users"),
                ("Appointments", "appointments", "calendar"),
                ("Departments", "departments", "building-2"),
                ("Users", "users", "user-cog"),
                ("Activity", "activity", "history"),
                ("Reports", "reports", "chart-bar"),
            ]
        ),
        rx.match(
            AdminState.active_tab,
            ("doctors", doctors_tab()),
            ("nurses", nurses_tab()),
            ("patients", patients_tab()),
            ("appointments", appointments_tab()),
            ("departments", departments_tab()),
            ("users", users_tab()),
            ("activity", activity_tab()),
            ("reports", reports_tab()),
            overview_tab(),
        ),
        class_name="max-w-7xl mx-auto",
    )
