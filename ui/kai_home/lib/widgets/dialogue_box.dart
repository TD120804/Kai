import 'package:flutter/material.dart';

class DialogueBox extends StatelessWidget {
  final String speaker;
  final String message;

  const DialogueBox({
    super.key,
    required this.speaker,
    required this.message,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,

      padding: const EdgeInsets.all(24),

      decoration: BoxDecoration(
        color: Colors.black.withOpacity(0.35),

        borderRadius:
            BorderRadius.circular(12),

        border: Border.all(
          color: const Color(
            0xFFD8B273,
          ),
          width: 1.5,
        ),
      ),

      child: Column(
        crossAxisAlignment:
            CrossAxisAlignment.start,

        mainAxisSize: MainAxisSize.min,

        children: [

          Text(
            speaker.toUpperCase(),

            style: const TextStyle(
              color: Color(0xFFD8B273),
              fontSize: 18,
              letterSpacing: 4,
              fontWeight:
                  FontWeight.w300,
            ),
          ),

          const SizedBox(height: 16),

          Text(
            message,

            style: const TextStyle(
              color: Colors.white,
              fontSize: 20,
              height: 1.6,
              fontWeight:
                  FontWeight.w300,
            ),
          ),

          const SizedBox(height: 16),

          const Align(
            alignment:
                Alignment.bottomRight,

            child: Icon(
              Icons.keyboard_arrow_down,
              color: Color(
                0xFFD8B273,
              ),
            ),
          ),
        ],
      ),
    );
  }
}