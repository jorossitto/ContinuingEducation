#pragma once
#include "Account.h"
//1. Personal Account : Account owned by an individual for personal use.There are further
//different types of personal account.
//a.Savings Account
//• Allows holder to make deposits& withdrawals
//• Unlimited number of withdrawals& deposits can be made
//• Earn interest on the money.
//• Can transfer money to other accounts

class SavingsAccount : public Account
{

private:
	int savings_acc_count = 1;

public:
	SavingsAccount();
	SavingsAccount(float balance, float interestRate, std::string SSN);
	void display();
};

