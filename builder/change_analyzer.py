from __future__ import annotations


class ChangeAnalyzer:
    """
    Analyzes user requirements
    and decides affected project files.
    """


    def analyze(
        self,
        request: str,
    ) -> list[str]:

        text = (
            request
            .lower()
            .replace("أ", "ا")
            .replace("إ", "ا")
            .replace("آ", "ا")
            .replace("ة", "ه")
        )


        rules = {

            # Restaurant system

            (
                "مطعم",
                "طلبات",
                "طلب",
                "وجبات",
                "طعام",
                "قائمة",
                "menu",
                "restaurant",
                "food",
            ): [

                "backend/main.py",
                "backend/orders.py",
                "database/models.py",
                "database/database.py",
                "frontend/lib/main.dart",
                "frontend/lib/screens/orders.dart",

            ],


            # Payment systems

            (
                "دفع",
                "فاتوره",
                "فاتورة",
                "payment",
                "invoice",

            ): [

                "backend/main.py",
                "database/models.py",
                "frontend/lib/main.dart",

            ],


            # Authentication

            (
                "مستخدم",
                "مستخدمين",
                "دخول",
                "login",
                "auth",

            ): [

                "backend/auth.py",
                "database/models.py",
                "frontend/lib/login.dart",

            ],


            # Notifications

            (
                "اشعار",
                "اشعارات",
                "تنبيه",
                "notification",

            ): [

                "backend/notifications.py",
                "database/models.py",
                "frontend/lib/notifications.dart",

            ],


            # Dashboard

            (
                "تقارير",
                "احصائيات",
                "dashboard",
                "analytics",

            ): [

                "backend/reports.py",
                "frontend/lib/dashboard.dart",

            ],


            # Settings

            (
                "اعداد",
                "اعدادات",
                "settings",

            ): [

                "frontend/lib/settings.dart",

            ],
        }


        files = set()


        for keywords, affected in rules.items():

            if any(
                word in text
                for word in keywords
            ):

                files.update(
                    affected
                )


        if not files:

            files.add(
                "README.md"
            )


        return list(files)
