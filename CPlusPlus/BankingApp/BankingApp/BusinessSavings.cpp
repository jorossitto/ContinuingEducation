#include "BusinessSavings.h"

BusinessSavings::BusinessSavings()
{
	b_savings_acc_count++;
	string b_s_a_c = to_string(b_savings_acc_count);
	account_count++;
	string a_c = to_string(account_count);
	this->accountID = 'A' + a_c + 'B' + b_s_a_c + 'S';
	this->AddInterest();
	this->accountType = "Business Savings";
}

void BusinessSavings::AddInterest()
{
	if (balance > 10000)
	{
		interestRate = 11.0;
	}
	else
	{
		interestRate = 8.5;
	}
}
void BusinessSavings::display()
{
	cout << "This is Business Savings Acccount" << endl;
	cout << "Account number: " << accountID << endl;
	std::cout << "Balance: " << balance << endl;
	cout << "Interest Rate: " << interestRate << endl;
	cout << "SSN: " << SSN << endl << endl;
	Deposit(100000,accountID);
	AddInterest();
	cout << "New Interest Rate " << interestRate << endl;
	Withdraw(99900, accountID);
	Withdraw(90, accountID);
	cout << endl;

}
void BusinessSavings::Withdraw(float amount, string accountID)
{
	freeWithdrawalsLeft--;
	if (freeWithdrawalsLeft >=0)
	{
		cout << "Withdrawing " << amount << " from " << accountID << endl;
		cout << "Free Withdrawals left = " << freeWithdrawalsLeft << endl;
		this->balance = this->balance - amount;
		cout << "Your new balance is " << this->balance << endl;
	}
	else
	{
		cout << "Withdrawing " << amount << " from " << accountID << endl;
		cout << "You will be charged for this transaction : " << withdrawalFee<<endl;
		cout << "Withdrawing " << amount <<"+"<< withdrawalFee << " from " << accountID << endl;
		this->balance = this->balance - amount - withdrawalFee;
		cout << "Your new balance is " << this->balance << endl;
	}
	
}