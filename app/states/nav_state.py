import reflex as rx


class NavState(rx.State):
    sidebar_open: bool = False
    notifications_open: bool = False
    search_query: str = ""

    notifications: list[dict[str, str]] = [
        {
            "title": "New appointment request",
            "time": "5 min ago",
            "type": "appointment",
        },
        {"title": "Lab results ready", "time": "1 hour ago", "type": "lab"},
        {
            "title": "Prescription updated",
            "time": "2 hours ago",
            "type": "prescription",
        },
        {
            "title": "New patient assigned",
            "time": "3 hours ago",
            "type": "patient",
        },
    ]

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @rx.event
    def close_sidebar(self):
        self.sidebar_open = False

    @rx.event
    def toggle_notifications(self):
        self.notifications_open = not self.notifications_open

    @rx.event
    def set_search(self, value: str):
        self.search_query = value
