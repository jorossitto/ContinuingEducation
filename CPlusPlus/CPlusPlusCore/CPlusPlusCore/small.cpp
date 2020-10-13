
#include "testclass.h"
#include <iostream>
#include <string>
#include "small.h"
#include "matrix.h"
#include <algorithm>
#include <cctype>
#include "STL.h"

using namespace std;
using namespace testNamespace;

int main()
{
	//testClassTest();
	//testMatrix();
	STL stlTest;
	//stlTest.CopyItMain();
	stlTest.FowlMain();
	//stlTest.ListMain();
	return 0;
}

void testMatrix()
{
	matrix m1(2, 3), m2(2, 3), m3(2, 3);
	m1(0, 0) = 5;
	m2(0, 0) = 7;
	m3 = m2;
	cout << m3(0, 0) << endl;
	//m3 += m1;
	cout << "Now m3(0,0) = " << m3(0, 0);
}

void testClassTest()
{
	testclass mc;

	cout << mc.testints(1, 2) << endl;
	mc.do_something();
}

// usebrass1.cpp -- testing bank account classes. Compile with brass.cpp
#include <iostream>
#include "brass.h"
int usebrass1()
{
	using std::cout;
	using std::endl;
	Brass Piggy("Porcelot Pigg", 381299, 4000.00);
	BrassPlus Hoggy("Horatio Hogg", 382288, 3000.00);
	Piggy.ViewAcct();
	cout << endl;
	Hoggy.ViewAcct();
	cout << endl;
	cout << "Depositing $1000 into the Hogg Account:\n";
	Hoggy.Deposit(1000.00);
	cout << "New balance: $" << Hoggy.Balance() << endl;
	cout << "Withdrawing $4200 from the Pigg Account:\n";
	Piggy.Withdraw(4200.00);
	cout << "Pigg account balance: $" << Piggy.Balance() << endl;
	cout << "Withdrawing $4200 from the Hogg Account:\n";
	Hoggy.Withdraw(4200.00);
	Hoggy.ViewAcct();
	return 0;
}