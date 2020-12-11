#include "Singleton.h"

Singleton::Singleton()
{
	std::cout << "Initalizing database" << endl;
	ifstream stream("capitals.txt");
	string name;
	string population;

	while (getline(stream, name))
	{
		getline(stream, population);
		capitals[name] = stoi(population);
	}
}

Singleton& Singleton::get()
{
	static Singleton db;
	return db;
}

void Singleton::print()
{
	for (auto it = capitals.cbegin(); it != capitals.cend(); ++it) 
	{
		std::cout << "{" << (*it).first << ": " << (*it).second << "}\n";
	}
}

map<string, int> Singleton::load()
{
	return capitals;
}

