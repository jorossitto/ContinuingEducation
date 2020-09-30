//a.File Name - BarcodeReader.h
//b.Author - Joseph Rossitto
//c.Date - 9/17/20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Contains the documentation for barcodeReader

#pragma once
#include <iostream>
#include <string>
using namespace std;

class BarcodeReader
{
private:
	string barcode = "";
	string editedBarcode = "";
	string validationStatement = "";
	int manufacturorCode;
	int productCode;
	int checkDigit;
	int numberSystem;
	bool continueChecking;

public:
	void readBarcode();
	void getBarcode();
	bool replaceDashes(string barcode);
	bool validateBarcode();
	friend ostream& operator<<(ostream& os, BarcodeReader& b);

};

