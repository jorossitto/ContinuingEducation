#pragma once
#include "CheckingAccount.h"
//High Volume Checking Account : Similar to Checking account but unlimited
//number of transactions are allowed.However, there is a small transaction fee
//for every deposit or check.
class HighVolumeCheckingAccount: public CheckingAccount
{
private:
	float DepositFee = 1.0;
	int hvc_checking_acc_count = 1;

public:
	HighVolumeCheckingAccount();
	void Deposit(float amount, string accountID);
	void Withdraw(float amount, string accountID);
	void display();
};

