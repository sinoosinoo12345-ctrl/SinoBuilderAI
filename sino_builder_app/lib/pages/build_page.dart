import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class BuildPage extends StatefulWidget {
  const BuildPage({super.key});

  @override
  State<BuildPage> createState() => _BuildPageState();
}

class _BuildPageState extends State<BuildPage> {
  final nameController = TextEditingController();
  final descriptionController = TextEditingController();

  bool loading = false;
  String status = "";

  Future<void> buildProject() async {
    if (nameController.text.isEmpty ||
        descriptionController.text.isEmpty) {
      return;
    }

    setState(() {
      loading = true;
      status = "🚀 Building project...";
    });

    try {
      final response = await http.post(
        Uri.parse("http://127.0.0.1:8000/build"),
        headers: {
          "Content-Type": "application/json",
        },
        body: jsonEncode({
          "project_name": nameController.text,
          "requirements": descriptionController.text,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);

        setState(() {
          status =
              "✅ Project ${data['project']} generated successfully";
        });
      } else {
        setState(() {
          status = "❌ Build failed: ${response.statusCode}";
        });
      }
    } catch (e) {
      setState(() {
        status = "❌ Connection error: $e";
      });
    }

    setState(() {
      loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff0f172a),
      appBar: AppBar(
        backgroundColor: const Color(0xff111827),
        elevation: 0,
        title: const Text("🚀 Build Project"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(18),
        child: Column(
          children: [
            TextField(
              controller: nameController,
              decoration: InputDecoration(
                labelText: "📦 Project Name",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
              ),
            ),

            const SizedBox(height: 15),

            Expanded(
              child: TextField(
                controller: descriptionController,
                maxLines: null,
                expands: true,
                decoration: InputDecoration(
                  labelText: "📝 Describe your application...",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                ),
              ),
            ),

            const SizedBox(height: 15),

            if (status.isNotEmpty)
              Padding(
                padding: const EdgeInsets.only(bottom: 12),
                child: Text(
                  status,
                  style: const TextStyle(color: Colors.white),
                ),
              ),

            SizedBox(
              width: double.infinity,
              height: 55,
              child: ElevatedButton.icon(
                onPressed: loading ? null : buildProject,
                icon: loading
                    ? const SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(
                          strokeWidth: 2,
                          color: Colors.white,
                        ),
                      )
                    : const Icon(Icons.rocket_launch),
                label: Text(
                  loading
                      ? "⏳ Building..."
                      : "🚀 Build Project",
                  style: const TextStyle(fontSize: 18),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
