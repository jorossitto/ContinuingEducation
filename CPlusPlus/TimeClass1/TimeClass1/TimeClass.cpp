// mytime0.cpp -- implementing Time methods
#include <iostream>
using namespace std;

#include "TimeClass.h"

double avg(int n1, int n2, int n3, int n4, int n5)
{
	double result;
	result = (n1 + n2 + n3 + n4 + n5) / 5.0;
	return result;
}

void swap(int v1, int v2)
{
	int temp;
	temp = v1;
	v1 = v2;
	v2 = temp;

}