import reflex as rx
from app.states.healthcare_state import HealthcareState


def stat_card(
    label: str, value, icon: str, color: str, sub: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name=f"h-5 w-5 text-{color}-600"),
                class_name=f"w-11 h-11 rounded-xl bg-{color}-100 flex items-center justify-center",
            ),
            rx.cond(
                sub != "",
                rx.el.span(
                    sub,
                    class_name="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-lg",
                ),
                rx.el.div(),
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.p(label, class_name="text-sm text-gray-500 font-medium"),
        rx.el.p(value, class_name="text-2xl font-bold text-gray-900 mt-1"),
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm hover:shadow-md transition-all",
    )


def status_badge(status) -> rx.Component:
    return rx.el.span(
        status,
        class_name=rx.match(
            status,
            (
                "Confirmed",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-700 w-fit",
            ),
            (
                "Completed",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-blue-100 text-blue-700 w-fit",
            ),
            (
                "Pending",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-amber-100 text-amber-700 w-fit",
            ),
            (
                "Admitted",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-blue-100 text-blue-700 w-fit",
            ),
            (
                "Outpatient",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-purple-100 text-purple-700 w-fit",
            ),
            (
                "Discharged",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-gray-100 text-gray-700 w-fit",
            ),
            (
                "Available",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-700 w-fit",
            ),
            (
                "On Duty",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-700 w-fit",
            ),
            (
                "Break",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-amber-100 text-amber-700 w-fit",
            ),
            (
                "In Surgery",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-rose-100 text-rose-700 w-fit",
            ),
            (
                "On Rounds",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-blue-100 text-blue-700 w-fit",
            ),
            (
                "Administered",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-700 w-fit",
            ),
            (
                "High",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-rose-100 text-rose-700 w-fit",
            ),
            (
                "Medium",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-amber-100 text-amber-700 w-fit",
            ),
            (
                "Low",
                "text-xs font-semibold px-2.5 py-1 rounded-lg bg-blue-100 text-blue-700 w-fit",
            ),
            "text-xs font-semibold px-2.5 py-1 rounded-lg bg-gray-100 text-gray-700 w-fit",
        ),
    )


def tab_button(label: str, tab_id: str, icon: str) -> rx.Component:
    is_active = HealthcareState.active_tab == tab_id
    return rx.el.button(
        rx.icon(icon, class_name="h-4 w-4"),
        rx.el.span(label, class_name="text-sm font-semibold"),
        on_click=lambda: HealthcareState.set_tab(tab_id),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-2 px-4 py-2.5 rounded-xl bg-blue-600 text-white shadow-md transition-all",
            "flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white text-gray-600 hover:text-blue-600 hover:bg-blue-50 border border-gray-200 transition-all",
        ),
    )


def tab_bar(tabs: list) -> rx.Component:
    return rx.el.div(
        *[tab_button(label, tid, icon) for label, tid, icon in tabs],
        class_name="flex items-center gap-2 flex-wrap mb-6 overflow-x-auto",
    )


def welcome_banner(name, role: str, subtitle: str = "") -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p("Welcome back,", class_name="text-blue-100 text-sm"),
                rx.el.h2(
                    name,
                    class_name="text-2xl md:text-3xl font-bold text-white mt-1",
                ),
                rx.el.p(
                    subtitle,
                    class_name="text-blue-100 text-sm mt-2",
                ),
            ),
            rx.el.div(
                rx.icon("heart-pulse", class_name="h-16 w-16 text-white/20"),
                class_name="hidden md:block",
            ),
            class_name="flex items-center justify-between",
        ),
        class_name="bg-gradient-to-br from-blue-600 to-blue-800 rounded-2xl p-6 md:p-8 shadow-lg mb-6",
    )


def empty_state(icon: str, title: str, message: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8 text-gray-400"),
            class_name="w-16 h-16 rounded-2xl bg-gray-100 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.p(
            title,
            class_name="text-base font-semibold text-gray-900 text-center",
        ),
        rx.el.p(message, class_name="text-sm text-gray-500 text-center mt-1"),
        class_name="p-10 bg-white/80 backdrop-blur-sm rounded-2xl border border-white/60",
    )


def section_card(
    title: str,
    subtitle: str,
    content: rx.Component,
    action: rx.Component = None,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(title, class_name="text-base font-bold text-gray-900"),
                rx.el.p(subtitle, class_name="text-xs text-gray-500 mt-0.5"),
            ),
            rx.cond(
                action is not None,
                action if action is not None else rx.el.div(),
                rx.el.div(),
            ),
            class_name="flex items-start justify-between mb-4",
        ),
        content,
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm",
    )


def form_input(
    label: str,
    name: str,
    placeholder: str,
    input_type: str = "text",
    required: bool = True,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-xs font-semibold text-gray-700 mb-1.5"
        ),
        rx.el.input(
            type=input_type,
            name=name,
            placeholder=placeholder,
            required=required,
            class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm text-gray-900 placeholder-gray-400 focus:outline-hidden focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all",
        ),
    )


def form_textarea(
    label: str, name: str, placeholder: str, required: bool = False
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-xs font-semibold text-gray-700 mb-1.5"
        ),
        rx.el.textarea(
            name=name,
            placeholder=placeholder,
            required=required,
            rows="3",
            class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-xl text-sm text-gray-900 placeholder-gray-400 focus:outline-hidden focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all resize-none",
        ),
    )
