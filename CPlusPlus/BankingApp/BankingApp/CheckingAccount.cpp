#include "CheckingAccount.h"

CheckingAccount::CheckingAccount(float balance, std::string SSN) : Account(balance, 1, SSN)
{
	checking_acc_count++;
	string s_a_c = to_string(checking_acc_count);
	this->accountID = accountID + 'P' + s_a_c + 'S';
}

CheckingAccount::CheckingAccount()
{
	checking_acc_count++;
	string s_a_c = to_string(checking_acc_count);
	checking_acc_count++;
	string a_c = to_string(account_count);
	this->accountID = 'A' + a_c + 'P' + s_a_c + 'S';
	SSN = "12345";
}
void CheckingAccount::display()
{
	cout << "This is Personal Checking Account" << endl;
	cout << "Account number: " << accountID << endl;
	std::cout << "Balance: " << balance << endl;
	cout << "SSN: " << SSN << endl << endl;
}
