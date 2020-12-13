#include "BusinessChecking.h"

BusinessChecking::BusinessChecking()
{
	b_checking_acc_count++;
	string b_s_a_c = to_string(b_checking_acc_count);
	account_count++;
	string a_c = to_string(account_count);
	this->accountID = 'A' + a_c + 'B' + b_s_a_c + 'C';
	this->accountType = "Business Checking";
}

void BusinessChecking::display()
{
	cout << "This is Business Checking Account" << endl;
	cout << "Account number: " << accountID << endl;
	std::cout << "Balance: " << balance << endl;
	cout << "SSN: " << SSN << endl << endl;
	Deposit(100000, accountID);
	Deposit(1, accountID);
	Withdraw(99900, accountID);
	Withdraw(90, accountID);
	cout << endl;
}

void BusinessChecking::Withdraw(float amount, string accountID)
{
	freeWithdrawalsLeft--;
	if (freeWithdrawalsLeft >= 0)
	{
		cout << "Withdrawing " << amount << " from " << accountID << endl;
		cout << "Free Withdrawals left = " << freeWithdrawalsLeft << endl;
		this->balance = this->balance - amount;
		cout << "Your new balance is " << this->balance << endl;
	}
	else
	{
		cout << "Withdrawing " << amount << " from " << accountID << endl;
		cout << "You will be charged for this transaction : " << withdrawalFee << endl;
		cout << "Withdrawing " << amount << "+" << withdrawalFee << " from " << accountID << endl;
		this->balance = this->balance - amount - withdrawalFee;
		cout << "Your new balance is " << this->balance << endl;
	}
}
void BusinessChecking::Deposit(float amount, string accountID)
{
	freeDeposit--;
	if (freeDeposit >= 0)
	{
		cout << "Depositing " << amount << " to " << accountID << endl;
		cout << "Free Deposits left = " << freeDeposit << endl;
		this->balance = this->balance + amount;
		cout << "Your new balance is " << this->balance << endl;
	}
	else
	{
		cout << "Depositing " << amount << " to " << accountID << endl;
		cout << "You will be charged for this transaction : " << DepositFee << endl;
		cout << "Depositing " << amount << "-" << DepositFee << " to " << accountID << endl;
		this->balance = this->balance + amount - DepositFee;
		cout << "Your new balance is " << this->balance << endl;
	}
}