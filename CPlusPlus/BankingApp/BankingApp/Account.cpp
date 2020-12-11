#include "Account.h"
#include <iostream>

using namespace std;

Account::Account()
{
	static int account_count;
	account_count++;
	this->accountCountString = to_string(account_count);
	this->accountID = "A" + accountCountString;
	this->balance = 0;
	this->interestRate = 1.1;
	this->SSN = "000";
}

Account::Account(float balance, float interestRate, string SSN)
{
	static int account_count;
	account_count++;
	accountCountString = to_string(account_count);
	cout << "Your account count string : " << accountCountString << endl;
	accountID = "A" + accountCountString;
	this->balance = balance;
	this->interestRate = interestRate;
	this->SSN = SSN;
}

void Account::AddInterest()
{
	this->interestGained = this->interestGained + (this->balance * (this->interestRate - 1));
	this->balance = this->balance * this->interestRate;
	cout << "Adding interest " << this->interestRate << endl; 
	cout << "Your new balance is " << this->balance << endl << endl;


}

void Account::Transfer(float amount, Account accountID)
{
	this->balance = this->balance - amount;
	accountID.balance = accountID.balance + amount;
	cout << "Transfering " << amount << "From " << this->accountID << " to " << accountID.accountID<< endl;
}

void Account::Deposit(float amount, string accountID)
{
	cout << "Adding " << amount << " to " << accountID << endl;

	this->balance = this->balance + amount;

	cout << "Your new balance is " << this->balance << endl;
}

void Account::Withdraw(float amount, string accountID)
{
	cout << "Withdrawing " << amount << " from " << accountID << endl;
	this->balance = this->balance - amount;
	cout << "Your new balance is " << this->balance << endl;
}

void Account::setName(std::string name)
{
	this->name = name;
}

void Account::setAddress(std::string address)
{
	this->address = address;
}

void Account::display()
{
	cout << "This is a regular account" << endl;
	cout << "Account number: " << accountID << endl;
	std::cout << "Balance: " << balance << endl;
	cout << "Interest Rate: " << interestRate << endl;
	cout << "SSN: " << SSN << endl << endl;

}


std::ostream& operator<<(std::ostream& os, Account& account)
{
	//float balance;
	//float interestRate;
	//std::string accountID;
	//std::string SSN;
	//std::string name;
	//std::string address;
	std::cout << "Balance: " << account.balance << endl;
	cout << "Interest Rate: " << account.interestRate << endl;

	cout << "Account number: " << account.accountID << endl;
	cout << "SSN: " << account.SSN << endl << endl;

	return cout;

}
