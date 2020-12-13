#include "HighVolumeCheckingAccount.h"

HighVolumeCheckingAccount::HighVolumeCheckingAccount()
{
	hvc_checking_acc_count++;
	string hvc_s_a_c = to_string(hvc_checking_acc_count);
	account_count++;
	string a_c = to_string(account_count);
	this->accountID = 'A' + a_c + 'B' + hvc_s_a_c + "HV";
	this->accountType = "High Volume Checking Account";
}

void HighVolumeCheckingAccount::display()
{
	cout << "This is High Volume Checking Account" << endl;
	cout << "Account number: " << accountID << endl;
	std::cout << "Balance: " << balance << endl;
	cout << "SSN: " << SSN << endl << endl;
	Deposit(100, accountID);
	Deposit(10, accountID);
	Withdraw(1, accountID);
	Withdraw(1, accountID);
	cout << endl;
}

void HighVolumeCheckingAccount::Withdraw(float amount, string accountID)
{
		cout << "Withdrawing " << amount << " from " << accountID << endl;
		this->balance = this->balance - amount;
		cout << "Your new balance is " << this->balance << endl;

}
void HighVolumeCheckingAccount::Deposit(float amount, string accountID)
{
	
		cout << "Depositing " << amount << " to " << accountID << endl;
		cout << "Transaction charge = " << DepositFee << endl;
		cout << "Total Amount =" << amount - DepositFee << endl;
		this->balance = this->balance + amount -DepositFee;
		cout << "Your new balance is " << this->balance << endl;
	
}