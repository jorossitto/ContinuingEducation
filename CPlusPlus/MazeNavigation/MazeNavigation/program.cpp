//a.File Name - program.cpp
//b.Author - Joseph Rossitto
//c.Date - 9/30/20
//d.Compiler Used - Visual Studio
//e.Brief Description of the file - Contains the main program, and how to deal with data passed in from mazeData.txt

#include <iostream>
#include <string>
#include <fstream>
#include "matrix.h"

using namespace std;
void readFile(string mazeNumber);

int main()
{
	//matrix m1(2, 3), m2(2, 3), m3(2, 3);
	//m1(0, 0) = 5;
	//m2(0, 0) = 7;
	//m3 = m2;
	//cout << m3(0, 0) << endl;
	//m3 += m1;
	//cout << "Now m3(0,0) = " << m3(0, 0);
	string maze;
	cout << "What Maze To run? 1/2/3:";
	cin >> maze;

	string maze1 = "data1.txt";
	string maze2 = "data2.txt";
	string maze3 = "data3.txt";
	string mazeNumber;

	if (maze == "1")
	{
		mazeNumber = maze1;
	}
	if (maze == "2")
	{
		mazeNumber = maze2;
	}
	if (maze == "3")
	{
		mazeNumber = maze3;
	}

	readFile(mazeNumber);
	return 0;
}

void readFile(string mazeNumber)
{
	string mazeData;
	bool timeToCreateMaze = true;
	bool timeToPlaceEntrance = false;
	bool timeToPlaceExit = false;
	bool timeToPlaceObsticals = false;
	bool timeToEndProgram = false;
	bool fullString = false;
	bool lookingForX = true;
	bool lookingForY = false;



	int x = 0;
	int y = 0;
	//int x = 6;
	//int y = 5;

	int currentX = 0;
	int currentY = 0;

	int endX = 0;
	int endY = 0;

	int maxX = 0;
	int maxY = 0;


	ifstream inFile;
	matrix mazeBuilder;

	//Criteria 1: Use file io
	inFile.open(mazeNumber);
	if (!inFile) {
		cout << "Unable to open file";
		exit(1); // terminate with error
	}

	while (inFile >> mazeData)
	{
		//cout << "Maze Data: " << mazeData << endl;

		for (char& c : mazeData)
		{
			if (c == '-')
			{
				timeToPlaceObsticals = false;
				timeToEndProgram = true;
			}
			if (c != '(' 
				&& c != ')' 
				&& c != ',')
			{
				if (lookingForX == true)
				{
					lookingForX = false;
					lookingForY = true;
					fullString = false;
					x = ((int)c - '0' -1);
				}
				else
				{
					lookingForX = true;
					lookingForY = false;
					fullString = true;
					y = ((int)c - '0' -1);
				}
			}
		}
		if (timeToCreateMaze == true && fullString == true)
		{
			timeToCreateMaze = false;
			timeToPlaceEntrance = true;
			
			//cout << mazeBuilder;

			matrix initializeMaze(x+1, y+1);
			mazeBuilder = initializeMaze;

			//matrix newMaze(initializeMaze);
			//matrix mazeBuilder(initializeMaze);

			//cout << "building maze: " << x << y << endl;
		}
		else if (timeToPlaceEntrance == true && fullString == true)
		{
			timeToPlaceEntrance = false;
			timeToPlaceExit = true;
			mazeBuilder(x, y) = 1;
			currentX = x;
			currentY = y;

			//cout << "Placing Entrance: " << x << y << endl;
		}
		else if (timeToPlaceExit == true && fullString == true)
		{
			timeToPlaceExit = false;
			timeToPlaceObsticals = true;
			endX = x;
			endY = y;
			mazeBuilder(x, y) = 2;
			//cout << "Placing Exit: " << x << y << endl;
		}
		else if(timeToPlaceObsticals == true && fullString == true)
		{
			mazeBuilder(x, y) = 3;
			//cout << "placing obstical " << x << y << endl;
		}
		else if (timeToEndProgram == true)
		{
			//cout << "All Data is read" << endl;
			bool finished = false;
			int count = 0;
			bool moveUpOpen = false;
			bool shouldMoveUp = false;
			bool moveLeftOpen = false;
			bool shouldMoveLeft = false;
			bool shouldMoveRight = false;
			bool moveRightOpen = false;
			bool moveDownOpen = false;
			bool shouldMoveDown = false;
			//Swap current X and current Y
			//int temp = currentX;
			//currentX = currentY;
			//currentY = temp;

			while (finished == false)
			{
				if (currentX < endX)
				{
					moveRightOpen = mazeBuilder(currentX + 1, currentY) != 3;
					shouldMoveRight = currentX < endX;
				}
				else
				{
					moveRightOpen = false;
				}

				if (currentY < endY)
				{
					moveDownOpen = mazeBuilder(currentX, currentY + 1) != 3;
					shouldMoveDown = currentY < endY;
				}
				else
				{
					moveDownOpen = false;
				}


				if (currentY != 0)
				{
					moveUpOpen = mazeBuilder(currentX, currentY - 1) != 3;
					shouldMoveUp = currentY > endY;
				}
				else
				{
					moveUpOpen = false;
				}

				if (currentX != 0)
				{
					moveLeftOpen = mazeBuilder(currentX - 1, currentY) != 3;
					shouldMoveLeft = currentX > endX;
				}
				else
				{
					moveLeftOpen = false;
				}
				
				

				//cout << " current x: " << currentX << " current y: " << currentY << " end x: " << endX << " end y: " << endY << endl;

				count = count + 1;
				cout << "================= Step " << count << " =================" << endl;
				cout << mazeBuilder;
				if (moveRightOpen && shouldMoveRight)
				{
					//cout << "Moving Right" << endl;
					mazeBuilder(currentX, currentY) = 0;
					mazeBuilder(currentX + 1, currentY) = 1;
					currentX = currentX + 1;
					moveRightOpen = false;
					shouldMoveRight = false;
				}
				else if (moveDownOpen && shouldMoveDown)
				{
					//cout << "Moving Down" << endl;
					mazeBuilder(currentX, currentY) = 0;
					mazeBuilder(currentX, currentY + 1) = 1;
					currentY = currentY + 1;
					moveDownOpen = false;
					shouldMoveDown = false;
				}
				else if (moveLeftOpen && shouldMoveLeft)
				{
					//cout << "Moving Down" << endl;
					mazeBuilder(currentX, currentY) = 0;
					mazeBuilder(currentX - 1, currentY) = 1;
					currentX = currentX - 1;
					moveLeftOpen = false;
					shouldMoveLeft = false;
				}
				else if (moveUpOpen && shouldMoveUp)
				{
					//cout << "Moving Down" << endl;
					mazeBuilder(currentX, currentY) = 0;
					mazeBuilder(currentX, currentY - 1) = 1;
					currentY = currentY - 1;
					moveUpOpen = false;
					shouldMoveUp = false;
				}
				else
				{
					cout << "Current X" << currentX << " End X: " << endX << "move right open: " << moveRightOpen << "should move right: " << shouldMoveRight << endl;
					cout << "Current Y" << currentY << " End Y: " << endY;
					cout << "Help I am stuck!" << endl;
				}

				if (currentX == endX && currentY == endY)
				{
					finished = true;
					count = count + 1;
					cout << "================= Step " << count << " =================" << endl;
					cout << mazeBuilder;
					//cout << "Yay we are done";
				}
				if (count > 20)
				{
					finished = true;
					cout << "break here and check program" << endl;
				}
			}
		}
		else
		{
			//cout << "Error error will robinson";
		}
	}
}