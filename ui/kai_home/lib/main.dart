import 'package:flutter/material.dart';

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

class KaiHomeScreen extends StatelessWidget {
const KaiHomeScreen({super.key});

@override
Widget build(BuildContext context) {
final h = MediaQuery.of(context).size.height;
final w = MediaQuery.of(context).size.width;


return Scaffold(
  body: Stack(
    children: [

      // =========================
      // BACKGROUND
      // =========================
      Positioned.fill(
        child: Image.asset(
          'assets/images/home_bg.png',
          fit: BoxFit.cover,
        ),
      ),

      // =========================
      // CINEMATIC OVERLAY
      // =========================
      Positioned.fill(
        child: Container(
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [
                Color.fromARGB(30, 0, 0, 0),
                Color.fromARGB(100, 0, 0, 0),
                Color.fromARGB(220, 0, 0, 0),
              ],
            ),
          ),
        ),
      ),

      // =========================
      // MENU BUTTON
      // =========================
      SafeArea(
        child: Padding(
          padding: const EdgeInsets.only(
            left: 24,
            top: 18,
          ),
          child: Align(
            alignment: Alignment.topLeft,
            child: Image.asset(
              'assets/images/menu_icon.png',
              width: 42,
            ),
          ),
        ),
      ),

      // =========================
      // SETTINGS
      // =========================
      SafeArea(
        child: Padding(
          padding: const EdgeInsets.only(
            right: 24,
            top: 18,
          ),
          child: Align(
            alignment: Alignment.topRight,
            child: Icon(
              Icons.auto_awesome,
              color: Colors.white70,
              size: 30,
            ),
          ),
        ),
      ),

      // =========================
      // EMBLEM
      // =========================
      Positioned(
        top: h * 0.045,
        left: 0,
        right: 0,
        child: Center(
          child: Image.asset(
            'assets/images/emblem.png',
            width: 65,
          ),
        ),
      ),

      // =========================
      // GLOW BEHIND KAI
      // =========================
      Positioned(
        top: h * 0.10,
        left: 0,
        right: 0,
        child: Center(
          child: Container(
            width: 550,
            height: 550,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              boxShadow: [
                BoxShadow(
                  color: const Color(
                    0xFFDCEBFF,
                  ).withOpacity(0.22),
                  blurRadius: 220,
                  spreadRadius: 50,
                ),
              ],
            ),
          ),
        ),
      ),

      // =========================
      // KAI
      // =========================
      Positioned(
        top: h * 0.15,
        left: 0,
        right: 0,
        child: Center(
          child: Image.asset(
            'assets/images/kai_home.png',
            height: h * 1.1,
            fit: BoxFit.contain,
          ),
        ),
      ),

      // =========================
      // DIVIDER
      // =========================
      Positioned(
        bottom: h * 0.35,
        left: 0,
        right: 0,
        child: Center(
          child: Image.asset(
            'assets/images/divider.png',
            width: w * 0.78,
          ),
        ),
      ),

      // =========================
      // TALK BUTTON
      // =========================
      Positioned(
        bottom: h * 0.015,
        left: 0,
        right: 0,
        child: Center(
          child: GestureDetector(
            onTap: () {
              debugPrint("Talk To Kai");
            },
            child: SizedBox(
              width: 250,
              height: 250,
              child: Stack(
                alignment: Alignment.center,
                children: [

                  Image.asset(
                    'assets/images/talk_ring.png',
                    width: 250,
                  ),

                  Text(
                    "TALK TO KAI",
                    style: TextStyle(
                      color: Colors.white.withOpacity(0.95),
                      fontSize: 22,
                      letterSpacing: 3,
                      fontWeight: FontWeight.w300,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    ],
  ),
);
}
}