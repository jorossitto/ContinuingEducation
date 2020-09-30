#include <iostream>

using namespace std;

#include "TimeClass.h"
#include "TimeClass.cpp"

void main()
{
	int x = 1;
	int y = 2;
	int z = 3;
	int a = 4;
	int b = 5;

	cout << avg(x, y, z, a, b) << endl;

	double result = avg(x, y, z, 2 * a, 3 * b);

	cout << "result: " << result << endl;

	swap(x, y);

	cout << "x = " << x << "y =" << y << endl;






}