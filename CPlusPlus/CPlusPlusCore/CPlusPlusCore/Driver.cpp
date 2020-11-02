#include "Resource.h"
#include <vector>
#include <stdexcept>
#include <iostream>
#include "Driver.h"

using std::vector;
using std::cout;

int main()
{
	vector<int> numbers{ 0,1,2 };
	numbers.push_back(-2);
	numbers[0] = 3;
	int num = numbers[2];

	for (int i : numbers)
	{
		cout << i << '\n';
	}

	Resource r("local");
	{
		spacing();
		vector<Resource> resources;
		resources.push_back(r);
		spacing();
		resources.push_back(Resource("first"));
		spacing();
		resources.push_back(Resource("second"));
		spacing();

	}
}

void spacing()
{
	cout << "-----------------------" << "\n";
}
