import reflex as rx
from app.states.auth_state import AuthState


ROLES = [
    ("admin", "Admin", "shield", "purple"),
    ("doctor", "Doctor", "stethoscope", "emerald"),
    ("nurse", "Nurse", "heart-pulse", "rose"),
    ("patient", "Patient", "user", "blue"),
]


def role_button(
    role_id: str, label: str, icon: str, color: str
) -> rx.Component:
    is_selected = AuthState.selected_role == role_id
    return rx.el.button(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(label, class_name="text-xs font-semibold mt-1.5"),
        type="button",
        on_click=lambda: AuthState.set_role(role_id),
        class_name=rx.cond(
            is_selected,
            f"flex flex-col items-center justify-center p-3 rounded-xl border-2 border-blue-500 bg-blue-50 text-blue-700 transition-all",
            "flex flex-col items-center justify-center p-3 rounded-xl border-2 border-gray-200 bg-white text-gray-600 hover:border-blue-300 hover:bg-blue-50/50 transition-all",
        ),
    )


def role_selector() -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "Select Your Role",
            class_name="block text-sm font-semibold text-gray-700 mb-3",
        ),
        rx.el.div(
            role_button("admin", "Admin", "shield", "purple"),
            role_button("doctor", "Doctor", "stethoscope", "emerald"),
            role_button("nurse", "Nurse", "heart-pulse", "rose"),
            role_button("patient", "Patient", "user", "blue"),
            class_name="grid grid-cols-4 gap-2",
        ),
        class_name="mb-5",
    )


def auth_shell(
    title: str, subtitle: str, form: rx.Component, footer: rx.Component
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("heart-pulse", class_name="h-6 w-6 text-white"),
                        class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-md",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "MediCare",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        rx.el.p(
                            "Hospital Management",
                            class_name="text-xs text-gray-500",
                        ),
                    ),
                    href="/",
                    class_name="flex items-center gap-3 justify-center mb-8",
                ),
                rx.el.div(
                    rx.el.h1(
                        title, class_name="text-2xl font-bold text-gray-900"
                    ),
                    rx.el.p(subtitle, class_name="text-sm text-gray-600 mt-1"),
                    class_name="text-center mb-6",
                ),
                form,
                footer,
                class_name="w-full max-w-md bg-white/80 backdrop-blur-xl rounded-2xl shadow-xl border border-white/60 p-8",
            ),
            class_name="min-h-screen flex items-center justify-center p-4 relative",
        ),
        rx.el.div(
            class_name="fixed top-20 -left-32 w-96 h-96 bg-blue-200/40 rounded-full blur-3xl -z-10",
        ),
        rx.el.div(
            class_name="fixed bottom-20 -right-32 w-96 h-96 bg-cyan-200/40 rounded-full blur-3xl -z-10",
        ),
        class_name="min-h-screen bg-gradient-to-br from-blue-50 via-white to-cyan-50 font-['Inter']",
    )


def input_field(
    label: str,
    name: str,
    placeholder: str,
    input_type: str = "text",
    icon: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, class_name="block text-sm font-semibold text-gray-700 mb-1.5"
        ),
        rx.el.div(
            rx.icon(
                icon,
                class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
            ),
            rx.el.input(
                type=input_type,
                name=name,
                placeholder=placeholder,
                required=True,
                class_name="w-full pl-10 pr-4 py-2.5 bg-white border border-gray-200 rounded-xl text-sm text-gray-900 placeholder-gray-400 focus:outline-hidden focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all",
            ),
            class_name="relative",
        ),
        class_name="mb-4",
    )


def login_form() -> rx.Component:
    form = rx.el.form(
        role_selector(),
        input_field(
            "Email Address", "email", "you@hospital.com", "email", "mail"
        ),
        input_field(
            "Password", "password", "Enter your password", "password", "lock"
        ),
        rx.cond(
            AuthState.login_error != "",
            rx.el.div(
                rx.icon("circle-alert", class_name="h-4 w-4 text-red-600"),
                rx.el.p(
                    AuthState.login_error, class_name="text-sm text-red-700"
                ),
                class_name="flex items-center gap-2 p-3 bg-red-50 border border-red-100 rounded-xl mb-4",
            ),
            rx.el.div(),
        ),
        rx.el.div(
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    class_name="h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500",
                ),
                rx.el.span("Remember me", class_name="text-sm text-gray-600"),
                class_name="flex items-center gap-2 cursor-pointer",
            ),
            rx.el.a(
                "Forgot password?",
                href="#",
                class_name="text-sm font-semibold text-blue-600 hover:text-blue-700",
            ),
            class_name="flex items-center justify-between mb-5",
        ),
        rx.el.button(
            "Sign In",
            rx.icon("arrow-right", class_name="h-4 w-4"),
            type="submit",
            class_name="w-full flex items-center justify-center gap-2 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition-all shadow-md hover:shadow-lg",
        ),
        on_submit=AuthState.handle_login,
        reset_on_submit=False,
    )
    footer = rx.el.p(
        "Don't have an account? ",
        rx.el.a(
            "Create one",
            href="/register",
            class_name="font-semibold text-blue-600 hover:text-blue-700",
        ),
        class_name="text-center text-sm text-gray-600 mt-6",
    )
    return auth_shell(
        "Welcome Back", "Sign in to access your dashboard", form, footer
    )


def register_form() -> rx.Component:
    form = rx.el.form(
        role_selector(),
        input_field("Full Name", "full_name", "John Doe", "text", "user"),
        input_field(
            "Email Address", "email", "you@hospital.com", "email", "mail"
        ),
        input_field(
            "Password", "password", "Min. 6 characters", "password", "lock"
        ),
        input_field(
            "Confirm Password",
            "confirm_password",
            "Re-enter password",
            "password",
            "lock-keyhole",
        ),
        rx.cond(
            AuthState.register_error != "",
            rx.el.div(
                rx.icon("circle-alert", class_name="h-4 w-4 text-red-600"),
                rx.el.p(
                    AuthState.register_error, class_name="text-sm text-red-700"
                ),
                class_name="flex items-center gap-2 p-3 bg-red-50 border border-red-100 rounded-xl mb-4",
            ),
            rx.el.div(),
        ),
        rx.el.button(
            "Create Account",
            rx.icon("arrow-right", class_name="h-4 w-4"),
            type="submit",
            class_name="w-full flex items-center justify-center gap-2 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition-all shadow-md hover:shadow-lg",
        ),
        on_submit=AuthState.handle_register,
        reset_on_submit=False,
    )
    footer = rx.el.p(
        "Already have an account? ",
        rx.el.a(
            "Sign in",
            href="/login",
            class_name="font-semibold text-blue-600 hover:text-blue-700",
        ),
        class_name="text-center text-sm text-gray-600 mt-6",
    )
    return auth_shell(
        "Create Your Account", "Join MediCare Hospital Management", form, footer
    )
