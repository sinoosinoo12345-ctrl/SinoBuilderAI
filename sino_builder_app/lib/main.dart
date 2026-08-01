import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(const SinoBuilderAI());
}

class SinoBuilderAI extends StatelessWidget {
  const SinoBuilderAI({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SinoHome(),
    );
  }
}

class SinoHome extends StatefulWidget {
  const SinoHome({super.key});

  @override
  State<SinoHome> createState() => _SinoHomeState();
}

class _SinoHomeState extends State<SinoHome> {
  late final WebViewController controller;

  @override
  void initState() {
    super.initState();

    controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..loadFlutterAsset('assets/frontend/index.html');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: WebViewWidget(controller: controller),
      ),
    );
  }
}
