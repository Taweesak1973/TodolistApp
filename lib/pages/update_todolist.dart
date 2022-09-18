import 'package:flutter/material.dart';
//http medthod package
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

class UpdatePage extends StatefulWidget {
  final v1, v2, v3;
  UpdatePage(this.v1, this.v2, this.v3);

  @override
  State<UpdatePage> createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {
  var _v1, _v2, _v3;
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();
  @override
  void initState() {
    _v1 = widget.v1;
    _v2 = widget.v2;
    _v3 = widget.v3;
    todo_title.text = _v2;
    todo_detail.text = _v1;

    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('ปรับปรุงข้อมูล'),
        actions: [
          IconButton(
              onPressed: () {
                deleteTodo();
               
                Navigator.pop(context);
              },
              icon: const Icon(
                Icons.delete,
                color: Color.fromARGB(247, 242, 175, 6),
                size: 40,
              ))
        ],
      ),
      body: ListView(children: [
        Padding(
          padding:
              const EdgeInsets.only(top: 20, right: 8, left: 8, bottom: 10),
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
          color: Color.fromARGB(247, 242, 175, 6),
          child: TextButton(
            onPressed: () {
              updateTodo();
            },
            child: const Text(
              'แก้ไข',
              style: TextStyle(fontSize: 30, color: Colors.black),
            ),
          ),
        ),
      ]),
    );
  }

  Future updateTodo() async {
    //  var url = Uri.https('792f-2001-fb1-86-56c-3922-2192-c0fb-369a.ap.ngrok.io',  '/api/post-todolist');
    var url = Uri.http('192.168.1.33:8000', '/api/update-todolist/$_v3');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}","detail":"${todo_detail.text}"}';
    var response = await http.put(url, headers: header, body: jsondata);
    print('--------result-------');
    print(response.body);
  }

  Future deleteTodo() async {
    var url = Uri.http('192.168.1.33:8000', '/api/delete-todolist/$_v3');
    Map<String, String> header = {"Content-type": "application/json"};
    var response = await http.delete(url, headers: header);
    print('--------result-------');
    print(response.body);
  }

  
}
