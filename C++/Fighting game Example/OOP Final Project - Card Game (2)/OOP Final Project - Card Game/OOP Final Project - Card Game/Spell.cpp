#include "Spell.h"
#include "Player.h"
#include <iostream>
using std::cout;
using std::endl;
Spell::Spell() {

}

Spell::Spell(int in_num) {
	// Brain Control
	if (in_num == 1) {
		name = "Brain Control";
		card_number = 12;
		description = "Pay 800 life points, and gain control of your opponents monster for one turn.";
		
	}
	
	// Horn of the Unicorn
	else if (in_num == 2) {
		name = "Horn of the Unicorn";
		card_number = 13;
		description = "Add 700 attack points to any one of your monsters.";
	}
	// Swords of Revealing Light
	else if (in_num == 3) {
		name = "Swords of Revealing Light";
		card_number = 14;
		description = "All cards flip face up, opponent cannot attack for three turns.";
	}
	
	// Dark Hole
	else if (in_num == 4) {
		name = "Dark Hole";
		card_number = 15;
		description = "Destroy ALL monsters on both sides of field.";
	}
	// Half Point
	else if (in_num == 5) {
		name = "Half Point";
		card_number = 16;
		description = "Halve a monsters attack";
	}
	
	// Armor Chest
	else if (in_num == 6) {
		name = "Armor Chest";
		card_number = 17;
		description = "Add 300 points to a monsters attack and defense.";
	}
	
	// Chariot Lance
	else if (in_num == 7) {
		name = "Chariot Lance";
		card_number = 18;
		description = "Be able to attack your opponent directly with half your monsters attack points.";
	}
}

void Spell::apply(int card_num, Monster& target) {
	// Brain Control
	if (card_num == 12) {
		cout << "The user has activated brain control" << endl;
		cout << "The user pays 800 health points to lower the opponents attack to zero!"<<endl;
		target.attack_points = 0;
	}
	
	// Horn of the Unicorn
	else if (card_num == 13) {
		
		cout << "Horn of the Unicorn has Added 700 attack points to your monster!" << endl;
		target.attack_points = target.attack_points + 700;
	
	}
	// Swords of Revealing Light
	else if (card_num == 14) {

		cout<<"Swords of Revealing Light Adds Half of your defense points to your attack"<<endl;
		target.attack_points = target.attack_points + (target.defense_points / 2);

	}

	// Dark Hole
	else if (card_num == 15) {
		
		cout << "Dark Hole has been played." << endl;
		cout << "The battle field has been erased." << endl;
		cout << "No monsters are left to battle." << endl;

	}
	// Shield and Sword
	else if (card_num == 16) {
		
		target.attack_points = target.attack_points / 2;
		cout << "The Half point spell has cuts your opponents attack in half!" << endl;
		
	}
	
	// Armor Chest
	else if (card_num == 17) {
		cout << "Armour Chest has buffed your monsters attack!";
		target.attack_points = target.attack_points + 300;
		
	}
	
	// Chariot Lance
	else if (card_num == 18) {
		
		target.attack_points = target.attack_points / 2;
		cout << "Chariot Lance Activated!" << endl;
		cout << "You attack your opponent directly" << endl;


	}
}
// method
string Spell::showname() {
	return name;
}

int Spell::showcardnumber() {
	return card_number;
}

string Spell::showdescription() {
	return description;
}

// destructor
Spell::~Spell() {

}