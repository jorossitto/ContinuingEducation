#pragma once
#include "Account.h"
//Checking Account
//• Allows holder to make deposits& withdrawals
//• Unlimited number of withdrawals& deposits can be made
//• No interest on the money.
//• Can transfer money to other accounts.
class CheckingAccount: public Account
{
private:
	int checking_acc_count = 1;
	//float interest = 0;
	//float balance;

public:
	CheckingAccount();
	CheckingAccount(float balance, std::string SSN);
	void display();

};

