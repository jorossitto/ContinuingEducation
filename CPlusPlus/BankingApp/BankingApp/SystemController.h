#pragma once
//d) System Controller
//The system controller is central control unitand manages the main simulation.Once the system is
//initialized, the System Controller takes over.For each unit of simulation time, it should use the traffic
//generator to decide on customer arrivaland enqueueing them into the queue.It then simulates the
//service of the customer using the ATM machine.At a given time, the customer may start using the ATM
//machine, continue using the ATM machine or be done using the ATM machine.In the last case, the
//customer should be dequeuedand the next customer should begin using the ATM machine
class SystemController
{

private:
	int simulatedTime;
protected:

public:

};

