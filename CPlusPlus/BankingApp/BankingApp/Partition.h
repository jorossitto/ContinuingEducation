#include "ATM.h"
#pragma once
class Partition
{
private:
	ATM *atmPointer;
	Partition *nextPartition;
public:
	Partition();
	void setATM(ATM *atmPointer);
	void setPartition(Partition* nextPartition);
	ATM* getATM();
	Partition* getPartition();

};

