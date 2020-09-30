//a.File Name - matrix.h
//b.Author - Joseph Rossitto
//c.Date - 9/30/20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - the function definitions for matrix.cpp

#pragma once
#include <iostream>
#include <string>
using namespace std;

class matrix
{
private:
	int rows;
	int columns;
	int** p;

public:
	matrix();
	matrix(int, int);
	matrix(const matrix& m);//avoid shallow copy by doing deep copy
	~matrix();//
	int& operator()(int i, int j) { return p[i][j]; }
	matrix operator=(const matrix& m);//avoid shallow copy by doing deep copy
	friend ostream& operator<<(ostream& os, matrix& matrix);
	float ** setSize(int x, int y);
	//matrix operator+=(matrix& m);

};

