import reflex as rx


def feature_card(icon: str, title: str, desc: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-6 w-6 text-{color}-600"),
            class_name=f"w-12 h-12 rounded-xl bg-{color}-100 flex items-center justify-center mb-4",
        ),
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-900 mb-2"),
        rx.el.p(desc, class_name="text-sm text-gray-600 leading-relaxed"),
        class_name="bg-white/70 backdrop-blur-sm p-6 rounded-2xl border border-white/60 shadow-sm hover:shadow-lg transition-all duration-300 hover:-translate-y-1",
    )


def stat_item(number: str, label: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            number, class_name="text-3xl md:text-4xl font-bold text-blue-600"
        ),
        rx.el.p(label, class_name="text-sm text-gray-600 font-medium mt-1"),
        class_name="text-center",
    )


def landing_nav() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("heart-pulse", class_name="h-6 w-6 text-white"),
                    class_name="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-md",
                ),
                rx.el.span(
                    "MediCare", class_name="text-xl font-bold text-gray-900"
                ),
                rx.el.span(
                    "HMS",
                    class_name="text-xs font-semibold text-blue-600 bg-blue-100 px-2 py-0.5 rounded-full ml-1",
                ),
                href="/",
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.a(
                    "Features",
                    href="#features",
                    class_name="text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors",
                ),
                rx.el.a(
                    "About",
                    href="#about",
                    class_name="text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors",
                ),
                rx.el.a(
                    "Contact",
                    href="#contact",
                    class_name="text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors",
                ),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.div(
                rx.el.a(
                    "Sign In",
                    href="/login",
                    class_name="px-4 py-2 text-sm font-semibold text-blue-600 hover:text-blue-700 transition-colors",
                ),
                rx.el.a(
                    "Get Started",
                    href="/register",
                    class_name="px-5 py-2 text-sm font-semibold bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-all shadow-sm hover:shadow-md",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16",
        ),
        class_name="fixed top-0 inset-x-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-100",
    )


def landing_page() -> rx.Component:
    return rx.el.div(
        landing_nav(),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "shield-check", class_name="h-4 w-4 text-blue-600"
                        ),
                        rx.el.span(
                            "Trusted by 500+ Hospitals",
                            class_name="text-xs font-semibold text-blue-700",
                        ),
                        class_name="inline-flex items-center gap-2 bg-blue-50 border border-blue-100 px-3 py-1.5 rounded-full mb-6",
                    ),
                    rx.el.h1(
                        "Modern Healthcare",
                        rx.el.br(),
                        rx.el.span(
                            "Management System", class_name="text-blue-600"
                        ),
                        class_name="text-4xl md:text-6xl font-bold text-gray-900 leading-tight tracking-tight",
                    ),
                    rx.el.p(
                        "Streamline your hospital operations with our comprehensive platform. Manage patients, doctors, nurses, appointments, and clinical workflows all in one secure place.",
                        class_name="text-lg text-gray-600 mt-6 leading-relaxed max-w-xl",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Get Started Free",
                            rx.icon("arrow-right", class_name="h-4 w-4"),
                            href="/register",
                            class_name="inline-flex items-center gap-2 px-6 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition-all shadow-md hover:shadow-lg",
                        ),
                        rx.el.a(
                            rx.icon("play", class_name="h-4 w-4"),
                            "Sign In",
                            href="/login",
                            class_name="inline-flex items-center gap-2 px-6 py-3 bg-white text-gray-800 font-semibold rounded-xl border border-gray-200 hover:border-blue-300 hover:text-blue-600 transition-all",
                        ),
                        class_name="flex flex-wrap gap-3 mt-8",
                    ),
                    rx.el.div(
                        stat_item("50K+", "Patients"),
                        stat_item("2K+", "Doctors"),
                        stat_item("500+", "Hospitals"),
                        stat_item("99.9%", "Uptime"),
                        class_name="grid grid-cols-2 md:grid-cols-4 gap-6 mt-12 pt-12 border-t border-gray-100",
                    ),
                    class_name="max-w-2xl",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "activity",
                                    class_name="h-5 w-5 text-blue-600",
                                ),
                                rx.el.span(
                                    "Live Dashboard",
                                    class_name="text-sm font-semibold text-gray-700",
                                ),
                                rx.el.span(
                                    rx.el.span(
                                        class_name="w-2 h-2 rounded-full bg-green-500 animate-pulse"
                                    ),
                                    "Online",
                                    class_name="ml-auto flex items-center gap-1.5 text-xs font-semibold text-green-600",
                                ),
                                class_name="flex items-center gap-2 pb-4 border-b border-gray-100",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "users",
                                            class_name="h-4 w-4 text-blue-600",
                                        ),
                                        class_name="w-8 h-8 rounded-lg bg-blue-100 flex items-center justify-center",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Total Patients",
                                            class_name="text-xs text-gray-500",
                                        ),
                                        rx.el.p(
                                            "1,284",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                    ),
                                    class_name="flex items-center gap-3 p-3 bg-blue-50/50 rounded-xl",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "stethoscope",
                                            class_name="h-4 w-4 text-emerald-600",
                                        ),
                                        class_name="w-8 h-8 rounded-lg bg-emerald-100 flex items-center justify-center",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Active Doctors",
                                            class_name="text-xs text-gray-500",
                                        ),
                                        rx.el.p(
                                            "87",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                    ),
                                    class_name="flex items-center gap-3 p-3 bg-emerald-50/50 rounded-xl",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "calendar-check",
                                            class_name="h-4 w-4 text-purple-600",
                                        ),
                                        class_name="w-8 h-8 rounded-lg bg-purple-100 flex items-center justify-center",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Appointments Today",
                                            class_name="text-xs text-gray-500",
                                        ),
                                        rx.el.p(
                                            "142",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                    ),
                                    class_name="flex items-center gap-3 p-3 bg-purple-50/50 rounded-xl",
                                ),
                                class_name="grid gap-3 mt-4",
                            ),
                            class_name="bg-white rounded-2xl p-5 shadow-xl border border-white/60",
                        ),
                        class_name="relative",
                    ),
                    rx.el.div(
                        class_name="absolute -top-8 -right-8 w-64 h-64 bg-blue-200/40 rounded-full blur-3xl -z-10",
                    ),
                    rx.el.div(
                        class_name="absolute -bottom-8 -left-8 w-64 h-64 bg-cyan-200/40 rounded-full blur-3xl -z-10",
                    ),
                    class_name="relative hidden lg:block",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid lg:grid-cols-2 gap-12 items-center pt-32 pb-20",
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "FEATURES",
                        class_name="text-xs font-bold text-blue-600 tracking-widest mb-3",
                    ),
                    rx.el.h2(
                        "Everything You Need in One Place",
                        class_name="text-3xl md:text-4xl font-bold text-gray-900",
                    ),
                    rx.el.p(
                        "Powerful tools built for modern healthcare teams",
                        class_name="text-lg text-gray-600 mt-3",
                    ),
                    class_name="text-center max-w-2xl mx-auto mb-12",
                ),
                rx.el.div(
                    feature_card(
                        "users",
                        "Patient Management",
                        "Complete patient records, medical history, and appointment tracking in one secure system.",
                        "blue",
                    ),
                    feature_card(
                        "stethoscope",
                        "Doctor Portal",
                        "Empower doctors with diagnosis tools, prescription management, and clinical workflows.",
                        "emerald",
                    ),
                    feature_card(
                        "heart-pulse",
                        "Nurse Dashboard",
                        "Track vitals, manage medication schedules, and coordinate patient care efficiently.",
                        "rose",
                    ),
                    feature_card(
                        "shield-check",
                        "Admin Control",
                        "Comprehensive administration with analytics, reports, and system-wide management.",
                        "purple",
                    ),
                    feature_card(
                        "calendar",
                        "Smart Scheduling",
                        "Intelligent appointment booking with automated reminders and conflict detection.",
                        "amber",
                    ),
                    feature_card(
                        "file-text",
                        "Digital Records",
                        "Secure electronic health records with easy access and HIPAA-compliant storage.",
                        "cyan",
                    ),
                    class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-6",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
            ),
            id="features",
            class_name="bg-gradient-to-b from-white to-blue-50/50",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Ready to Transform Your Hospital?",
                        class_name="text-3xl md:text-4xl font-bold text-white",
                    ),
                    rx.el.p(
                        "Join hundreds of hospitals using MediCare to deliver better patient care.",
                        class_name="text-blue-100 mt-3 text-lg",
                    ),
                    rx.el.a(
                        "Create Free Account",
                        rx.icon("arrow-right", class_name="h-4 w-4"),
                        href="/register",
                        class_name="inline-flex items-center gap-2 mt-8 px-6 py-3 bg-white text-blue-600 font-semibold rounded-xl hover:bg-blue-50 transition-all shadow-lg",
                    ),
                    class_name="text-center",
                ),
                class_name="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
            ),
            class_name="bg-gradient-to-br from-blue-600 to-blue-800",
        ),
        rx.el.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "heart-pulse", class_name="h-5 w-5 text-blue-600"
                        ),
                        rx.el.span(
                            "MediCare HMS", class_name="font-bold text-gray-900"
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "© 2024 MediCare Hospital Management System. All rights reserved.",
                        class_name="text-sm text-gray-500 mt-2",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center",
            ),
            class_name="bg-white border-t border-gray-100",
        ),
        class_name="min-h-screen bg-gradient-to-b from-blue-50/40 via-white to-white font-['Inter']",
    )
