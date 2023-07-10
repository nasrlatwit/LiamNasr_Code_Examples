#pragma once
#include <string>
using std::string;
class Player
{

	friend class Spell;
	// attributes
	string name;
	int health;

public:
	// constructor
	Player();
	Player(string in_name, int in_health);

	// method
	string showname();
	int showhealth();
	void addhealth(int in_num);
	void removehealth(int in_num);

	// destructor
	~Player();
};