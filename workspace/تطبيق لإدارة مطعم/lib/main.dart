import 'package:flutter/material.dart';

void main() {
  runApp(const SinoApp());
}

class SinoApp extends StatelessWidget {
  const SinoApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Sino Builder AI',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Sino Builder AI'),
        ),
        body: const Center(
          child: Text(
            'Project Generated Successfully',
          ),
        ),
      ),
    );
  }
}