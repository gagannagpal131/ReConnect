# ReConnect
**Class Level Architecture Recovery**

--> ReConnect is a tool for class level architecture recovery. <br/>
--> C++ source is taken as input to the tool.<br/>

**Python File: logic.py**<br/>
This file implements the following aspects:</br>
--> The names of all the classes present in the source code are extracted and stored as a class list <br/>
--> Inheritance, Methods and Variables of the classes present in the source code are extracted <br/>
--> Relationship among the classes is stored using Python dictionaries.<br/>

**Python File: UI.py**<br/>
This file implements the following aspects:<br/>
--> Importing of class relationships (dictionaries) from the logic.py file<br/>
--> Tkinter is used to implement the UI of the tool.<br/>

**User Interface**<br/>
--> Main view contains the name of all the classes present in the input source code.<br/>
--> Upon clicking the individual class, new window opens to display the Inheritance, Methods and variables of that particular    class.<br/>

**Execution**<br/>
--> Sample test file used here is SampleCPP.cpp.<br/>
--> Excecute the UI.py file using Python.<br/>

**Screen Shots** <br/><br/>
--> Main View <br/><br/>
<img src="https://github.com/gagannagpal131/ReConnect/blob/master/Screenshots/Main%20View.png" width="500">

--> Class View <br/><br/>
<img src = "https://github.com/gagannagpal131/ReConnect/blob/master/Screenshots/Class%20View%201.png" width="500">

--> Clustered View <br/><br/>
<img src = "https://github.com/gagannagpal131/ReConnect/blob/master/Screenshots/Cluster%20View.png" width="750">
