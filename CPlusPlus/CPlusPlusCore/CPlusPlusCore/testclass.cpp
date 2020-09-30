#include "testclass.h"
#include <iostream>
using namespace std;
using namespace testNamespace;


int testNamespace::testclass::testints(int x, int y)
{
	return (x + y) / 2;
}

void testNamespace::testclass::do_something()
{
	cout << "Do Somthing" << endl;
}

