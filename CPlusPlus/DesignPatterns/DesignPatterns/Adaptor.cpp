#include "Adaptor.h"
#include <iostream>

//using namespace std;

Adaptor::Adaptor()
{
}

string Adaptor::toMillions(int number) const
{
	string millions{ adaptingString };
	millions = to_string(number) + " Million";
	return { millions };
}

string Adaptor::get()
{
	cout << this->adaptingString << endl;
	return this->adaptingString;
}
