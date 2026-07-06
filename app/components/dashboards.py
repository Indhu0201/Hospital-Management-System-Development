import reflex as rx
from app.components.layout import app_shell
from app.states.auth_state import AuthState
from app.components.patient_dashboard import patient_dashboard_content
from app.components.doctor_dashboard import doctor_dashboard_content
from app.components.nurse_dashboard import nurse_dashboard_content
from app.components.admin_dashboard import (
    admin_content as admin_dashboard_content,
)


def stat_card(
    label: str, value: str, icon: str, color: str, trend: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name=f"h-5 w-5 text-{color}-600"),
                class_name=f"w-11 h-11 rounded-xl bg-{color}-100 flex items-center justify-center",
            ),
            rx.el.span(
                trend,
                class_name="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-lg",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.p(label, class_name="text-sm text-gray-500 font-medium"),
        rx.el.p(value, class_name="text-2xl font-bold text-gray-900 mt-1"),
        class_name="bg-white/80 backdrop-blur-sm p-5 rounded-2xl border border-white/60 shadow-sm hover:shadow-md transition-all",
    )


def welcome_banner(name: str, role: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p("Welcome back,", class_name="text-blue-100 text-sm"),
                rx.el.h2(
                    name,
                    class_name="text-2xl md:text-3xl font-bold text-white mt-1",
                ),
                rx.el.p(
                    f"Here's what's happening in your {role} portal today.",
                    class_name="text-blue-100 text-sm mt-2",
                ),
            ),
            rx.el.div(
                rx.icon("heart-pulse", class_name="h-16 w-16 text-white/20"),
                class_name="hidden md:block",
            ),
            class_name="flex items-center justify-between",
        ),
        class_name="bg-gradient-to-br from-blue-600 to-blue-800 rounded-2xl p-6 md:p-8 shadow-lg",
    )


def admin_content() -> rx.Component:
    return admin_dashboard_content()


def doctor_content() -> rx.Component:
    return doctor_dashboard_content()


def nurse_content() -> rx.Component:
    return nurse_dashboard_content()


def patient_content() -> rx.Component:
    return patient_dashboard_content()


def unauthorized_page(required_role: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("shield-alert", class_name="h-8 w-8 text-red-600"),
                class_name="w-16 h-16 rounded-2xl bg-red-100 flex items-center justify-center mx-auto mb-4",
            ),
            rx.el.h1(
                "Access Restricted",
                class_name="text-2xl font-bold text-gray-900 text-center",
            ),
            rx.el.p(
                f"This area is only accessible to {required_role} accounts. Please sign in with the appropriate role.",
                class_name="text-sm text-gray-600 text-center mt-2 max-w-sm mx-auto",
            ),
            rx.el.div(
                rx.el.a(
                    "Sign In",
                    href="/login",
                    class_name="px-5 py-2.5 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition-all shadow-sm text-sm",
                ),
                rx.el.a(
                    "Go Home",
                    href="/",
                    class_name="px-5 py-2.5 bg-white text-gray-700 border border-gray-200 font-semibold rounded-xl hover:border-blue-300 transition-all text-sm",
                ),
                class_name="flex items-center justify-center gap-3 mt-6",
            ),
            class_name="bg-white/80 backdrop-blur-xl p-8 rounded-2xl shadow-xl border border-white/60 max-w-md w-full",
        ),
        class_name="min-h-screen flex items-center justify-center p-4 bg-gradient-to-br from-blue-50 via-white to-cyan-50 font-['Inter']",
    )


def role_dashboard(
    role: str, role_label: str, content: rx.Component
) -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        rx.cond(
            AuthState.user_role == role,
            app_shell(role, role_label, f"{role_label} Dashboard", content),
            unauthorized_page(role_label),
        ),
        unauthorized_page(role_label),
    )


def admin_dashboard() -> rx.Component:
    return role_dashboard("admin", "Admin", admin_content())


def doctor_dashboard() -> rx.Component:
    return role_dashboard("doctor", "Doctor", doctor_content())


def nurse_dashboard() -> rx.Component:
    return role_dashboard("nurse", "Nurse", nurse_content())


def patient_dashboard() -> rx.Component:
    return role_dashboard("patient", "Patient", patient_content())
