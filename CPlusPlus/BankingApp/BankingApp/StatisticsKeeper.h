#pragma once
#include "Bank.h"
//c) Statistics Keeper
//This component collects all the data needed for reporting statistics.The simulation must run for the time
//specified by the user(we’ll use one iteration of the loop as one unit of time) and report statistics at the
//end of the simulation.Some information provided might include :
//1. Duration of simulation
//2. Number of ATM machines
//3. Total no.of customers serviced
//4. Total no.of customers serviced categorized by type of accounts
//5. Average service time for each customer
//6. Average waiting time for each customer
//7. Total number of transactions
//8. Total number of transactions categorized by type of transaction
//9. Total amount of money deposited / withdrawn
//10. Number of refill_cash events generated
class StatisticsKeeper
{
private:
	int durationOfSimulation;
	int numberOfATMMachines;
	int numberOfCustomersServed;
	int numberOfCustomersServicedByAccountType[8] = { 0,0,0,0,0,0,0,0 };
	float averageServiceTimePerCustomer;
	float waitingServiceTimePerCustomer;
	int totalNumberOfTransactions;
	int totalNumberOfTransactionsByTransactionType[4] = { 0,0,0,0 };
	int totalAmountOfMoneyDeposited;
	int totalAmountOfMoneyWithdrawn;
	int numberOfRefillCashEventsGenerated;
	int totalServiceTime;
	int numberOfPeopleServiced;
	Bank* bank;

protected:

public:
	StatisticsKeeper(Bank* bank);
	void Report();
	void setDurationOfSimulation(int time);
	void getNumberOfATMs();
	void addCustomerServed();
	void sumServiceTime(int Time);
	void printFinalStatus();


};

