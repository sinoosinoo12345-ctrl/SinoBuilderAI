import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff0f172a),
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [

              Text(
                "🐉",
                style: TextStyle(
                  fontSize: 70,
                ),
              ),

              SizedBox(height: 20),

              Text(
                "Sino Builder AI",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                ),
              ),

              SizedBox(height: 10),

              Text(
                "Build Professional Applications with AI",
                style: TextStyle(
                  color: Colors.white70,
                  fontSize: 16,
                ),
              ),

            ],
          ),
        ),
      ),
    );
  }
}
