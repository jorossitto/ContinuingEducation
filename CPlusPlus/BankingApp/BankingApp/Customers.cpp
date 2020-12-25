#include "Customers.h"
#include "SavingsAccount.h"
#include "CheckingAccount.h"
#include "BusinessChecking.h"
#include "CODAccount.h"
#include "ForeignCurrencyAccount.h"
#include "HighVolumeCheckingAccount.h"
#include "MoneyMarketAccount.h"
#include "BusinessSavings.h"
#include <queue>
#include <fstream>


Customers::Customers()
{
	static int customerCount;
	customerCount++;
	this->customerID = customerCount;
}

Customers::Customers(int arrivalTime, int serviceTime = 0)
{
	static int customerCount;
	customerCount++;
	this->customerID = customerCount;
	this->arrivalTime = arrivalTime;
	this->serviceTime = serviceTime;
}

void Customers::addAccount(int account, int accountType)
{
	/*this->accounts.push_back(account);*/
	//Account* accounts[2];
	if (accountType == 1)
	{
		accounts[account] = new SavingsAccount();
		//accounts[amount] = new SavingsAccount();
	}
	else if (accountType == 2)
	{
		accounts[account] = new CheckingAccount();
		//accounts[amount] = new CheckingAccount();
	}
	else if (accountType == 3)
	{
		accounts[account] = new MoneyMarketAccount();
		//accounts[amount] = new MoneyMarketAccount();
	}
	else if (accountType == 4)
	{
		accounts[account] = new CODAccount();
		//accounts[amount] = new CODAccount();
	}
	else if (accountType == 5)
	{
		accounts[account] = new BusinessSavings();
		//accounts[amount] = new BusinessSavings();
	}
	else if (accountType == 6)
	{
		accounts[account] = new BusinessChecking();
		//accounts[amount] = new BusinessChecking();
	}
	else if (accountType == 7)
	{
		accounts[account] = new HighVolumeCheckingAccount();
		//accounts[amount] = new HighVolumeCheckingAccount();
	}
	else//foreignCurrency
	{
		accounts[account] = new ForeignCurrencyAccount();
		//accounts[amount] = new ForeignCurrencyAccount();
	}
	this->accountsTest.push_back(accounts[account]);

}

void Customers::calculateWaitingTime()
{
}

void Customers::Display()
{
	//Account* accounts[2];
	cout << "Your customer ID is: " << customerID << endl;
	cout << "Your service time is: " << this->serviceTime << endl;
	cout << "Your accounts are: " << endl;
	//accounts[i].
	//for (int i = 0; i < 2; i++)
	//{
	//	//cout << i << endl;
	//	try
	//	{
	//		if (accounts[i] == nullptr)
	//		{
	//			cout << "Testing";
	//			
	//		}
	//		else
	//		{
	//			accounts[i]->display();
	//		}
	//		
	//	}
	//	catch(const std::exception& e)
	//	{
	//		cout << e.what() << endl;
	//	}
	//	catch (char* e)
	//	{
	//		cout << "Caught you" << endl;
	//	}
	//}
	//cout << "Your first account is " << 
	//typedef std::unique_ptr<Account> AccountPointer;
	typedef std::list<Account*>::iterator AccountPointer;
	for (AccountPointer i = accountsTest.begin(); i != accountsTest.end(); i++)
	{
		(*i)->display();
	}
	//for_each(accountsTest.begin(), accountsTest.end(), &Account::display);
	//for_each()
}

int Customers::getServiceTime()
{
	return serviceTime;
}

void Customers::report()
{
	fstream myfile;
	myfile.open("output.txt", fstream::app);
	myfile << "Your customer ID is: " << customerID << endl;
	myfile << "Your service time is: " << this->serviceTime << endl;
	myfile << "Your accounts are: " << endl;
	myfile.close();
	cout << "Your customer ID is: " << customerID << endl;
	cout << "Your service time is: " << this->serviceTime << endl;
	cout << "Your accounts are: " << endl;

	typedef std::list<Account*>::iterator AccountPointer;
	for (AccountPointer i = accountsTest.begin(); i != accountsTest.end(); i++)
	{
		//(*i)->display();
		(*i)->reportDone();
	}
}

int Customers::getID()
{
	return this->customerID;
}


