#pragma once
#include "CheckingAccount.h"
//Business Account : Bank accounts for a business may vary depending on the type of
//business.
//a.Checking Account : Details same as personal checking account but limit on
//number of transactions
class BusinessChecking: public CheckingAccount
{
private:
	int transactionsLeft;
	int freeWithdrawalsLeft = 1;
	int freeDeposit = 1;
	float DepositFee = 1.0;
	float withdrawalFee = 2.5;
	int b_checking_acc_count = 1;
public:
	BusinessChecking();
	void Deposit(float amount, string accountID);
	void Withdraw(float amount, string accountID);
	void display();
};

