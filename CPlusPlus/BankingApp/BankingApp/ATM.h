#pragma once
#include <queue>
#include "Customers.h"
//contains a queue of customers
class ATM
{
private:
	queue<Customers> customerQueue;
	Customers lastCustomer;
	int ATMID;
	Customers currentCustomer;

protected:
public:
	ATM();
	void joinQueue(Customers customer);
	void leaveQueue();
	void setCurrentCustomer(Customers customer);
	int getID();


};

