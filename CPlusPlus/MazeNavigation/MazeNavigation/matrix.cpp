//a.File Name - matrix.cpp
//b.Author - Joseph Rossitto
//c.Date - 9/30/20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Contains matrix function implementation details

#include "matrix.h"
#include <stdlib.h>
#include <iostream>
#include <cassert>
using namespace std;

matrix::matrix()
{
	//Matrix = matrix(1, 1);
}

matrix::matrix(int row=1, int column=1) :rows(row), columns(column)
{
	p = new int* [rows];
	for (int i = 0; i < rows; i++)
	{
		p[i] = new int[columns];
	}
		
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
		{
			p[i][j] = 0;
		}
	}
}

matrix::matrix(const matrix& m) :rows(m.rows), columns(m.columns)
{
	p = new int* [rows];
	for (int i = 0; i < rows; i++)
	{
		p[i] = new int[columns];
	}

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
		{
			p[i][j] = m.p[i][j];
		}
	}
}

matrix::~matrix()
{
	for (int i = 0; i < rows; i++)
	{
		delete[] p[i];
	}
	delete[]p;
}

matrix matrix::operator=(const matrix& m)
{
	//Deallocate old memory
	for (int i = 0; i < rows; i++)
	{
		delete[] p[i];
	}
	delete[]p;

	//update data members
	rows = m.rows;
	columns = m.columns;

	//initalize new matrix
	//matrix newMatrix(rows, columns);

	p = new int* [rows];
	for (int i = 0; i < rows; i++)
	{
		p[i] = new int[columns];
	}

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
		{
			p[i][j] = 0;
		}
	}

	//return new matrix
	return (*this);

	//assert(m.columns == columns && m.rows == rows);
	//int i, j;
	//for (i = 0; i < rows; i++)
	//	for (j = 0; j < columns; j++)
	//		p[i][j] = m.p[i][j];
	//return(*this);
}

float** matrix::setSize(int x, int y)
{
	return nullptr;
}

//matrix matrix::operator+=(matrix& m)
//{
//	return matrix();
//}

ostream& operator<<(ostream& os, matrix& matrix)
{
	for (int i = 0; i < matrix.rows; i++)
	{
		for (int j = 0; j < matrix.columns; j++)
		{
			if (matrix(i, j) == 0)
			{
				os << "=\t";
			}
			if (matrix(i, j) == 1)
			{
				os << "C\t";
			}
			if (matrix(i, j) == 2)
			{
				os << "E\t";
			}
			if (matrix(i, j) == 3)
			{
				os << "O\t";
			}
		}
		os << endl;
	}
	return os;
}
