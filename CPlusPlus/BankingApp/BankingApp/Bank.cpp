#include "Bank.h"

//Documentation(out of 10) :
//	Part 1 : Hierarchy Design & Implementation(out of 12) :
//	Part 2 : System Components(out of 13) :
//	Part 3 & 4 : Event Handling and Scheduling(out of 15) :


Bank::Bank(int ATMS, string inputFile)
{
	this->ATMS = ATMS;
	this->inputFile = inputFile;
	//this->trafficGenerator = TrafficGenerator();

	for (int i = 0; i < ATMS; i++)
	{
		ATM atm = ATM();
		this->atmList.push_back(atm);
	}
}

void Bank::set_inputfile(string inputFile)
{
	this->inputFile = inputFile;
}

void Bank::set_atm_num(int ATMs)
{
	this->ATMS = ATMs;
}

void Bank::set_sim_time(int time)
{
	this->simulationTime = time;
}

void Bank::generate_customerbase()
{
	//TrafficGenerator trafficGenerator = TrafficGenerator();
}

void Bank::report()
{
	//cout << "Duration of simulation: " << this->trafficGenerator.getTime() << endl;
	cout << "Number of ATMs : " << this->ATMS << endl;
}

list<ATM> Bank::getATMList()
{
	return this->atmList;
}

queue<Customers> Bank::getCustomers()
{
	return this->customerQueue;
}

void Bank::addCustomer(Customers* customer)
{
	this->customerQueue.push(*customer);
}

void Bank::serveCustomer()
{
	this->customerQueue.pop();
}
