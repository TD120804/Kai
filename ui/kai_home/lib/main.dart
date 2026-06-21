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
    final screenHeight = MediaQuery.of(context).size.height;
    final screenWidth = MediaQuery.of(context).size.width;

    return Scaffold(
      body: Stack(
        children: [

          /// BACKGROUND
          Positioned.fill(
            child: Image.asset(
              'assets/images/home_bg.png',
              fit: BoxFit.cover,
            ),
          ),

          /// DARK OVERLAY
          Positioned.fill(
            child: Container(
              decoration: const BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    Color.fromARGB(70, 0, 0, 0),
                    Color.fromARGB(130, 0, 0, 0),
                    Color.fromARGB(220, 0, 0, 0),
                  ],
                ),
              ),
            ),
          ),

          /// MENU BUTTON
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.only(
                left: 24,
                top: 10,
              ),
              child: Align(
                alignment: Alignment.topLeft,
                child: Image.asset(
                  'assets/images/menu_icon.png',
                  width: 42,
                  height: 42,
                ),
              ),
            ),
          ),

          /// SETTINGS ICON
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.only(
                right: 24,
                top: 10,
              ),
              child: Align(
                alignment: Alignment.topRight,
                child: Icon(
                  Icons.auto_awesome,
                  color: Colors.white.withOpacity(0.9),
                  size: 30,
                ),
              ),
            ),
          ),

          /// EMBLEM
          Positioned(
            top: 70,
            left: 0,
            right: 0,
            child: Center(
              child: Image.asset(
                'assets/images/emblem.png',
                width: 90,
              ),
            ),
          ),

          /// KAI
          Positioned(
            bottom: 220,
            left: 0,
            right: 0,
            child: Center(
              child: Image.asset(
                'assets/images/kai_home.png',
                height: screenHeight * 0.58,
              ),
            ),
          ),

          /// TALK RING
          Positioned(
            bottom: 90,
            left: 0,
            right: 0,
            child: Center(
              child: GestureDetector(
                onTap: () {
                  debugPrint("Talk To Kai");
                },
                child: SizedBox(
                  width: 230,
                  height: 230,
                  child: Stack(
                    alignment: Alignment.center,
                    children: [

                      Image.asset(
                        'assets/images/talk_ring.png',
                        width: 230,
                      ),

                      Column(
                        mainAxisSize: MainAxisSize.min,
                        children: const [

                          SizedBox(height: 15),

                          Text(
                            "TALK TO KAI",
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 22,
                              letterSpacing: 3,
                              fontWeight: FontWeight.w300,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),

          /// DIVIDER
          Positioned(
            bottom: 35,
            left: 0,
            right: 0,
            child: Center(
              child: Image.asset(
                'assets/images/divider.png',
                width: screenWidth * 0.75,
              ),
            ),
          ),
        ],
      ),
    );
  }
}