#include "TrafficGenerator.h"
#include <cstdlib>
#include "SavingsAccount.h"
#include "CheckingAccount.h"
#include "BusinessChecking.h"
#include "CODAccount.h"
#include "ForeignCurrencyAccount.h"
#include "HighVolumeCheckingAccount.h"
#include "MoneyMarketAccount.h"
#include "BusinessSavings.h"
#include "TimingWheel.h"

//TrafficGenerator::TrafficGenerator()
//{
//	//this->customersLeft = customerBase - initialTraffic;
//	this->customersLeft = customerBase;
//	//this->time++;
//
//}

TrafficGenerator::TrafficGenerator(Bank* bank, TimingWheel* timingWheel)
{
	this->timingWheel = timingWheel;
	this->bank = bank;
	this->customersLeft = customerBase;
}

void TrafficGenerator::CreateCustomer(int amount)
{
	//Customers* customerList[200];
	int accountAmount = 0;
	for (amount; amount > 0; amount--)
	{
		//int serviceTime[2] = { 5,12 };
		int randomServiceTime = rand() % 6 + 5;
		cout << "Random service time" << randomServiceTime << endl;
		this->customersLeft--;
		//customerList[this->customersLeft] = new Customers(this->time, randomServiceTime);
		this->currentCustomer = new Customers(this->time, randomServiceTime);
		bank->addCustomer(this->currentCustomer);
		//Customers* customer = new Customers(time);
		//Customers customer(this->time, this->time);
		int randomNumber = (rand() % 100 + 1);
		if (randomNumber <= this->multipleAccounts)
		{
			accountAmount = 2;
		}
		else
		{
			accountAmount = 1;
		}
		CreateAccounts(accountAmount);
		
		//customer.addAccount();
		//this->customers.push_back(customer);
	}

}

void TrafficGenerator::CreateAccounts(int amount)
{
	//Account* accounts[8];
	//accounts[0] = new SavingsAccount();
	//accounts[1] = new CheckingAccount();
	//accounts[2] = new MoneyMarketAccount();
	//accounts[3] = new CODAccount();
	//accounts[4] = new BusinessSavings();
	//accounts[5] = new BusinessChecking();
	//accounts[6] = new HighVolumeCheckingAccount();
	//accounts[7] = new ForeignCurrencyAccount();
	//float personalAccounts = 65;
	//float businessAccounts = 100 - personalAccounts;
	//std::set<int> savingAccounts = { 50,30 };
	//std::set<int> checkingAccounts = { 30,55 };
	//std::set<int> moneyMarketAccounts = { 8,0 };
	//std::set<int> certificateOfDeposits = { 12,0 };
	//std::set<int> highVolumeChecking = { 0,10 };
	//std::set<int> foreignCurrency = { 0,5 };
	//const int numberOfAccounts = amount;
	int randomNumberAccount = (rand() % 100 + 1);
	//Account* accounts[2];
	//Account account;

	for (amount; amount > 0; amount--)
	{
		//Customers* customer = new Customers(time);
		//Customers customer(time, this->time);
		
		if (randomNumberAccount <= this->personalAccounts)
		{
			int randomNumber = (rand() % 100 + 1);
			int personalSavingAccountPercent = this->savingAccounts[0];
			int personalCheckingAccountPercent = personalSavingAccountPercent + this->checkingAccounts[0];
			int personalMoneyMarketAccountPercent = personalCheckingAccountPercent + this->moneyMarketAccounts[0];

			if (randomNumber <= personalSavingAccountPercent)
			{
				this->currentCustomer->addAccount(amount -1, 1);
				//customerList[this->customersLeft]->addAccount(amount-1, 1);
				//account = SavingsAccount();
				//accounts[amount] = new SavingsAccount();
			}
			else if(randomNumber <= personalSavingAccountPercent)
			{
				this->currentCustomer->addAccount(amount - 1, 2);
				//customerList[this->customersLeft]->addAccount(amount-1, 2);
				//account = CheckingAccount();
				//accounts[amount] = new CheckingAccount();
			}
			else if (randomNumber <= personalMoneyMarketAccountPercent)
			{
				this->currentCustomer->addAccount(amount - 1, 3);
				//customerList[this->customersLeft]->addAccount(amount-1, 3);
				//account = MoneyMarketAccount();
				//accounts[amount] = new MoneyMarketAccount();
			}
			else //COD
			{
				this->currentCustomer->addAccount(amount - 1, 4);
				//customerList[this->customersLeft]->addAccount(amount-1, 4);
				//account = CODAccount();
				//accounts[amount] = new CODAccount();
			}

		}
		else //businessAccount
		{
			int randomNumber = (rand() % 100 + 1);
			int businessSavingAccountPercent = this->savingAccounts[1];
			int businessCheckingAccountPercent = businessSavingAccountPercent + this->checkingAccounts[1];
			int businessHighVolumeCheckingAccountPercent = businessCheckingAccountPercent + this->highVolumeChecking[1];

			if (randomNumber <= businessSavingAccountPercent)
			{
				this->currentCustomer->addAccount(amount - 1, 5);
				//customerList[this->customersLeft]->addAccount(amount-1, 5);
				//account = BusinessSavings();
				//accounts[amount] = new BusinessSavings();
			}
			else if (randomNumber <= businessCheckingAccountPercent)
			{
				this->currentCustomer->addAccount(amount - 1, 6);
				//customerList[this->customersLeft]->addAccount(amount-1, 6);
				//account = BusinessChecking();
				//accounts[amount] = new BusinessChecking();
			}
			else if (randomNumber <= businessHighVolumeCheckingAccountPercent)
			{
				this->currentCustomer->addAccount(amount - 1, 7);
				//customerList[this->customersLeft]->addAccount(amount-1, 7);
				//account = HighVolumeCheckingAccount();
				//accounts[amount] = new HighVolumeCheckingAccount();
			}
			else //foreignCurrency
			{
				this->currentCustomer->addAccount(amount - 1, 8);
				//customerList[this->customersLeft]->addAccount(amount-1, 8);
				//account = ForeignCurrencyAccount();
				//accounts[amount] = new ForeignCurrencyAccount();
			}
			//customer.addAccount(accounts[amount]);
			
		}
		//customerList[this->customersLeft]->addAccount(account);
		//customerList[this->customersLeft].addAccount(account);
		//this->customers.push_back(customer);
	}
}

int TrafficGenerator::getTime()
{
	return this->time;
}

int* TrafficGenerator::getServiceTime()
{
	return this->serviceTime;
}

void TrafficGenerator::RunSimulation()
{
	CreateCustomer(initialTraffic);

	int customer = 0;

	while (customersLeft > 0)
	{
		this->timingWheel->addTime();
		this->timingWheel->schedule();
		int howManyCustomers = rand() % 3;
		cout << "Creating " << howManyCustomers << " Customer[s] " << "We have " << customersLeft << "Customers left" << endl;
		this->customersLeft - howManyCustomers;
		CreateCustomer(howManyCustomers);
	}

	//typedef std::list<Customers>::iterator CustomerPointer;
	//for (CustomerPointer i = customers.begin(); i != customers.end(); i++)
	//{
	//	i->Display();
	//}
	//Customers customer;
	this->bank->getCustomers().back().Display();
	this->bank->getCustomers().front().Display();

	//this->customerList[1]->Display();
	//this->customerList[10]->Display();
	//this->customerList[100]->Display();
	//cout << customers.size() << endl;
}
