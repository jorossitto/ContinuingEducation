#pragma once
#include<iostream>
#include <string>
#include <set>
#include <ostream>
using namespace std;

//Please remember that other than implementing the features mentioned above your hierarchy
//should be able to generate the account ids as detailed in the project description document.
//You can consider the following to be the basic amount of information for an account.You will be
//adding on attributes as needed for the subtypes.
//Account
//Account ID
//SSN
//Nameand Address(optional)
//Balance

class Account
{
protected:
	int account_count;
	string accountCountString;
	string accountID;
	float balance;
	float interestRate;
	float interestGained;
	//string accountID;
	string SSN;
	string name;
	string address;
	
	//static int void accountCount = 0;


public:
	
    Account();
	explicit Account(float balance, float interestRate, string SSN);

	void virtual AddInterest();
	void virtual Transfer(float amount, Account accountID);
	void virtual Deposit(float amount , string accountID);
	void virtual Withdraw(float amount, string accountID);
	void setName(std::string name);
	void setAddress(std::string address);
	void virtual display();
	friend std::ostream& operator<<(std::ostream& os, Account& account);
	//void setAccountId();

};
