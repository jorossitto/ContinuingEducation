#pragma once
#include <set>
#include "Customers.h"
#include <list>
#include "Bank.h"
#include "TimingWheel.h"
#include "StatisticsKeeper.h"

//This module generates the customer base, initial trafficand dynamic player traffic.The customer base is
//the total number of customers that hold accounts in the bank.The initial traffic is the number of customers
//in line to use the ATM when simulation starts.Dynamic player traffic are the customers that will arrive
//during the simulation.On arrival, the customer joins the shortest queue(once we scale up in the next
//	phases).
//	You can also choose to have NO initial traffic assuming you are starting the simulation when the ATM is
//	not being used.
//	The above is generated based on the user specified parameters which will come in form of an input file of
//	the given format(black – actual content of file; blue – explanation) :
//	In the above file, it is specified that there is a total of 200 customers.Out of the them, five should be
//	randomly chosen to be in the queue as initial traffic(if implemented).After this we generate a random
//	number between 0 and 2 to decide how many customers arrive at a given time.For every customer, you
//	then generate a random number between 5 and 12 to decide on the service time.Next you generate
//	another random number between 0 and 100. If it is less than 20, the customer has one account; multiple,
//	otherwise.You are free to implement how many accounts(if multiple) in any way you want.At this point,
//	200 <= customer base
//	5 <= initial traffic(if used); change the number to 20 for Phase IV
//	2 <= 0 – 2 customers can come at any given instant – generated randomly; change the number to 7 for Phase IV
//	5 12 <= a customer’s service time can vary from 5 – 12 time units
//	80 <= 80 % of the time a customer has multiple accounts – you are free to decide how many
//	Personal 65 <= 65 % of accounts are personal
//	Business 35 <= 35 % of accounts are business
//	Savings 50 30 <= 50 % of personal accounts are Savings account; 30 % of business accounts are Savings account
//	Checking 30 55
//	Money Market 8 0
//	Certificate of Deposits 12 0
//	High Volume Checking 0 10
//	Foreign Currency 0 5
//	CS 501 Fall 2020
//	Project Part II University of Bridgeport
//	what is left is to decide what is the type of each account.For this, you’ll generate two more random
//	numbers between 0 and 100, one to decide whether the account is Personal or Business and the second
//	to decide on the subtype.Now you are ready to create the appropriate account(s) for the customer.Those
//	of us that are implementing a scaled down version can modify the numbers for the subtypes.Please do
//	NOT change the format of the file.Finally, you’ll decide how manyand what kind of transactions will the
//	customer perform on the account – you are free to design your own methodology for that.
//	At simulation time, the user will be prompted to specify the name of the input fileand the number of ATM
//	machines(you can specify 1 for now) and the duration of simulation.

class TrafficGenerator
{
private:
	int time = 0;
	int customerBase = 200;
	int initialTraffic = 5;
	int customersAtATime = 2;
	int serviceTime[2] = { 5,12 };
	float multipleAccounts = 80;
	float personalAccounts = 65;
	float businessAccounts = 100 - personalAccounts;
	int savingAccounts[2] = { 50, 30 };
	int checkingAccounts[2] = { 30,55 };
	int moneyMarketAccounts[2] = { 8,0 };
	int certificateOfDeposits[2] = { 12,0 };
	int highVolumeChecking[2] = { 0,10 };
	int foreignCurrency[2] = { 0,5 };
	std::list<Customers> customers;
	Customers* customerList[200];
	int customersLeft;
	Bank* bank;
	Customers* currentCustomer;
	TimingWheel* timingWheel;
	StatisticsKeeper* statisticsKeeper;



protected:
public:
	TrafficGenerator(Bank* bank, TimingWheel* timingWheel);
	void CreateCustomer(int amount);
	void CreateAccounts(int amount);
	int getTime();
	int* getServiceTime();
	void RunSimulation();


};

