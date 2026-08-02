import 'package:flutter/material.dart';

void main() {

  runApp(

    const SinoBuilderApp(),

  );

}

class SinoBuilderApp extends StatelessWidget {

  const SinoBuilderApp({super.key});

  @override

  Widget build(BuildContext context) {

    return MaterialApp(

      debugShowCheckedModeBanner: false,

      title: "{project}",

      home: const Scaffold(

        body: Center(

          child: Text(

            "{project}",

          ),

        ),

      ),

    );

  }

}
