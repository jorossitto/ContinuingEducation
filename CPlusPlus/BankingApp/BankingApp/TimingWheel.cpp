#include "TimingWheel.h"

TimingWheel::TimingWheel(Bank* bank)
{
	this->bank = bank;
	this->time = 0;
	this->createTimeSlots();
}

void TimingWheel::insert(Customers customer, ATM* ATMPointer)
{
	ATMPointer->joinQueue(customer);
}

void TimingWheel::schedule()
{
	//Next TimeSlot in the list
	int size = timeSlots.size();
	this->atmList = timeSlots.back();

	//This is customers using the atm
	while (atmList.empty() == false)
	{
		//Take the next customer in the queue
		customerQueue = bank->getCustomers();
		Customers nextCustomer = customerQueue.front();
		bank->serveCustomer();

		//give the ATM the customer
		list<ATM> currentTimeslotATMList = timeSlots.back();
		ATM currentATM = currentTimeslotATMList.front();
		currentATM.setCurrentCustomer(nextCustomer);

		//add the atm to its new TimeSlot
		int waitingTime = nextCustomer.getServiceTime();
		cout << "Waiting time" << waitingTime << endl;
		list<ATM> nextATMList = timeSlots[waitingTime];
		cout << "*" << timeSlots[waitingTime].size() << endl;
		cout << "*" << nextATMList.size() << endl;
		nextATMList.push_back(currentATM);
		timeSlots[waitingTime] = nextATMList;
		atmList.pop_front();
		cout << "**" << timeSlots[waitingTime].size() << endl;
		cout << "**" << nextATMList.size() << endl;
	}
	cout << "***" << atmList.size() << endl;

	//move the timeslots forward
	list<ATM> emptyATMList;
	cout << "Timing Wheel before pop and insert" << endl;
	for (int i = 0; i < timeSlots.size(); i++)
	{
		cout << timeSlots[i].size() << endl;
	}
	cout << endl;
	timeSlots.pop_back();
	timeSlots.insert(timeSlots.begin(), emptyATMList);
	for (int i = 0; i < timeSlots.size(); i++)
	{
		cout << timeSlots[i].size() << endl;
	}
}

void TimingWheel::createTimeSlots()
{
	//get atms from the bank
	this->atmList = bank->getATMList();
	timeSlots.push_back(atmList);

	for (int i = 0; i < maxDelay -1; i++)
	{
		list<ATM> emptyATMList;
		timeSlots.push_back(emptyATMList);
	}
}

void TimingWheel::addTime()
{
	this->time++;
}
