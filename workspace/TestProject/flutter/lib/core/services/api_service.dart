import '../core/network/api.dart';

class ApiService {

  Future<dynamic> get(String url) async {

    final response = await api.get(url);

    return response.data;

  }

}
