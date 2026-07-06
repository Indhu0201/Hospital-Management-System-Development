import reflex as rx
from app.components.landing import landing_page
from app.components.auth_forms import login_form, register_form
from app.components.dashboards import (
    admin_dashboard,
    doctor_dashboard,
    nurse_dashboard,
    patient_dashboard,
)


def index() -> rx.Component:
    return landing_page()


def login() -> rx.Component:
    return login_form()


def register() -> rx.Component:
    return register_form()


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(register, route="/register")
app.add_page(admin_dashboard, route="/dashboard/admin")
app.add_page(doctor_dashboard, route="/dashboard/doctor")
app.add_page(nurse_dashboard, route="/dashboard/nurse")
app.add_page(patient_dashboard, route="/dashboard/patient")
