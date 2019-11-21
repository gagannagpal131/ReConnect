class Parent1
{
	int a=6, b, c=10;
	string myStr = "sehaj", noStr="Singh";
};

class Parent2
{
	int a=6, b, c=10;
	int x,y,z=10;

	int method1()
	{
		Cout<<"method 1 output";
	}

	int method2()
	{
		double dbl=98, yeah;
		Cout<<"method 2 output";
	}
};

class Parent3
{
};

class Super
{

int method1(){

	int ab = 10;
	string s = "inside method1";

	cout<<"Test output";
	}

};

class Intermediate : public Super
{
int a = 0;
string s = "hello";
int method2(){

	cout<<"Test output 1";
	}

};

class Child1 : public Parent1 , private Parent2
{
	int sehaj;
	double Gagandeep;
};

class Child2 : public Parent3
{
	int acc;
	void method3()
	{
		cout<<"method 3 output"
	}
};

class Child3 : protected Parent2 , public Parent3
{
	int ase, ns=69;
};

class Child4 : private Parent2
{
	float method4(int a)
	{

	}int acc;
	void child4_method()
	{

	}
};



class Base : public Intermediate
{

	int ab = 10;
	double xy = 55;
	char c;

	int method3(){

	cout<<"Test output 2";
	}

	char method5(){

		out<<"Test output 5";
	}
};
