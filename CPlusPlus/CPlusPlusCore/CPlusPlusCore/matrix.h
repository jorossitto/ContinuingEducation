#pragma once
class matrix
{
private:
	int rows;
	int columns;
	int ** p;

public:
	matrix(int, int);
	matrix(const matrix&);//avoid shallow copy by doing deep copy
	~matrix();//
	int& operator()(int i, int j) { return p[i][j]; }
	matrix operator=(const matrix& m);//avoid shallow copy by doing deep copy
	matrix operator+=(matrix& m);

};

