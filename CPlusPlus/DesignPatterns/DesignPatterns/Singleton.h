//a.File Name - Singleton.h
//b.Author - Joseph Rossitto
//c.Date - 11-27-20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Singleton Pattern.
#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <map>


using namespace std;

class Singleton
{
private:
	Singleton();
	map<string, int> capitals;

public:
	Singleton(Singleton const&) = delete;
	void operator=(Singleton const&) = delete;
	static Singleton& get();
	void print();
	map<string, int> load();

};

