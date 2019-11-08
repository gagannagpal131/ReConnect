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
};

class child2 : public parent3 
{
	int acc;
	void method3()
	{
		
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
	void chld4()
	{
		
	}
};