#include "StatisticsKeeper.h"
#include <iostream>
#include <fstream>

StatisticsKeeper::StatisticsKeeper(Bank* bank)
{
	this->bank = bank;
	this->getNumberOfATMs();
	this->numberOfCustomersServed = 0;
	this->totalServiceTime = 0;
	this->numberOfPeopleServiced = 0;
}

void StatisticsKeeper::Report()
{
	cout << "Number of ATMS: " << this->numberOfATMMachines << endl;
	cout << "Duration of Simulation: " << this->durationOfSimulation << endl;
	cout << "Customers served: " << this->bank->getCustomersServed() << endl;
	//cout << "Customers served by account type: " << endl;
	cout << "Average Service Time: " << this->averageServiceTimePerCustomer << endl;
	//cout << "Average Waiting Time: " << endl;
	cout << endl;

	fstream myfile;
	myfile.open("output.txt", fstream::app);
	myfile << "Number of ATMS: " << this->numberOfATMMachines << endl;
	myfile << "Duration of Simulation: " << this->durationOfSimulation << endl;
	myfile << "Customers served: " << this->bank->getCustomersServed() << endl;
	//cout << "Customers served by account type: " << endl;
	myfile << "Average Service Time: " << this->averageServiceTimePerCustomer << endl;
	//cout << "Average Waiting Time: " << endl;
	myfile << endl;
	myfile.close();
}

void StatisticsKeeper::setDurationOfSimulation(int time)
{
	this->durationOfSimulation = time;
}

void StatisticsKeeper::getNumberOfATMs()
{
	this->numberOfATMMachines = bank->getATMList().size();
}

void StatisticsKeeper::addCustomerServed()
{
	this->numberOfCustomersServed = this->bank->getCustomersServed();
}

void StatisticsKeeper::sumServiceTime(int Time)
{
	this->totalServiceTime += Time;
	this->numberOfPeopleServiced++;
	this->averageServiceTimePerCustomer = this->totalServiceTime / this->numberOfPeopleServiced;
}

void StatisticsKeeper::printFinalStatus()
{
	cout << endl;
	cout << "Final Status: " << endl;
	cout << "Number of ATMS: " << this->numberOfATMMachines << endl;
	cout << "Duration of Simulation: " << this->durationOfSimulation << endl;
	cout << "Customers served: " << this->bank->getCustomersServed() << endl;
	//cout << "Customers served by account type: " << endl;
	cout << "Average Service Time: " << this->averageServiceTimePerCustomer << endl;
	//cout << "Average Waiting Time: " << endl;
	cout << endl;

	fstream myfile;
	myfile.open("output.txt", fstream::app);
	myfile << "Number of ATMS: " << this->numberOfATMMachines << endl;
	myfile << "Duration of Simulation: " << this->durationOfSimulation << endl;
	myfile << "Customers served: " << this->bank->getCustomersServed() << endl;
	//cout << "Customers served by account type: " << endl;
	myfile << "Average Service Time: " << this->averageServiceTimePerCustomer << endl;
	//cout << "Average Waiting Time: " << endl;
	myfile << endl;
	myfile.close();
}
