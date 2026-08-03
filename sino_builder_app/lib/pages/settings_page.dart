import 'package:flutter/material.dart';

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff0f172a),
      appBar: AppBar(
        title: const Text("⚙️ Settings"),
        backgroundColor: const Color(0xff111827),
      ),
      body: ListView(
        children: const [
          ListTile(
            leading: Icon(Icons.language),
            title: Text("Language"),
            subtitle: Text("Arabic / English"),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.dark_mode),
            title: Text("Dark Mode"),
            subtitle: Text("Enabled"),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.memory),
            title: Text("AI Engine"),
            subtitle: Text("Sino Brain"),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.security),
            title: Text("Security"),
            subtitle: Text("Sino Cyber AI"),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.info),
            title: Text("Version"),
            subtitle: Text("Sino Builder AI V7"),
          ),
        ],
      ),
    );
  }
}
