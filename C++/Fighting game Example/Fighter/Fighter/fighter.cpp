#include "fighter.h"

fighter::fighter() {
	name = "Liam";
	health = 100;

}
fighter::fighter(string in_name) {
	name = in_name;
	health = 100;

}
fighter::fighter(string in_name, int in_health) {
	name = in_name;
	health = in_health;

}
string fighter::show_name() {
	return name;

}

int fighter::show_health() {
	return health;
}

void fighter::punch(fighter& opp) {
	opp.health = opp.health - 10;

}
void fighter::potion() {
	health=health + 20;
	
}
void fighter::splash_potion(fighter& opp) {
	opp.health = opp.health - 35;

}
//destructor 
fighter::~fighter() {

}