import 'dart:convert';

import 'package:http/http.dart' as http;

class KaiApiService {

  // ==================================================
  // CONFIG
  // ==================================================

  static const String _baseUrl =
      "http://127.0.0.1:8000";

  static const Duration _timeout =
      Duration(seconds: 30);

  // ==================================================
  // CHAT
  // ==================================================

  static Future<String> sendMessage(
      String message) async {

    try {

      final response = await http

          .post(

            Uri.parse(
              "$_baseUrl/chat",
            ),

            headers: {

              "Content-Type":
                  "application/json",

            },

            body: jsonEncode({

              "message": message,

            }),

          )

          .timeout(_timeout);

      if (response.statusCode != 200) {

        return "Backend Error (${response.statusCode})";
      }

      final data = jsonDecode(
        response.body,
      );

      return data["response"];

    }

    catch (e) {

      return "Connection Error:\n$e";
    }
  }

  // ==================================================
  // STATUS
  // ==================================================

  static Future<bool> isOnline() async {

    try {

      final response = await http

          .get(
            Uri.parse(_baseUrl),
          )

          .timeout(
            const Duration(
              seconds: 3,
            ),
          );

      return response.statusCode == 200;

    }

    catch (_) {

      return false;
    }
  }

}