#include "SavingsAccount.h"

SavingsAccount::SavingsAccount(float balance, float interestRate, std::string SSN) : Account(balance, interestRate, SSN)
{
	savings_acc_count++;
	string s_a_c = to_string(savings_acc_count);
	this->accountID = accountID + 'P' + s_a_c + 'S';
	interestRate = interestRate;
	this->accountType = "Personal Savings Account";
}

SavingsAccount::SavingsAccount()
{
	static int savingAccountNumber;
	savingAccountNumber++;
	string savingAccountString = to_string(savingAccountNumber);
	//string a_c = to_string(account_count);
	this->accountID = this->accountID +  'S' + savingAccountString;
	//interestRate = interestRate;
	this->accountType = "Personal Savings Account";
}
void SavingsAccount::display()
{
	cout << "This is Personal Savings Account"<<endl;
	cout << "Account number: " << accountID << endl;
	std::cout << "Balance: " << balance << endl;
	cout << "Interest Rate: " << interestRate << endl;
	cout << "SSN: " << SSN << endl << endl;
}