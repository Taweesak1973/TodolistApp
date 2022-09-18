import 'package:flutter/material.dart';
//http medthod package
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

class AddPage extends StatefulWidget {
  AddPage({Key? key}) : super(key: key);

  @override
  State<AddPage> createState() => _AddPageState();
}

class _AddPageState extends State<AddPage> {
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('เพิ่มรายการใหม่'),
      ),
      body: ListView(children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextField(
            controller: todo_title,
            autofocus: true,
            keyboardType: TextInputType.text,
            decoration: const InputDecoration(
              labelText: 'รายการที่ต้องทำ',
              border: OutlineInputBorder(),
            ),
          ),
        ),
        const SizedBox(
          height: 20,
        ),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextField(
            minLines: 4,
            maxLines: 8,
            controller: todo_detail,
            autofocus: true,
            keyboardType: TextInputType.text,
            decoration: const InputDecoration(
              labelText: 'รายละเอียด',
              border: OutlineInputBorder(),
            ),
          ),
        ),
        const SizedBox(
          height: 20,
        ),
        Card(
          margin: EdgeInsets.symmetric(vertical: 20, horizontal: 30),
          color: Colors.green,
          child: TextButton(
            onPressed: () {
              setState(() {
                postTodo();
                todo_title.clear();
                todo_detail.clear();
              });
            },
            child: const Text(
              'กดเพิ่มรายการ',
              style: TextStyle(fontSize: 30, color: Colors.white),
            ),
          ),
        ),
      ]),
    );
  }

  Future postTodo() async {
  //  var url = Uri.https('792f-2001-fb1-86-56c-3922-2192-c0fb-369a.ap.ngrok.io',  '/api/post-todolist');
     var url = Uri.http('192.168.1.33:8000', '/api/post-todolist');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}","detail":"${todo_detail.text}"}';
    var response = await http.post(url, headers: header, body: jsondata);
    // print('--------result-------');
    // print(response.body);
  }
}
