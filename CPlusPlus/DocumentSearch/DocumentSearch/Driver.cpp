//a.File Name - Driver.cpp
//b.Author - Joseph Rossitto
//c.Date - 10-14-2020
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - drives the program forward with simple selection menu

#include "SearchDocuments.h"
#include "Driver.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>
#include <numeric>
#include <iterator>
#include <list>
#include <set>

using namespace std;

int main()
{
	int documentAmount;
	string searchString;
	string documentString;
	double maxScore = 0;
	double currentScore = 0;
	string bestMatch;

	cout << "What is your search? ";
	getline(cin, searchString);
	cout << endl;

	cout << "How many documents would you like to search? ";
	cin >> documentAmount;
	cout << endl;

	vector<string> documents;
	cin.ignore();
	//getline(cin, documentString);
	for (int i = 0; i < documentAmount; i++)
	{
		cout << "Please enter your document: ";
		getline(cin, documentString);
		//while (documentString == "")
		//{
		//	getline(cin, documentString);
		//}
		//cout << documentString << "**";
		cout << endl;
		SearchDocuments firstDocument(searchString, documentString);
		if (firstDocument.GetSimScore() > maxScore)
		{
			maxScore = firstDocument.GetSimScore();
			bestMatch = documentString;
		}
		cout << endl;
		
	}

	cout << "Your search returned the document " << bestMatch << ", With a Sim Score of: " << maxScore;
	


	
	//return notes();
	
	//firstDocument.printWords(tempString);


	//for (string word : document)
	//{
	//	cout << word << endl;
	//}

	return 0;
}

int notes()
{
	vector<int> v;
	vector<string> s = { "hi", "my", "name", "is" };

	//populate
	for (int i = 0; i < 5; i++)
	{
		v.push_back(i);
	}

	//total
	int sum = 0;
	for (int elem : v)
	{
		sum += elem;
	}

	//int total = std::accumulate(begin(s), end(s), 0);

	int count3 = count(begin(v), end(v), 3);
	cout << count3 << " Sum: " << sum << endl;

	auto copyV = remove_if(begin(v), end(v), [](int elem) {return (elem == 3); });

	for (int i = 0; i < 5; i++)
	{
		v.push_back(rand());
	}

	//Sort
	sort(begin(v), end(v));

	return 0;
}
