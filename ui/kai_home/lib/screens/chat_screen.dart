import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() =>
      _ChatScreenState();
}

class _ChatScreenState
    extends State<ChatScreen> {

  String kaiMessage =
      "Good evening, Commander.\n\nWhat shall we accomplish today?";

  bool isLoading = false;

  final TextEditingController
      messageController =
          TextEditingController();

  Future<void> sendMessage() async {

    final message =
        messageController.text.trim();

    if (message.isEmpty) return;

    messageController.clear();

    setState(() {
      isLoading = true;
    });

    try {

      final response =
          await ApiService.sendMessage(
        message,
      );

      setState(() {
        kaiMessage = response;
        isLoading = false;
      });

    } catch (e) {

      setState(() {
        kaiMessage =
            "Connection error.\n$e";
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {

    final h =
        MediaQuery.of(context).size.height;

    final w =
        MediaQuery.of(context).size.width;

    return Scaffold(
      backgroundColor:
          const Color(0xFF080D16),

      body: Stack(
        children: [

          // ==========================
          // BACKGROUND
          // ==========================

          Positioned.fill(
            child: Image.asset(
              'assets/images/home_bg.png',
              fit: BoxFit.cover,
            ),
          ),

          Positioned.fill(
            child: Container(
              color: Colors.black.withOpacity(
                0.60,
              ),
            ),
          ),

          // ==========================
          // BRONZE GLOW
          // ==========================

          Positioned(
            top: 40,
            left: 0,
            right: 0,
            child: Center(
              child: Container(
                width: 600,
                height: 600,

                decoration: BoxDecoration(
                  shape: BoxShape.circle,

                  boxShadow: [
                    BoxShadow(
                      color: const Color(
                        0xFFB08D57,
                      ).withOpacity(0.12),

                      blurRadius: 220,
                      spreadRadius: 60,
                    ),
                  ],
                ),
              ),
            ),
          ),

          // ==========================
          // HUD
          // ==========================

          const Positioned(
            top: 40,
            left: 50,

            child: Column(
              crossAxisAlignment:
                  CrossAxisAlignment.start,

              children: [

                Text(
                  "KAI",

                  style: TextStyle(
                    color:
                        Color(0xFFD8B273),

                    fontSize: 32,
                    letterSpacing: 8,
                    fontWeight:
                        FontWeight.w300,
                  ),
                ),

                SizedBox(height: 8),

                Text(
                  "ONLINE ●",

                  style: TextStyle(
                    color:
                        Colors.white70,

                    fontSize: 12,
                    letterSpacing: 3,
                  ),
                ),

                SizedBox(height: 3),

                Text(
                  "EXECUTIVE AI",

                  style: TextStyle(
                    color:
                        Colors.white38,

                    fontSize: 10,
                    letterSpacing: 3,
                  ),
                ),
              ],
            ),
          ),

          // ==========================
          // KAI
          // ==========================

          Positioned(
            top: 10,
            left: 0,
            right: 0,

            child: Center(
              child: Image.asset(
                'assets/images/kai_chat.png',

                height: h * 0.72,
                fit: BoxFit.contain,
              ),
            ),
          ),

          // ==========================
          // DIALOGUE PANEL
          // ==========================

          Positioned(
            left: w * 0.06,
            right: w * 0.06,
            bottom: 110,

            child: SizedBox(
              height: 170,

              child: Stack(
                clipBehavior: Clip.none,

                children: [

                  Positioned.fill(
                    child: Image.asset(
                      'assets/images/dialogue_panel.png',
                      fit: BoxFit.fill,
                    ),
                  ),

                  Positioned(
                    top: -25,
                    left: 30,

                    child: Image.asset(
                      'assets/images/divider.png',
                      width: 200,
                    ),
                  ),

                  Positioned(
                    right: 65,
                    top: 18,

                    child: Opacity(
                      opacity: 0.12,

                      child: Image.asset(
                        'assets/images/emblem.png',
                        width: 120,
                      ),
                    ),
                  ),

                  const Positioned(
                    left: 55,
                    top: 18,

                    child: Text(
                      "KAI",

                      style: TextStyle(
                        color:
                            Color(0xFFD8B273),

                        fontSize: 20,
                        letterSpacing: 4,
                        fontWeight:
                            FontWeight.w300,
                      ),
                    ),
                  ),

                  Positioned(
                    left: 55,
                    top: 55,

                    child: SizedBox(
                      width: 700,

                      child: Text(
                        isLoading
                            ? "Kai is thinking..."
                            : kaiMessage,

                        style:
                            const TextStyle(
                          color:
                              Colors.white,

                          fontSize: 14,
                          height: 1.5,

                          fontWeight:
                              FontWeight.w300,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),

          // ==========================
          // COMMAND BAR
          // ==========================

          Positioned(
            left: w * 0.08,
            right: w * 0.08,
            bottom: 25,

            child: Container(
              height: 60,

              decoration: BoxDecoration(
                color:
                    const Color(0xFF0E121A),

                borderRadius:
                    BorderRadius.circular(
                  12,
                ),

                border: Border.all(
                  color:
                      const Color(
                    0xFFB08D57,
                  ),
                  width: 1,
                ),
              ),

              child: Row(
                children: [

                  const SizedBox(
                    width: 20,
                  ),

                  Expanded(
                    child: TextField(
                      controller:
                          messageController,

                      style:
                          const TextStyle(
                        color:
                            Colors.white,

                        fontSize: 15,
                      ),

                      onSubmitted: (_) {
                        sendMessage();
                      },

                      decoration:
                          const InputDecoration(
                        border:
                            InputBorder.none,

                        hintText:
                            "Enter your command...",

                        hintStyle:
                            TextStyle(
                          color:
                              Colors.white38,
                        ),
                      ),
                    ),
                  ),

                  Container(
                    width: 50,
                    height: 50,

                    margin:
                        const EdgeInsets.only(
                      right: 8,
                    ),

                    decoration:
                        BoxDecoration(
                      shape:
                          BoxShape.circle,

                      border:
                          Border.all(
                        color:
                            const Color(
                          0xFFB08D57,
                        ),
                      ),
                    ),

                    child: IconButton(
                      onPressed:
                          sendMessage,

                      icon: const Icon(
                        Icons.arrow_forward,

                        color:
                            Color(
                          0xFFD8B273,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
