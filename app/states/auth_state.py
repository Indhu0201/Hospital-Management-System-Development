import reflex as rx
import re


class AuthState(rx.State):
    is_authenticated: bool = False
    user_email: str = ""
    user_name: str = ""
    user_role: str = ""
    selected_role: str = "patient"
    login_error: str = ""
    register_error: str = ""
    success_message: str = ""
    show_password: bool = False

    @rx.event
    def set_role(self, role: str):
        self.selected_role = role
        self.login_error = ""
        self.register_error = ""

    @rx.event
    def toggle_password(self):
        self.show_password = not self.show_password

    @rx.event
    def handle_login(self, form_data: dict):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        role = self.selected_role

        if not email or not password:
            self.login_error = "Please fill in all fields."
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.login_error = "Please enter a valid email address."
            return
        if len(password) < 6:
            self.login_error = "Password must be at least 6 characters."
            return

        self.is_authenticated = True
        self.user_email = email
        self.user_name = email.split("@")[0].title()
        self.user_role = role
        self.login_error = ""
        self.success_message = f"Welcome back, {self.user_name}!"
        return rx.redirect(f"/dashboard/{role}")

    @rx.event
    def handle_register(self, form_data: dict):
        name = form_data.get("full_name", "").strip()
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        confirm = form_data.get("confirm_password", "").strip()
        role = self.selected_role

        if not name or not email or not password or not confirm:
            self.register_error = "Please fill in all required fields."
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.register_error = "Please enter a valid email address."
            return
        if len(password) < 6:
            self.register_error = "Password must be at least 6 characters."
            return
        if password != confirm:
            self.register_error = "Passwords do not match."
            return

        self.is_authenticated = True
        self.user_email = email
        self.user_name = name
        self.user_role = role
        self.register_error = ""
        self.success_message = f"Account created! Welcome, {name}."
        return rx.redirect(f"/dashboard/{role}")

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.user_email = ""
        self.user_name = ""
        self.user_role = ""
        self.success_message = ""
        return rx.redirect("/")

    @rx.event
    def check_access(self, required_role: str):
        if not self.is_authenticated:
            return rx.redirect("/login")
        if self.user_role != required_role:
            return rx.redirect(f"/dashboard/{self.user_role}")

    @rx.event
    def require_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/login")
