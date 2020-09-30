//a.File Name - program.cpp
//b.Author - Joseph Rossitto
//c.Date - 9/17/20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Contains the main program

#include "BarcodeReader.h"

void main()
{
	int input;
	BarcodeReader barcodeReader;

	cout << "Menu: " << endl;
	cout << "Press 1 to enter barcode: " << endl;
	cout << "Press 2 to read barcode from file: " << endl;
	cin >> input;
	//cout << input;

	if (input == 1)
	{
		barcodeReader.readBarcode();
	}
	else
	{
		barcodeReader.getBarcode();
	}
	

}