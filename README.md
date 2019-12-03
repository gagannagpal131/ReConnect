# ReConnect
Class Level Architecture Recovery

--> ReConnect is a tool for class level architecture recovery. <br/>
--> C++ source is taken as input to the tool.<br/>

**logic.py**<br/>
This file implements the following aspects:</br>
--> The names of all the classes present in the source code are extracted and staored as a class list <br/>
--> Inheritance, Methods and Variables of the classes present in the source code are extracted <br/>
--> Relationship among the classes is stored using Python dictionaries.<br/>

**UI.py**<br/>
This file implements the following aspects:<br/>
--> Importing of class relationships (dictionaries) from the logic.py file<br/>
--> Tkinter is used to implement the UI of the tool.<br/>

**User Interface**<br/>
--> Main view contains the name of all the classes present in the input source code.<br/>
--> Upon clicking the individual class, new window opens to display the Inheritance, Methods and variables of that particular    class.<br/>


