#pragma once

//Money Market Account
//• Pays higher interest rate than any of the above accounts
//• Requires minimum balance for the account to start earning interests.
//• Withdrawals are limited(e.g.six per month).
#include "Account.h"
class MoneyMarketAccount: public Account
{
private:
	float minimumBalance;
	int withdrawalLimit = 6;

	//float balance;

	//std::set<std::string> documentContents;
	//std::set<std::string> search;
	//int searchLength;
	//int documentLength;
	//double simScore;

public:
	MoneyMarketAccount();
	void display();
	//void AddInterest(float amount);
	//void printWords(std::string newString);
	//void addWords(std::string newString, std::set<std::string>& whatToAddTo);
	//double ComputeSim();
	//auto GetDocument() { return documentContents; }
	//auto GetSimScore() { return simScore; }
};

