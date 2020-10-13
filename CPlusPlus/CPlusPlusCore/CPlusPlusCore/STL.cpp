#include "STL.h"
// copyit.cpp -- copy() and iterators
#include <iostream>
#include <iterator>
#include <vector>
#include <string>
#include <memory>
#include <algorithm>
#include <list>

int STL::CopyItMain()
{
    using namespace std;

    int casts[10] = { 6, 7, 2, 9 ,4 , 11, 8, 7, 10, 5 };
    vector<int> dice(10);

    // copy from array to vector
    copy(casts, casts + 10, dice.begin());
    cout << "Let the dice be cast!\n";

    // create an ostream iterator
    ostream_iterator<int, char> out_iter(cout, " ");

    // copy from vector to output
    copy(dice.begin(), dice.end(), out_iter);
    cout << endl;
    cout << "Implicit use of reverse iterator.\n";
    copy(dice.rbegin(), dice.rend(), out_iter);
    cout << endl;
    cout << "Explicit use of reverse iterator.\n";

    // vector<int>::reverse_iterator ri;  // use if auto doesn't work
    for (auto ri = dice.rbegin(); ri != dice.rend(); ++ri)
        cout << *ri << ' ';
    cout << endl;
    // cin.get();
    return 0;
}

int STL::FowlMain()
{
    using namespace std;

    auto_ptr<string> films[5] =
    {
        auto_ptr<string>(new string("Fowl Balls")),
        auto_ptr<string>(new string("Duck Walks")),
        auto_ptr<string>(new string("Chicken Runs")),
        auto_ptr<string>(new string("Turkey Errors")),
        auto_ptr<string>(new string("Goose Eggs"))
    };

    cout << "The nominees for best avian baseball film are\n";
    for (int i = 0; i < 5; i++)
    {
        cout << *films[i] << endl;
    }

    auto_ptr<string> pwin;
    pwin = films[2];   // films[2] loses ownership

    cout << "The winner is " << *pwin << "!\n";
    // cin.get();
    return 0;
}

int STL::InsertsMain()
{
    return 0;
}

void STL::print(std::string& s)
{
    std::cout << s << " ";
}

int STL::ListMain()
{
    //using namespace std;
    //list<int> one(5, 2); // list of 5 2s
    //int stuff[5] = { 1,2,4,8, 6 };
    //list<int> two;
    //two.insert(two.begin(), stuff, stuff + 5);
    //int more[6] = { 6, 4, 2, 4, 6, 5 };
    //list<int> three(two);
    //three.insert(three.end(), more, more + 6);
    //cout << "List one: ";
    //for_each(one.begin(), one.end(), STL::outint);
    //cout << endl << "List two: ";
    //for_each(two.begin(), two.end(), STL::outint);
    //cout << endl << "List three: ";
    //for_each(three.begin(), three.end(), STL::outint);
    //three.remove(2);
    //cout << endl << "List three minus 2s: ";
    //for_each(three.begin(), three.end(), STL::outint);
    //three.splice(three.begin(), one);
    //cout << endl << "List three after splice: ";
    //for_each(three.begin(), three.end(), STL::outint);
    //cout << endl << "List one: ";
    //for_each(one.begin(), one.end(), STL::outint);
    //three.unique();
    //cout << endl << "List three after unique: ";
    //for_each(three.begin(), three.end(), STL::outint);
    //three.sort();
    //three.unique();
    //cout << endl << "List three after sort & unique: ";
    //for_each(three.begin(), three.end(), STL::outint);
    //two.sort();
    //three.merge(two);
    //cout << endl << "Sorted two merged into three: ";
    //for_each(three.begin(), three.end(), STL::outint);
    //cout << endl;
    return 0;
}
