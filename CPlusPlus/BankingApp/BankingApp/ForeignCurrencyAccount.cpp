#include "ForeignCurrencyAccount.h"

ForeignCurrencyAccount::ForeignCurrencyAccount()
{
	this->accountType = "Foreign Currency Account";
}

void ForeignCurrencyAccount::display()
{
	cout << "This is Foreign Currency Account" << endl;
}