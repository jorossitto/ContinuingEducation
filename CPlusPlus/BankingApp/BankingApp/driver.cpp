#include "driver.h"
#include "TrafficGenerator.h"
#include "Bank.h"

using namespace std;

int main()
{
	//testingRegularAccount();
	//testingSavingsAccount();
	//testingCheckingAccount();

	//---------------------------------------------------------------------------------------------------------------------------------
	//static int test;
	//test = test + 1;
	//cout << test << endl;

	//testAccounts();
	
	//--------------------------------------------------------------------------------------------------------------------------------
	//TrafficGenerator trafficGenerator = TrafficGenerator();
	
	int ATMs, time;
	ATMs = 2;
	string fname = "test string";
	Bank* mybank = new Bank(ATMs, fname);
	//cout << "Please specify input file name:\n";
	//cin >> fname;
	//mybank.set_inputfile(fname);
	//cout << "Number of ATMs:\n";
	//cin >> ATMs; // input 1 for this part
	
	//mybank.set_atm_num(ATMs);
	//cout << "Simulation time:\n";
	//cin >> time;
	time = 200;
	//mybank.set_sim_time(time);
	//mybank.generate_customerbase(); // Traffic Generator
	//mybank.generate_initial_traffic(); // Traffic Generator
	//mybank.simulate(); // System Controller
	//mybank.report(); // Statistic Keeper
	TimingWheel* timingWheel = new TimingWheel(mybank);

	TrafficGenerator trafficGenerator = TrafficGenerator(mybank, timingWheel);
	trafficGenerator.RunSimulation();

	return 0;
}

void testAccounts()
{
	Account* accounts[8];
	accounts[0] = new SavingsAccount();
	accounts[1] = new CheckingAccount();
	accounts[2] = new MoneyMarketAccount();
	accounts[3] = new CODAccount();
	accounts[4] = new BusinessSavings();
	accounts[5] = new BusinessChecking();
	accounts[6] = new HighVolumeCheckingAccount();
	accounts[7] = new ForeignCurrencyAccount();
	Account acc;
	acc.display();

	for (int i = 0; i < 7; i++)
	{
		accounts[i]->display();
	}
}

void testingCheckingAccount()
{
	cout << "Testing Checking Account" << endl;
	CheckingAccount checkingAccount(0, "000");
	accountTest(checkingAccount);
}

void testingSavingsAccount()
{
	cout << "Testing Savings Account" << endl;
	SavingsAccount savingsAccount(0, 1.1, "000");
	accountTest(savingsAccount);
}

void testingRegularAccount()
{
	cout << "Testing Account" << endl;
	Account account(0, 1.1, "000");
	accountTest(account);
}

void accountTest(Account& account)
{
	cout << account;
	account.Deposit(100, "1234");
	account.AddInterest();
	account.Withdraw(50, "1234");
	cout << account;
}
