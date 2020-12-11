#pragma once
#include "CheckingAccount.h"
#include <iostream>
#include <array>

//Foreign Currency Accounts : Same as Checking Account but would let the user
//deposit in a currency other than dollars.You can choose five world currencies of
//your choiceand use the current exchange rates to implement this feature.
class ForeignCurrencyAccount: public CheckingAccount
{
private:
	
	double exchangeRate[5] = {.85, 6.65, .77, 20.98, 1.31 };
	//float balanceInDollars = exchangeRate[0]

public:
	enum currency { Euro = 0, Yuan = 1, Pound = 2, Peso = 3, CanadianDollar = 4 };
	ForeignCurrencyAccount();
	void display();
	float toDollars(float amount);
	float fromDollars(float amount);
};

