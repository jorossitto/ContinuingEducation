#pragma once
//Certificates of Deposits
//• Require the account holder to make a deposit and agree to leave funds
//in the account for a specific amount of time
//• Interests are paid in return of the above - mentioned agreement.
//• Interests paid are higher than any of the afore - mentioned accounts.
//• Withdrawals may be allowed on the interest but only a limited number.
#include "Account.h"
class CODAccount:public Account
{
private:
	string codAccountString;
	int depositTime;
	int interestGained;
	int withdrawalsAllowed;
	//float defaultInterest = 1.10

	//float balance;
	//std::set<std::string> documentContents;
	//std::set<std::string> search;
	//int searchLength;
	//int documentLength;
	//double simScore;

public:
	CODAccount();
	void Withdraw(float amount);
	//void setWithdrawalsAllowed(int sumOfInterestGained);
	void display();
	//void AddInterest(float amount);
	//void printWords(std::string newString);
	//void addWords(std::string newString, std::set<std::string>& whatToAddTo);
	//double ComputeSim();
	//auto GetDocument() { return documentContents; }
	//auto GetSimScore() { return simScore; }
};

