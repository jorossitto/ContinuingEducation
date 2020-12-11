#pragma once
#include <string>
#include "ATM.h"

//e) Bank
//The bank is the entity that the above components belong to.It will read the user inputand generate
//appropriate objects e.g.the total number of ATM machines, the input file handle, etc.It can either read
//the input fileand pass the information to the appropriate components or , pass the filename to the
//components which process the relevant parts.Before control is passed to the System Controller, the
//Traffic Generator is called to create the customer baseand initial traffic.At the end of the simulation, the
//casino should invoke the appropriate methods of the Statistics Keeper to print the final report.

//mybank.set_sim_time(time);
//mybank.generate_customerbase(); // Traffic Generator
//mybank.generate_initial_traffic(); // Traffic Generator
//mybank.simulate(); // System Controller
//mybank.report(); // Statistic Keeper

using namespace std;

class Bank
{
private:
	int ATMS;
	string inputFile;
	int simulationTime;
	ATM* chosenATM;
	list<ATM> atmList;
	queue<Customers> customerQueue;


protected:
public:
	Bank(int ATMS, string inputFile);
	Bank();
	void set_inputfile(string inputFile);
	void set_atm_num(int ATMs);
	void set_sim_time(int time);
	void generate_customerbase(); // Traffic Generator
	void report(); // Statistic Keeper
	list<ATM> getATMList();
	queue<Customers> getCustomers();
	void addCustomer(Customers *customer);
	void serveCustomer();


};

