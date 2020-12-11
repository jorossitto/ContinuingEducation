#include "Partition.h"

Partition::Partition()
{
}

void Partition::setATM(ATM *atmPointer)
{
	this->atmPointer = atmPointer;
}

void Partition::setPartition(Partition* nextPartition)
{
	this->nextPartition = nextPartition;
}

ATM* Partition::getATM()
{
	return this->atmPointer;
}

Partition* Partition::getPartition()
{
	return this->nextPartition;
}
