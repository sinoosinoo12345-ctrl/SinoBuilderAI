import 'package:dio/dio.dart';

final Dio api = Dio(

  BaseOptions(

    connectTimeout: const Duration(seconds: 30),

    receiveTimeout: const Duration(seconds: 30),

    headers: {

      "Accept": "application/json",

    },

  ),

);
