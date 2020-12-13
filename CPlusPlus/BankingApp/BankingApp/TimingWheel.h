#include "Partition.h"
//#include "TrafficGenerator.h"
#include "Customers.h"
#include "Bank.h"

#pragma once
class TimingWheel
{
private:
	int time;
	int maxDelay = 12;
	//Partition *slot[maxDelay[1]+1];
	//TrafficGenerator traffic;
	int currentSlot;
	queue<Customers> customerQueue;
	list<ATM> atmList;
	vector<list<ATM>> timeSlots;
	Bank* bank;
	int customersServed;

public:
	TimingWheel(Bank* bank);
	void insert(Customers customer, ATM* ATMPointer);
	void schedule();
	void createTimeSlots();
	void addTime();
	int getTime();
};

