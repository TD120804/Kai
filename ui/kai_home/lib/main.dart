import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const KaiApp());
}

class KaiApp extends StatelessWidget {
  const KaiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Kai',
      theme: ThemeData.dark(),
      home: const KaiHomeScreen(),
    );
  }
}