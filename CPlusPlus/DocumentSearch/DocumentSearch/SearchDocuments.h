//a.File Name - SearchDocuments.h
//b.Author - Joseph Rossitto
//c.Date - 10-14-2020
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - headerfile for the SearchDocuments Class

#pragma once
#include <string>
#include <set>

class SearchDocuments
{
private:
	std::set<std::string> documentContents;
	std::set<std::string> search;
	int searchLength;
	int documentLength;
	double simScore;

public:
	SearchDocuments(std::string search, std::string document);
	void printWords(std::string newString);
	void addWords(std::string newString, std::set<std::string>& whatToAddTo);
	double ComputeSim();
	auto GetDocument() { return documentContents; }
	auto GetSimScore() { return simScore; }

};

