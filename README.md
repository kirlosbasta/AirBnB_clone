<h1>0x00.AirBnB clone - The console</h1>
Welcome to the AirBnB clone project!
This project involves the creation of python packages and command interpreters using cmd module, serializing and deserializing a class, and unit testing.

Command interpreters are written in a simple framework provided by the cmd class.
How to start the program:-
1- clone AirBnB_clone repo to your machine using this url:-
"https://github.com/jsweidan/AirBnB_clone.git"
2-run ./console.py

How to use it:-
There are sevral build in command that you can use to like:-
1-quit
2-create
3-show
4-destroy
5-all
6-update
To get more information of the command or the syntax use "help <code><command></code>"

examples:-
>>> create User
6a802e85-072f-476b-a872-a7ebf1807b88
>>> show User 6a802e85-072f-476b-a872-a7ebf1807b88
[User] (6a802e85-072f-476b-a872-a7ebf1807b88) {'id': '6a802e85-072f-476b-a872-a7ebf1807b88', 'created_at': datetime.datetime(2024, 2, 11, 18, 56, 12, 906211), 'updated_at': datetime.datetime(2024, 2, 11, 18, 56, 12, 906213)}
>>> all
["[User] (d8939dad-ca5b-413a-a6d3-76a87634f017) {'id': 'd8939dad-ca5b-413a-a6d3-76a87634f017', 'created_at': datetime.datetime(2024, 2, 11, 16, 50, 23, 820426), 'updated_at': datetime.datetime(2024, 2, 11, 16, 50, 23, 820427)}", "[BaseModel] (ab31061e-41bb-4f10-a602-be2b0398ec9a) {'id': 'ab31061e-41bb-4f10-a602-be2b0398ec9a', 'created_at': datetime.datetime(2024, 2, 11, 16, 50, 23, 827883), 'updated_at': datetime.datetime(2024, 2, 11, 16, 50, 23, 827884)}"]
>>> update User 6a802e85-072f-476b-a872-a7ebf1807b88 name "James"
>>> show User 6a802e85-072f-476b-a872-a7ebf1807b88
[User] (6a802e85-072f-476b-a872-a7ebf1807b88) {'id': '6a802e85-072f-476b-a872-a7ebf1807b88', 'created_at': datetime.datetime(2024, 2, 11, 18, 56, 12, 906211), 'updated_at': datetime.datetime(2024, 2, 11, 20, 57, 43, 306647), 'name': '"James"'}
>>> destroy User 6a802e85-072f-476b-a872-a7ebf1807b88
>>> show User 6a802e85-072f-476b-a872-a7ebf1807b88
** no instance found **
>>> quit