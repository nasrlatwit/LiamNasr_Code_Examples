#pragma once
#include <string>
using std::string;
class Card
{
protected:
	string name;
	int card_number;
	string description;

public:
	// constructor
	Card();
	Card(string in_name, int in_card_number, string in_description);

	// method
	virtual string showname();
	virtual int showcardnumber();
	virtual string showdescription();

	// destructor
	~Card();
};