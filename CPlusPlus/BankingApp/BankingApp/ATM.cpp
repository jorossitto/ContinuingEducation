#include "ATM.h"
#include "Customers.h"

ATM::ATM()
{
	static int ATMNumber;
	ATMNumber++;
	this->ATMID = ATMNumber;
}

//ATM::ATM()
//{
//	Customers customer(1, 2);
//	this->lastCustomer = customer;
//}

void ATM::joinQueue(Customers customer)
{
	customerQueue.push(customer);
}

void ATM::leaveQueue()
{
	this->lastCustomer = this->customerQueue.front();
	this->customerQueue.pop();

}

void ATM::setCurrentCustomer(Customers customer)
{
	this->currentCustomer = customer;
}

int ATM::getID()
{
	return ATMID;
}

