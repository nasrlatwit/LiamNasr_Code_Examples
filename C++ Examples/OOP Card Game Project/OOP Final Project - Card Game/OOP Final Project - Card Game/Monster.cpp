#include "Monster.h"
#include <iostream>
using std::cout;
using std::endl;
Monster::Monster() {
	attack_points = 0;
	defense_points = 0;

}

Monster::Monster(int in_num) {
	attack_points = 0;
	defense_points = 0;
	if (in_num == 1) {
		name = "Dark Magician";
		description = "Attack Points: 2500   ||   Defense Points: 2100";
		card_number = 1;
		attack_points = 2500;
		defense_points = 2100;
	}
	// Mystical Elf
	else if (in_num == 2) {
		name = "Mystical Elf";
		description = "Attack Points: 800   ||   Defense Points: 2000";
		card_number = 2;
		attack_points = 800;
		defense_points = 2000;
	}
	// Feral Imp
	else if (in_num == 3) {
		name = "Feral Imp";
		description = "Attack Points: 1300   ||   Defense Points: 1400";
		card_number = 3;
		attack_points = 1300;
		defense_points = 1400;
	}
	// Beta the Magnet Warrior
	else if (in_num == 4) {
		name = "Beta the Magnet Warrior";
		description = "Attack Points: 1700   ||   Defense Points: 1600";
		card_number = 4;
		attack_points = 1700;
		defense_points = 1600;
	}
	// Blue Flamed Swordsman
	else if (in_num == 5) {
		name = "Blue Flamed Swordsman";
		description = "Attack Points: 1800   ||   Defense Points: 1600";
		card_number = 5;
		attack_points = 1800;
		defense_points = 1600;
	}
	// Mystic Crown
	else if (in_num == 6) {
		name = "Mystic Crown";
		description = "Attack Points: 1500   ||   Defense Points: 1000";
		card_number = 6;
		attack_points = 1500;
		defense_points = 1000;
	}
	// D. Human
	else if (in_num == 7) {
		name = "D. Human";
		description = "Attack Points: 1300   ||   Defense Points: 1100";
		card_number = 7;
		attack_points = 1300;
		defense_points = 1100;
	}
	// Speed Warrior
	else if (in_num == 8) {
		name = "Speed Warrior";
		description = "Attack Points: 800   ||   Defense Points: 800";
		card_number = 8;
		attack_points = 800;
		defense_points = 800;
	}
	// Warlock Child
	else if (in_num == 9) {
		name = "Warlock Child";
		description = "Attack Points: 500   ||   Defense Points: 1500";
		card_number = 9;
		attack_points = 500;
		defense_points = 1500;
	}
	// Blood Ronin
	else if (in_num == 10) {
		name = "Blood Ronin";
		description = "Attack Points: 1800   ||   Defense Points: 100";
		card_number = 10;
		attack_points = 1800;
		defense_points = 100;
	}
	// Angelic Fiend
	else if (in_num == 11) {
		name = "Angelic Fiend";
		description = "Attack Points: 1000   ||   Defense Points: 1000";
		card_number = 11;
		attack_points = 1000;
		defense_points = 1000;
	}
}

// method
string Monster::showname() {
	return name;
}

int Monster::showcardnumber() {
	return card_number;
}

string Monster::showdescription() {
	return description;
}

int Monster::showattackpoints() {
	return attack_points;
}

int Monster::showdefensepoints() {
	return defense_points;
}

// destructor
Monster::~Monster() {

}