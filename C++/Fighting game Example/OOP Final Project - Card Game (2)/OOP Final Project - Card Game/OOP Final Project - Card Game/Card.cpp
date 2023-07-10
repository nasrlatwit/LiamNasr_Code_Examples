#include "Card.h"

Card::Card() {
	card_number = 0;
}

Card::Card(string in_name, int in_card_number, string in_description) {
	name = in_name;
	card_number = in_card_number;
	description = in_description;
}

string Card::showname() {
	return name;
}

int Card::showcardnumber() {
	return card_number;
}

string Card::showdescription() {
	return description;
}

Card::~Card() {

}