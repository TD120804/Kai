import 'package:flutter/material.dart';
import 'chat_screen.dart';

class KaiHomeScreen extends StatefulWidget {
  const KaiHomeScreen({super.key});

  @override
  State<KaiHomeScreen> createState() => _KaiHomeScreenState();
}

class _KaiHomeScreenState extends State<KaiHomeScreen> {
  bool _startTransition = false;

  Future<void> _openChat() async {
    setState(() {
      _startTransition = true;
    });

    await Future.delayed(const Duration(milliseconds: 800));

    if (!mounted) return;

    await Navigator.of(context).push(
      PageRouteBuilder(
        transitionDuration: const Duration(milliseconds: 600),

        pageBuilder: (_, _, _) => const ChatScreen(),

        transitionsBuilder: (_, animation, _, child) {
          return FadeTransition(opacity: animation, child: child);
        },
      ),
    );

    if (!mounted) return;

    setState(() {
      _startTransition = false;
    });
  }

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
            child: Image.asset('assets/images/home_bg.png', fit: BoxFit.cover),
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
          // DARKEN ON TRANSITION
          // =========================
          Positioned.fill(
            child: IgnorePointer(
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 700),
                color: _startTransition
                    ? Colors.black.withValues(alpha: 0.45)
                    : Colors.transparent,
              ),
            ),
          ),

          // =========================
          // MENU BUTTON
          // =========================
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.only(left: 24, top: 18),
              child: Align(
                alignment: Alignment.topLeft,
                child: Image.asset('assets/images/menu_icon.png', width: 42),
              ),
            ),
          ),

          // =========================
          // SETTINGS
          // =========================
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.only(right: 24, top: 18),
              child: Align(
                alignment: Alignment.topRight,
                child: const Icon(
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
              child: Image.asset('assets/images/emblem.png', width: 65),
            ),
          ),

          // =========================
          // GLOW
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
                      color: const Color(0xFFDCEBFF).withValues(alpha: 0.22),
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
              child: AnimatedOpacity(
                duration: const Duration(milliseconds: 700),
                opacity: _startTransition ? 0.45 : 1,
                child: Image.asset(
                  'assets/images/kai_home.png',
                  height: h * 1.1,
                  fit: BoxFit.contain,
                ),
              ),
            ),
          ),

          // =========================
          // DIVIDER
          // =========================
          Positioned(
            bottom: h * 0.70,
            left: 0,
            right: 0,
            child: SizedBox(
              width: w,
              height: 80,
              child: Stack(
                alignment: Alignment.center,
                children: [
                  // LEFT SIDE
                  AnimatedPositioned(
                    duration: const Duration(milliseconds: 700),
                    curve: Curves.easeInOutCubic,

                    left: _startTransition ? 20 : w * 0.22,

                    child: Image.asset(
                      'assets/images/divider_left.png',
                      width: 180,
                    ),
                  ),

                  // RIGHT SIDE
                  AnimatedPositioned(
                    duration: const Duration(milliseconds: 700),
                    curve: Curves.easeInOutCubic,

                    right: _startTransition ? 20 : w * 0.22,

                    child: Image.asset(
                      'assets/images/divider_right.png',
                      width: 180,
                    ),
                  ),

                  // CENTER CRYSTAL
                  Image.asset('assets/images/divider_center.png', width: 42),
                ],
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
                onTap: _openChat,

                child: AnimatedScale(
                  duration: const Duration(milliseconds: 300),
                  scale: _startTransition ? 1.08 : 1,

                  child: SizedBox(
                    width: 250,
                    height: 250,
                    child: Stack(
                      alignment: Alignment.center,
                      children: [
                        AnimatedOpacity(
                          duration: const Duration(milliseconds: 500),
                          opacity: _startTransition ? 0.7 : 1,
                          child: Image.asset(
                            'assets/images/talk_ring.png',
                            width: 250,
                          ),
                        ),

                        Text(
                          "TALK TO KAI",
                          style: TextStyle(
                            color: Colors.white.withValues(alpha: 0.95),
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
          ),
        ],
      ),
    );
  }
}
