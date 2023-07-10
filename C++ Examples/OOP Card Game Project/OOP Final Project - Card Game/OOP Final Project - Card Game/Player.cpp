#include "Player.h"
Player::Player() {
	health = 0;
}

Player::Player(string in_name, int in_health) {
	name = in_name;
	health = in_health;
}

// method
string Player::showname() {
	return name;
}

int Player::showhealth() {
	return health;
}

void Player::addhealth(int in_num) {
	health = health + (in_num);
}

void Player::removehealth(int in_num) {
	health = health - (in_num);
}

// destructor
Player::~Player() {

}