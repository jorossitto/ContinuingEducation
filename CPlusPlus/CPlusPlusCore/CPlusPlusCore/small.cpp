
#include "testclass.h"
#include <iostream>
#include <string>
#include "small.h"
#include "matrix.h"

using namespace std;
using namespace testNamespace;

int main()
{
	//testClassTest();

	matrix m1(2, 3), m2(2, 3), m3(2, 3);
	m1(0, 0) = 5;
	m2(0, 0) = 7;
	m3 = m2;
	cout << m3(0, 0) << endl;
	m3 += m1;
	cout << "Now m3(0,0) = " << m3(0, 0);
	return 0;
}

void testClassTest()
{
	testclass mc;

	cout << mc.testints(1, 2) << endl;
	mc.do_something();
}
