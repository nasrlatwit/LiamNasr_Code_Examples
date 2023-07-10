#include <iostream>
#include <string>
#include "fighter.h"

using std::cin;
using std::cout;
using std::string;
using std::endl;


int main() {
	// start a game
	//create a fighter
	fighter player1;

	//display data of player 1
	cout << player1.show_name() << " (health) " << player1.show_health() << endl;

	// create player 2
	cout << "Enter a second player: "<< endl;
	string username;
	cin >> username;

	fighter player2(username);
	//display player 2
	cout << player2.show_name() << " (health) " << player2.show_health() << endl;

	//create player 3
	fighter player3("John", 66);
	//display player 3
	cout << player3.show_name() << " (health) " << player3.show_health() << endl;

	//play 1 punch player 3
	cout << "Player 3 has been punched!"<<endl;
	player1.punch(player3);
	cout << player3.show_name() << " (health) " << player3.show_health() << endl;
	
	//player 3 drinks a potion
	cout << "Player 3 drinks a potion!"<< endl;
	player3.potion();
	cout << player3.show_name() << " (health) " << player3.show_health() << endl;

	//player 3 splashes player1
	cout << "Player 3 splashes player 1!" << endl;
	player3.splash_potion(player1);
	cout << player1.show_name() << " (health) " << player1.show_health() << endl;


	//destructor 
	/*player1.~fighter();
	cout << player1.show_name() << "\n";
	cout << " (health) " << player1.show_health();
	*/




}

