import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
import 'add.dart';
import 'update_todolist.dart';

class Todolist extends StatefulWidget {
  @override
  State<Todolist> createState() => _TodolistState();
}

class _TodolistState extends State<Todolist> {
  List todolistItem = ['A', 'B', 'C', 'D'];

  @override
  void initState() {
    getTodolist();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey.shade100,
      floatingActionButton: FloatingActionButton(
        backgroundColor: Color.fromARGB(255, 32, 37, 4),
        onPressed: () {
          Navigator.push(
                  context, MaterialPageRoute(builder: (context) => AddPage()))
              .then((value) => {getTodolist()});
        },
        child: Icon(
          Icons.add,
          color: Color.fromARGB(255, 247, 231, 4),
        ),
      ),
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 47, 55, 5),
        actions: [
          IconButton(
              onPressed: () {
                setState(() {
                  getTodolist();
                });
              },
              icon: const Icon(
                Icons.refresh_sharp,
                color: Colors.amber,
                size: 30,
              ))
        ],
        title: Text('All Todolist'),
      ),
      body: todolistCreate(),
    );
  }

  Widget todolistCreate() {
    return ListView.builder(
      itemCount: todolistItem.length,
      itemBuilder: (context, index) {
        return Padding(
          padding: const EdgeInsets.all(8.0),
          child: Card(
            color: Colors.blueGrey,
            elevation: 5,
            child: ListTile(
              title: Text('${todolistItem[index]['title']}'),
              subtitle: Text('${todolistItem[index]['detail']}'),
              leading: Text('${todolistItem[index]['id']}'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => UpdatePage(
                      todolistItem[index]['detail'],
                      todolistItem[index]['title'],
                      todolistItem[index]['id'],
                    ),
                  ),
                ).then((value) => {getTodolist()});
              },
            ),
          ),
        );
      },
    );
  }

  Future<void> getTodolist() async {
    List alltode = [];
    var url = Uri.http('192.168.1.33:8000', '/api/all-todolist');
    var response = await http.get(url);
    var result = utf8.decode(response.bodyBytes); //แปลงเป็นภาษาไทย

    setState(() {
      todolistItem = jsonDecode(result);
    });
  }
}
