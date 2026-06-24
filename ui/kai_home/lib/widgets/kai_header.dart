import 'package:flutter/material.dart';

class KaiHeader extends StatelessWidget {
  const KaiHeader({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [

        Text(
          "KAI",
          style: TextStyle(
            color: Color(0xFFD8B273),
            fontSize: 32,
            letterSpacing: 8,
            fontWeight: FontWeight.w300,
          ),
        ),

        SizedBox(height: 6),

        Text(
          "ONLINE ●",
          style: TextStyle(
            color: Colors.white70,
            fontSize: 12,
            letterSpacing: 3,
          ),
        ),
      ],
    );
  }
}