import reflex as rx
from app.states.auth_state import AuthState
from app.states.nav_state import NavState


NAV_ITEMS = {
    "admin": [
        ("Overview", "layout-dashboard", "/dashboard/admin"),
        ("Doctors", "stethoscope", "/dashboard/admin"),
        ("Nurses", "heart-pulse", "/dashboard/admin"),
        ("Patients", "users", "/dashboard/admin"),
        ("Appointments", "calendar", "/dashboard/admin"),
        ("Departments", "building-2", "/dashboard/admin"),
        ("Reports", "file-text", "/dashboard/admin"),
        ("Settings", "settings", "/dashboard/admin"),
    ],
    "doctor": [
        ("Overview", "layout-dashboard", "/dashboard/doctor"),
        ("My Patients", "users", "/dashboard/doctor"),
        ("Appointments", "calendar", "/dashboard/doctor"),
        ("Prescriptions", "pill", "/dashboard/doctor"),
        ("Medical Notes", "clipboard-list", "/dashboard/doctor"),
        ("Nurses", "heart-pulse", "/dashboard/doctor"),
        ("Schedule", "clock", "/dashboard/doctor"),
    ],
    "nurse": [
        ("Overview", "layout-dashboard", "/dashboard/nurse"),
        ("Assigned Patients", "users", "/dashboard/nurse"),
        ("Daily Tasks", "list-checks", "/dashboard/nurse"),
        ("Medications", "pill", "/dashboard/nurse"),
        ("Vitals", "activity", "/dashboard/nurse"),
        ("Notes", "clipboard-list", "/dashboard/nurse"),
    ],
    "patient": [
        ("Overview", "layout-dashboard", "/dashboard/patient"),
        ("Appointments", "calendar", "/dashboard/patient"),
        ("My Doctor", "stethoscope", "/dashboard/patient"),
        ("Prescriptions", "pill", "/dashboard/patient"),
        ("Medical History", "file-text", "/dashboard/patient"),
        ("Notifications", "bell", "/dashboard/patient"),
    ],
}


def sidebar_item(
    label: str, icon: str, href: str, active: bool = False
) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-4 w-4"),
        rx.el.span(label, class_name="text-sm font-medium"),
        href=href,
        class_name=(
            "flex items-center gap-3 px-3 py-2.5 rounded-xl text-blue-700 bg-blue-50 transition-all"
            if active
            else "flex items-center gap-3 px-3 py-2.5 rounded-xl text-gray-600 hover:bg-blue-50 hover:text-blue-700 transition-all"
        ),
    )


def render_nav_items(role: str) -> rx.Component:
    items = NAV_ITEMS.get(role, [])
    return rx.el.nav(
        *[
            sidebar_item(label, icon, href, i == 0)
            for i, (label, icon, href) in enumerate(items)
        ],
        class_name="flex flex-col gap-1 flex-1",
    )


def sidebar_content(role: str, role_label: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("heart-pulse", class_name="h-5 w-5 text-white"),
                    class_name="w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-md",
                ),
                rx.el.div(
                    rx.el.p(
                        "MediCare",
                        class_name="font-bold text-gray-900 text-sm leading-tight",
                    ),
                    rx.el.p("HMS Platform", class_name="text-xs text-gray-500"),
                ),
                href="/",
                class_name="flex items-center gap-2.5",
            ),
            class_name="h-16 flex items-center px-5 border-b border-gray-100",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "MAIN MENU",
                    class_name="text-[10px] font-bold text-gray-400 tracking-widest px-3 mb-2",
                ),
                render_nav_items(role),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            AuthState.user_name,
                            class_name="text-sm font-semibold text-gray-900 truncate",
                        ),
                        rx.el.p(
                            role_label,
                            class_name="text-xs text-blue-600 font-medium capitalize",
                        ),
                    ),
                    rx.el.button(
                        rx.icon("log-out", class_name="h-4 w-4"),
                        on_click=AuthState.logout,
                        class_name="ml-auto p-2 text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-lg transition-all",
                        title="Logout",
                    ),
                    class_name="flex items-center gap-2 p-3 bg-blue-50/50 rounded-xl border border-blue-100",
                ),
                class_name="pt-4 border-t border-gray-100 mt-4",
            ),
            class_name="flex-1 flex flex-col p-4 overflow-y-auto",
        ),
        class_name="h-full flex flex-col bg-white",
    )


def sidebar(role: str, role_label: str) -> rx.Component:
    return rx.el.div(
        rx.el.aside(
            sidebar_content(role, role_label),
            class_name="hidden lg:flex flex-col w-64 h-screen border-r border-gray-100 sticky top-0 shrink-0 bg-white",
        ),
        rx.cond(
            NavState.sidebar_open,
            rx.el.div(
                rx.el.div(
                    on_click=NavState.close_sidebar,
                    class_name="fixed inset-0 bg-black/40 z-40 lg:hidden",
                ),
                rx.el.aside(
                    sidebar_content(role, role_label),
                    class_name="fixed top-0 left-0 h-screen w-64 z-50 lg:hidden shadow-2xl",
                ),
            ),
            rx.el.div(),
        ),
    )


def notification_item(title: str, time: str, ntype: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("bell", class_name="h-4 w-4 text-blue-600"),
            class_name="w-8 h-8 rounded-lg bg-blue-100 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium text-gray-900"),
            rx.el.p(time, class_name="text-xs text-gray-500 mt-0.5"),
        ),
        class_name="flex items-start gap-3 p-3 hover:bg-gray-50 rounded-xl transition-colors cursor-pointer",
    )


def topbar(title: str) -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon("menu", class_name="h-5 w-5"),
                on_click=NavState.toggle_sidebar,
                class_name="lg:hidden p-2 text-gray-600 hover:bg-gray-100 rounded-lg",
            ),
            rx.el.div(
                rx.el.h1(title, class_name="text-lg font-bold text-gray-900"),
                rx.el.p(
                    "Welcome back to your dashboard",
                    class_name="text-xs text-gray-500 hidden sm:block",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        placeholder="Search patients, doctors, records...",
                        default_value=NavState.search_query,
                        on_change=NavState.set_search.debounce(300),
                        class_name="w-full pl-10 pr-4 py-2 bg-gray-50 border border-gray-200 rounded-xl text-sm placeholder-gray-400 focus:outline-hidden focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all",
                    ),
                    class_name="relative hidden md:block w-72",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("bell", class_name="h-5 w-5"),
                        rx.el.span(
                            "4",
                            class_name="absolute top-1 right-1 w-4 h-4 rounded-full bg-red-500 text-white text-[10px] font-bold flex items-center justify-center",
                        ),
                        on_click=NavState.toggle_notifications,
                        class_name="relative p-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors",
                    ),
                    rx.cond(
                        NavState.notifications_open,
                        rx.el.div(
                            rx.el.div(
                                rx.el.p(
                                    "Notifications",
                                    class_name="font-semibold text-gray-900",
                                ),
                                rx.el.span(
                                    "4 new",
                                    class_name="text-xs bg-blue-100 text-blue-700 px-2 py-0.5 rounded-full font-semibold",
                                ),
                                class_name="flex items-center justify-between p-4 border-b border-gray-100",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    NavState.notifications,
                                    lambda n: notification_item(
                                        n["title"], n["time"], n["type"]
                                    ),
                                ),
                                class_name="p-2 max-h-80 overflow-y-auto",
                            ),
                            class_name="absolute right-0 top-full mt-2 w-80 bg-white rounded-2xl shadow-xl border border-gray-100 z-40",
                        ),
                        rx.el.div(),
                    ),
                    class_name="relative",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            AuthState.user_name.length() > 0,
                            class_name="hidden",
                        ),
                        rx.icon("user", class_name="h-4 w-4 text-white"),
                        class_name="w-9 h-9 rounded-full bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-sm",
                    ),
                    rx.el.div(
                        rx.el.p(
                            AuthState.user_name,
                            class_name="text-sm font-semibold text-gray-900 leading-tight",
                        ),
                        rx.el.p(
                            AuthState.user_role,
                            class_name="text-xs text-gray-500 capitalize",
                        ),
                        class_name="hidden sm:block",
                    ),
                    class_name="flex items-center gap-2 pl-3 border-l border-gray-200",
                ),
                class_name="flex items-center gap-3 ml-auto",
            ),
            class_name="flex items-center gap-4 h-16 px-4 md:px-6",
        ),
        class_name="sticky top-0 z-30 bg-white/80 backdrop-blur-md border-b border-gray-100",
    )


def app_shell(
    role: str, role_label: str, title: str, content: rx.Component
) -> rx.Component:
    return rx.el.div(
        sidebar(role, role_label),
        rx.el.div(
            topbar(title),
            rx.el.main(
                content,
                class_name="p-4 md:p-6 lg:p-8",
            ),
            class_name="flex-1 min-w-0 flex flex-col",
        ),
        class_name="flex min-h-screen bg-gradient-to-br from-blue-50/30 via-white to-cyan-50/30 font-['Inter']",
    )
