import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class CareWellHomePage extends StatefulWidget {
  const CareWellHomePage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<CareWellHomePage> createState() => _CareWellHomePageState();
}

class _CareWellHomePageState extends State<CareWellHomePage> {
  String dropdownValue = 'One';

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Center(
      child: Column(
        children: <Widget>[
          Material(
              child: DropdownButton<String>(
            value: dropdownValue,
            icon: const Icon(Icons.arrow_downward),
            elevation: 16,
            style: const TextStyle(color: Colors.deepPurple),
            underline: Container(
              height: 2,
              color: Colors.deepPurpleAccent,
            ),
            onChanged: (String? newValue) {
              setState(() {
                dropdownValue = newValue!;
              });
            },
            /*
            TODO: Get list by querying the data in carewell
            */
            items: <String>['One', 'Two', 'Free', 'Four']
                .map<DropdownMenuItem<String>>((String value) {
              return DropdownMenuItem<String>(
                value: value,
                child: Text(value),
              );
            }).toList(),
          )),
          CareWellListViewCard(title: "Beta Study", subtitle: "ST"),
          CareWellListViewCard(title: "Feasibility Study", subtitle: "ST"),
          CareWellListViewCard(title: "New Grant", subtitle: "ST"),
        ],
      ),
      // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

/*
* Create a card widget for multiple research projects. 
*/
class CareWellListViewCard extends StatelessWidget {
  CareWellListViewCard({Key? key, required this.title, required this.subtitle})
      : super(key: key);
  String title;
  String subtitle;

  @override
  Widget build(BuildContext context) {
    return Card(
        child: ListTile(
      title: Text(this.title),
      subtitle: Text(this.subtitle),
      leading: CircleAvatar(),
      trailing: TextButton(
        child: const Text('VIEW DATA'),
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) => CareWellHomePage(title: "CareWell")),
          );
        },
      ),
    ));
  }
}
