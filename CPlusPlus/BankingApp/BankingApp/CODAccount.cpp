#include "CODAccount.h"
//Certificates of Deposits
//• Require the account holder to make a depositand agree to leave funds
//in the account for a specific amount of time
//• Interests are paid in return of the above - mentioned agreement.
//• Interests paid are higher than any of the afore - mentioned accounts.
//• Withdrawals may be allowed on the interest but only a limited number.
CODAccount::CODAccount()
{
	this->interestRate = interestRate + .1;
	static int codAccountNumber;
	codAccountNumber++;
	codAccountString = "D" + to_string(codAccountNumber);
	this->accountID = this->accountID + codAccountString;
	this->withdrawalsAllowed = 1;
	this->depositTime = 12;
	this->interestGained = 0;

}

void CODAccount::Withdraw(float amount)
{
	if (this->withdrawalsAllowed > 0)
	{
		if (amount < this->interestGained)
		{
			this->interestGained = this->interestGained - amount;
			this->balance = this->balance - amount;
			this->withdrawalsAllowed--;
			cout << "You have withdrawn : " << amount << "Your balance is : " << this->balance << endl;
		}
		else
		{
			cout << "Your amount : " << amount << " is too large it needs to be less then : " << this->interestGained << endl;
		}
	}
	else
	{
		cout << "I'm sorry your withdrawal limit has been reached" << endl;
	}
}

void CODAccount::display()
{
	cout << "COD Account :" << endl;
	cout << "Your interest rate is : " << interestRate << endl;
	cout << "Account Number : " << this->accountID << endl;
}
