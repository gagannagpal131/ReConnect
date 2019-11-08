class parent1
{
	int a=6, b, c=10;
	string myStr = "sehaj", noStr="Singh";
};

class parent2
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

class parent3
{
};

class child1 : public parent1 , private parent2
{
	int sehaj;
	double Gagandeep;
};

class child2 : public parent3
{
	int acc;
	void method3()
	{
		cout<<"method 3 output"
	}
};

class child3 : protected parent2 , public parent3
{
	int ase, ns=69;
};

class child4 : private parent2
{
	string method4(int a)
	{

	}int acc;
	void child4_method()
	{

	}
};

class super
{

int method1(){

	int ab = 10;
	string s = "inside method1";

	cout<<"Test output";
	}

};

class intermediate : public super
{
int a = 0;
string s = "hello";
int method2(){

	cout<<"Test output 1";
	}

};

class base : public intermediate
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
