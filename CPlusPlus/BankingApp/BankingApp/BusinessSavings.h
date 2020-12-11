#pragma once
#include "SavingsAccount.h"
//Savings Account : Similar to the aforementioned business accounts in most
//respects, but it also has a rate of interest associated with the monies in the
//account.The numbers of deposits are unlimitedand free but the number of free
//withdrawals is limited.
class BusinessSavings :public SavingsAccount
{
	int freeWithdrawalsLeft =1;
	float withdrawalFee = 2.5;
	int b_savings_acc_count = 0;
	
public:
	BusinessSavings();
	void AddInterest();
	void Withdraw(float amount, string accountID);
	void display();
};

