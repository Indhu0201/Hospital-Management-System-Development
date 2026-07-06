import reflex as rx
from typing import TypedDict


class Department(TypedDict):
    id: int
    name: str
    head: str
    staff_count: int
    beds: int
    status: str


class ActivityLog(TypedDict):
    id: int
    time: str
    user: str
    role: str
    action: str
    target: str
    category: str


class UserAccount(TypedDict):
    id: int
    name: str
    email: str
    role: str
    status: str
    last_login: str


class AdminState(rx.State):
    active_tab: str = "overview"
    search_query: str = ""
    filter_role: str = "all"
    filter_status: str = "all"
    show_add_modal: bool = False
    modal_type: str = ""
    edit_id: int = 0

    departments: list[Department] = [
        {
            "id": 1,
            "name": "Cardiology",
            "head": "Dr. Sarah Rivera",
            "staff_count": 24,
            "beds": 30,
            "status": "Active",
        },
        {
            "id": 2,
            "name": "Neurology",
            "head": "Dr. James Chen",
            "staff_count": 18,
            "beds": 22,
            "status": "Active",
        },
        {
            "id": 3,
            "name": "Pediatrics",
            "head": "Dr. Priya Patel",
            "staff_count": 22,
            "beds": 28,
            "status": "Active",
        },
        {
            "id": 4,
            "name": "Orthopedics",
            "head": "Dr. Marcus Lee",
            "staff_count": 16,
            "beds": 24,
            "status": "Active",
        },
        {
            "id": 5,
            "name": "Dermatology",
            "head": "Dr. Elena Vasquez",
            "staff_count": 12,
            "beds": 10,
            "status": "Active",
        },
        {
            "id": 6,
            "name": "ICU",
            "head": "Dr. Robert Kim",
            "staff_count": 30,
            "beds": 20,
            "status": "Active",
        },
        {
            "id": 7,
            "name": "Emergency",
            "head": "Dr. Maya Singh",
            "staff_count": 28,
            "beds": 15,
            "status": "Active",
        },
        {
            "id": 8,
            "name": "Radiology",
            "head": "Dr. Alan Brooks",
            "staff_count": 14,
            "beds": 0,
            "status": "Maintenance",
        },
    ]

    activity_logs: list[ActivityLog] = [
        {
            "id": 1,
            "time": "2024-11-20 09:42",
            "user": "Dr. Sarah Rivera",
            "role": "Doctor",
            "action": "Prescribed medication",
            "target": "John Anderson",
            "category": "prescription",
        },
        {
            "id": 2,
            "time": "2024-11-20 09:35",
            "user": "Nurse Amelia Foster",
            "role": "Nurse",
            "action": "Recorded vitals",
            "target": "William Zhang",
            "category": "vitals",
        },
        {
            "id": 3,
            "time": "2024-11-20 09:28",
            "user": "Admin",
            "role": "Admin",
            "action": "Added new doctor",
            "target": "Dr. Elena Vasquez",
            "category": "user",
        },
        {
            "id": 4,
            "time": "2024-11-20 09:15",
            "user": "Dr. James Chen",
            "role": "Doctor",
            "action": "Completed appointment",
            "target": "Isabella Nguyen",
            "category": "appointment",
        },
        {
            "id": 5,
            "time": "2024-11-20 08:58",
            "user": "Nurse Rachel Green",
            "role": "Nurse",
            "action": "Administered medicine",
            "target": "Ethan Brooks",
            "category": "medication",
        },
        {
            "id": 6,
            "time": "2024-11-20 08:45",
            "user": "Maria Gonzalez",
            "role": "Patient",
            "action": "Booked appointment",
            "target": "Dr. James Chen",
            "category": "appointment",
        },
        {
            "id": 7,
            "time": "2024-11-20 08:30",
            "user": "Admin",
            "role": "Admin",
            "action": "Updated department",
            "target": "Cardiology",
            "category": "department",
        },
        {
            "id": 8,
            "time": "2024-11-20 08:12",
            "user": "Dr. Priya Patel",
            "role": "Doctor",
            "action": "Added diagnosis",
            "target": "Ethan Brooks",
            "category": "diagnosis",
        },
        {
            "id": 9,
            "time": "2024-11-19 22:14",
            "user": "Admin",
            "role": "Admin",
            "action": "System backup",
            "target": "Database",
            "category": "system",
        },
        {
            "id": 10,
            "time": "2024-11-19 18:03",
            "user": "Nurse Omar Hassan",
            "role": "Nurse",
            "action": "Completed task",
            "target": "Sophia Carter",
            "category": "task",
        },
    ]

    user_accounts: list[UserAccount] = [
        {
            "id": 1,
            "name": "Dr. Sarah Rivera",
            "email": "sarah.rivera@medicare.com",
            "role": "Doctor",
            "status": "Active",
            "last_login": "2024-11-20 09:12",
        },
        {
            "id": 2,
            "name": "Dr. James Chen",
            "email": "james.chen@medicare.com",
            "role": "Doctor",
            "status": "Active",
            "last_login": "2024-11-20 08:45",
        },
        {
            "id": 3,
            "name": "Nurse Amelia Foster",
            "email": "amelia.foster@medicare.com",
            "role": "Nurse",
            "status": "Active",
            "last_login": "2024-11-20 07:30",
        },
        {
            "id": 4,
            "name": "Nurse David Kim",
            "email": "david.kim@medicare.com",
            "role": "Nurse",
            "status": "Active",
            "last_login": "2024-11-19 22:10",
        },
        {
            "id": 5,
            "name": "John Anderson",
            "email": "john.anderson@email.com",
            "role": "Patient",
            "status": "Active",
            "last_login": "2024-11-19 15:22",
        },
        {
            "id": 6,
            "name": "Maria Gonzalez",
            "email": "maria.g@email.com",
            "role": "Patient",
            "status": "Active",
            "last_login": "2024-11-20 08:44",
        },
        {
            "id": 7,
            "name": "Dr. Marcus Lee",
            "email": "marcus.lee@medicare.com",
            "role": "Doctor",
            "status": "Inactive",
            "last_login": "2024-11-15 10:00",
        },
        {
            "id": 8,
            "name": "System Admin",
            "email": "admin@medicare.com",
            "role": "Admin",
            "status": "Active",
            "last_login": "2024-11-20 09:28",
        },
    ]

    appointment_trends: list[dict[str, str | int]] = [
        {"day": "Mon", "scheduled": 42, "completed": 38},
        {"day": "Tue", "scheduled": 55, "completed": 48},
        {"day": "Wed", "scheduled": 48, "completed": 45},
        {"day": "Thu", "scheduled": 62, "completed": 55},
        {"day": "Fri", "scheduled": 58, "completed": 52},
        {"day": "Sat", "scheduled": 35, "completed": 30},
        {"day": "Sun", "scheduled": 24, "completed": 20},
    ]

    _next_dept_id: int = 100
    _next_log_id: int = 100
    _next_user_id: int = 100

    @rx.event
    def set_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def set_search(self, q: str):
        self.search_query = q

    @rx.event
    def set_filter_role(self, r: str):
        self.filter_role = r

    @rx.event
    def set_filter_status(self, s: str):
        self.filter_status = s

    @rx.event
    def open_modal(self, modal_type: str):
        self.modal_type = modal_type
        self.show_add_modal = True
        self.edit_id = 0

    @rx.event
    def close_modal(self):
        self.show_add_modal = False
        self.modal_type = ""
        self.edit_id = 0

    def _log(self, action: str, target: str, category: str):
        self._next_log_id += 1
        self.activity_logs.insert(
            0,
            {
                "id": self._next_log_id,
                "time": "2024-11-20 10:00",
                "user": "Admin",
                "role": "Admin",
                "action": action,
                "target": target,
                "category": category,
            },
        )

    @rx.event
    def add_department(self, form_data: dict):
        name = form_data.get("name", "").strip()
        head = form_data.get("head", "").strip()
        beds = form_data.get("beds", "0").strip()
        if not name or not head:
            return rx.toast("Please fill all fields.", duration=3000)
        self._next_dept_id += 1
        self.departments.append(
            {
                "id": self._next_dept_id,
                "name": name,
                "head": head,
                "staff_count": 0,
                "beds": int(beds) if beds.isdigit() else 0,
                "status": "Active",
            }
        )
        self._log("Added department", name, "department")
        self.show_add_modal = False
        return rx.toast(f"Department '{name}' added.", duration=2500)

    @rx.event
    def delete_department(self, dept_id: int):
        name = ""
        for d in self.departments:
            if d["id"] == dept_id:
                name = d["name"]
        self.departments = [d for d in self.departments if d["id"] != dept_id]
        self._log("Deleted department", name, "department")
        return rx.toast(f"Department '{name}' deleted.", duration=2500)

    @rx.event
    def toggle_department_status(self, dept_id: int):
        for i, d in enumerate(self.departments):
            if d["id"] == dept_id:
                new_status = (
                    "Active" if d["status"] != "Active" else "Maintenance"
                )
                self.departments[i] = {**d, "status": new_status}
                self._log(f"Set {new_status}", d["name"], "department")
                return rx.toast(f"{d['name']} → {new_status}", duration=2000)

    @rx.event
    def add_user(self, form_data: dict):
        name = form_data.get("name", "").strip()
        email = form_data.get("email", "").strip()
        role = form_data.get("role", "Patient").strip()
        if not name or not email:
            return rx.toast("Please fill all fields.", duration=3000)
        self._next_user_id += 1
        self.user_accounts.append(
            {
                "id": self._next_user_id,
                "name": name,
                "email": email,
                "role": role,
                "status": "Active",
                "last_login": "Never",
            }
        )
        self._log(f"Added {role.lower()}", name, "user")
        self.show_add_modal = False
        return rx.toast(f"{role} '{name}' added.", duration=2500)

    @rx.event
    def delete_user(self, user_id: int):
        name = ""
        for u in self.user_accounts:
            if u["id"] == user_id:
                name = u["name"]
        self.user_accounts = [
            u for u in self.user_accounts if u["id"] != user_id
        ]
        self._log("Deleted user", name, "user")
        return rx.toast(f"User '{name}' deleted.", duration=2500)

    @rx.event
    def toggle_user_status(self, user_id: int):
        for i, u in enumerate(self.user_accounts):
            if u["id"] == user_id:
                new_status = "Active" if u["status"] != "Active" else "Inactive"
                self.user_accounts[i] = {**u, "status": new_status}
                self._log(f"Set user {new_status}", u["name"], "user")
                return rx.toast(f"{u['name']} → {new_status}", duration=2000)

    @rx.var
    def filtered_users(self) -> list[UserAccount]:
        q = self.search_query.lower()
        result = self.user_accounts
        if self.filter_role != "all":
            result = [
                u
                for u in result
                if u["role"].lower() == self.filter_role.lower()
            ]
        if self.filter_status != "all":
            result = [
                u
                for u in result
                if u["status"].lower() == self.filter_status.lower()
            ]
        if q:
            result = [
                u
                for u in result
                if q in u["name"].lower()
                or q in u["email"].lower()
                or q in u["role"].lower()
            ]
        return result

    @rx.var
    def filtered_activity_logs(self) -> list[ActivityLog]:
        q = self.search_query.lower()
        if not q:
            return self.activity_logs
        return [
            l
            for l in self.activity_logs
            if q in l["user"].lower()
            or q in l["action"].lower()
            or q in l["target"].lower()
            or q in l["category"].lower()
        ]

    @rx.var
    def filtered_departments(self) -> list[Department]:
        q = self.search_query.lower()
        if not q:
            return self.departments
        return [
            d
            for d in self.departments
            if q in d["name"].lower() or q in d["head"].lower()
        ]

    @rx.var
    def department_distribution(self) -> list[dict[str, str | int]]:
        return [
            {"name": d["name"], "staff": d["staff_count"], "beds": d["beds"]}
            for d in self.departments
        ]

    @rx.var
    def total_departments(self) -> int:
        return len(self.departments)

    @rx.var
    def total_users(self) -> int:
        return len(self.user_accounts)

    @rx.var
    def active_users_count(self) -> int:
        return len([u for u in self.user_accounts if u["status"] == "Active"])
