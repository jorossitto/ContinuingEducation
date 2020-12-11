//a.File Name - State.h
//b.Author - Joseph Rossitto
//c.Date - 11-27-20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - State Pattern.

#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

enum class State
{
    On,
    Off
};

ostream& operator<<(ostream& os, const State& s);

enum class Trigger
{
    Welcome,
    Closed
};

ostream& operator<<(ostream& os, const Trigger& t);



