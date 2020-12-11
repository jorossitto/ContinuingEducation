//a.File Name - Adaptor.h
//b.Author - Joseph Rossitto
//c.Date - 11-27-20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Adaptor Pattern.
#pragma once
#include <vector>
#include <stack>
#include <string>
#include <algorithm> 
#include <sstream>
#include <iterator>

using namespace std;

class Adaptor
{
private:
	string adaptingString;
	int adaptingInt;

public:
	Adaptor();

	string toMillions(int number) const;
	string get();

};

