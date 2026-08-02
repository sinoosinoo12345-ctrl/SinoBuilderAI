import 'package:go_router/go_router.dart';

import '../features/home/home_screen.dart';
import '../features/dashboard/dashboard_screen.dart';
import '../features/settings/settings_screen.dart';

final appRouter = GoRouter(

  initialLocation: "/",

  routes: [

    GoRoute(

      path: "/",

      builder: (context, state) => const HomeScreen(),

    ),

    GoRoute(

      path: "/dashboard",

      builder: (context, state) => const DashboardScreen(),

    ),

    GoRoute(

      path: "/settings",

      builder: (context, state) => const SettingsScreen(),

    ),

  ],

);
