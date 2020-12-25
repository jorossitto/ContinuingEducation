#pragma once
#include "Account.h"
#include <time.h>
#include <set>
#include <list>

//A customer can hold one or more accounts.These could be both Personal accounts and /or Business
//accounts.Furthermore, the customer can invoke any of the transactions that were detailed in Part I.
//Among other attributes, a customer would have an arrival time(when the customer joins the ATM queue),
//service time(how long he / she would use the ATM machine), exit time(when the customer in done).This
//will enable you to compute the waiting time for the customer.
class Customers
{
protected:
	int customerID;
	std::list<Account*> accountsTest;
	Account* accounts[2];

	int arrivalTime;
	int serviceTime;
	int exitTime;
	int waitingTime;


public:
	Customers();
	Customers(int arrivalTime, int serviceTime);
	void addAccount(int account, int accountType);
	void calculateWaitingTime();
	virtual void Display();
	int getServiceTime();
	void report();
	int getID();
	//void createAccounts(int howMany);
};

