//a.File Name - SearchDocuments.cpp
//b.Author - Joseph Rossitto
//c.Date - 10-14-2020
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - main file for the SearchDocuments Class, handels reading in data, breaking it down into search phrases and calculating sim score

#include "SearchDocuments.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>
#include <numeric>
#include <iterator>
#include <list>
#include <set>
#include <sstream>
#include <cmath>

using namespace std;

SearchDocuments::SearchDocuments(std::string search, std::string document)
{
    //string tempDocument;
    //cin >> tempDocument;
    if (document == "")
    {
        document = "Cows are big. Cows go moo. I love cows.";
    }

    addWords(search, this->search);
    addWords(document, this->documentContents);

    this->searchLength = this->search.size();
    this->documentLength = this->documentContents.size();

    ComputeSim();

    //set<string> tempSet = tempString;
    //vector<string> document = { "Cows are big. Cows go moo. I love cows." };
}

void SearchDocuments::printWords(string str)
{
    // word variable to store word 
    string word;

    // making a string stream 
    stringstream iss(str);

    // Read and print each word. 
    while (iss >> word)
        cout << word << endl;
}

void SearchDocuments::addWords(std::string newString, std::set<std::string>& whatToAddTo)
{
    // word variable to store word 
    string word;

    newString.erase(std::remove(newString.begin(), newString.end(), '.'), newString.end());
    transform(newString.begin(), newString.end(), newString.begin(), ::tolower);
    // making a string stream 
    stringstream iss(newString);

    
    // Read and print each word. 
    while (iss >> word)
        whatToAddTo.insert(word);
        //cout << word << endl;
    int count = 0;
    for (string word : whatToAddTo)
    {
        count = count + 1;
        cout << word << ", ";
        if (count % 10 == 0)
        {
            cout << endl;
        }
    }
    cout << endl;
}

double SearchDocuments::ComputeSim()
{
    int searchMatch = 0;
    int count = 0;
    for (string word : this->search)
    {
        count = std::count_if(begin(this->documentContents), end(this->documentContents), [&](string c) {return (c == word); });
        searchMatch = searchMatch + count;
    }
    double sqrtOfSearch = sqrt(this->searchLength);
    double sqrtOfDocument = sqrt(this->documentLength);

    this->simScore = (searchMatch / (sqrtOfSearch * sqrtOfDocument));
    cout << "Your search value is: " << searchMatch << endl;
    cout << "Your SimScore is: " << this->simScore << endl;

    return this->simScore;
}