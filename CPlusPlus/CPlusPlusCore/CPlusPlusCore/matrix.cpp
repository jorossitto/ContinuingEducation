#include "matrix.h"
#include <cassert>

matrix::matrix(int row, int column):rows(row), columns(column)
{
	p = new int* [rows];
	for (int i = 0; i < rows; i++)
		p[i] = new int[columns];
}

matrix::matrix(const matrix& m):rows(m.rows), columns(m.columns)
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
	assert(m.columns == columns && m.rows == rows);
	int i, j;
	for (i = 0; i < rows; i++)
		for (j = 0; j < columns; j++)
			p[i][j] = m.p[i][j];
	return(*this);
}

//matrix matrix::operator+=(matrix& m)
//{
//	return matrix();
//}
