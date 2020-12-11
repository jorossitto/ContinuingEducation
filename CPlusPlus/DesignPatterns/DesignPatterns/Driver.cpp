//a.File Name - Driver.cpp
//b.Author - Joseph Rossitto
//c.Date - 11-27-20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Main file used for driving the program.

#include "Singleton.h"
#include "Adaptor.h"
#include "State.h"
#include <iterator>

using namespace std;

int main()
{
	auto& db = Singleton::get();
    map<string, int> capitals;
    capitals = db.load();
    int imigrantPool = 0;
    Adaptor adaptor = Adaptor();


    for (auto it = capitals.cbegin(); it != capitals.cend(); ++it)
    {
        std::cout << "{" << (*it).first << ": " << adaptor.toMillions((*it).second) << "}" << endl;
    }
    cout << endl;

    map<State, vector<pair<Trigger, State>>> rules;

    rules[State::Off] = 
    {
      {Trigger::Closed, State::Off},
      {Trigger::Welcome, State::On}
    };
    rules[State::On] = 
    {
      {Trigger::Welcome, State::On},
      {Trigger::Closed, State::Off}
    };

    State currentState{ State::On },
        exitState{ State::Off };

    while (true)
    {
        cout << "We are currently adding " << imigrantPool << " million immigrants " << endl;
        cout << "Our current status is " << currentState << endl;
        imigrantPool = imigrantPool + 10;
    select_trigger:
        cout << "Select a state:" << endl;

        int i = 0;
        for (auto item : rules[currentState])
        {
            cout << i++ << ". " << item.first << endl;
        }

        int input;
        cin >> input;
        if (input < 0 || (input + 1) > rules[currentState].size())
        {
            cout << "Incorrect option. Please try again." << endl;
            goto select_trigger;
        }

        currentState = rules[currentState][input].second;
        if (currentState == exitState) break;
    }

    cout << "We are now closed for immigrantion" << endl << endl;
    int size = capitals.size();
    int immigrants = imigrantPool / size;

    for (auto it = capitals.cbegin(); it != capitals.cend(); ++it)
    {
        std::cout << "{" << (*it).first << ": " << adaptor.toMillions((*it).second + immigrants) << "}\n";
    }

    getchar();
	return 0;
}
