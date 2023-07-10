#pragma once
#include <iostream>
#include <string>
using std::string;

class fighter
{
	string name;
	int health;

public: 
	// constructtor (set initial value to each object 
	fighter(); // when user doesnt give any info --> default value
	fighter(string name);
	fighter(string name, int health);
	//method ( what can a fighter do)
	string show_name();
	int show_health();


	void punch(fighter& opp);
	void potion();
	void splash_potion(fighter& them);
	//destructor
	~fighter();

};

