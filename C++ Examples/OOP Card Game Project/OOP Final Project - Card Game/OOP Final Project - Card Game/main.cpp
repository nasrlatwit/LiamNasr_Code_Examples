// Liam Nasr
// Object Oriented Programming Final Project
// Advanced Card Game (Yu-Gi-Oh-based Card Game)

// 12 December 2022

#include <iostream>
#include <string>
#include <list>
#include <cstdlib>
#include "Player.h"
#include "Card.h"
#include "Monster.h"
#include "Spell.h"


using std::cin;
using std::cout;
using std::string;
using std::list;
using std::getline;
using std::endl;

int loss(int greater, int lesser);

int main() {
	srand((unsigned)time(NULL));
	int cardnum;
	int card_number=0;
	int deck_check = 0;
	int card_per_turn = 0;
	int startgame;
	int place_card=0;
	int cardplace=0;
	int cpu_card = 0;

	string test;

	cout << "||** Welcome to our Yu-Gi-Oh-Based Card Game **||" << endl;
	cout << "Enter your username: ";
	string username;
	getline(cin, username);

	cout << "Welcome " << username << "!" << endl;

	Player user(username, 4000);
	Player computer("VILLAIN", 4000);
	
	

	
	


	list <Card> player_deck;
	list <Card> computer_deck;
	
	

	while (1) {
		cout << "\nWould you like to start a new game?" << endl;
		cout << "1 - Yes" << endl;
		cout << "2 - Exit" << endl;
		cin >> startgame;

		// ADDING MONSTER CARDS TO PLAYER DECK
		for (int i = 0; i < 5; i++) {
			// here, we will draw a deck of 3 monster cards
			cardnum = 1 + (rand() % 11);
			player_deck.push_back(Monster(cardnum));
		}

		// ADDING SPELL CARDS TO PLAYER DECK
		for (int i = 0; i < 2; i++) {
			// here, we will draw a deck of 2 spell cards
			cardnum = 1 + (rand() % 7);
			player_deck.push_back(Spell(cardnum));
		}

		// ADDING MONSTER CARDS TO COMPUTER DECK
		for (int i = 0; i < 7; i++) {
			// here, we will draw a deck of 3 monster cards
			cardnum = 1 + (rand() % 11);
			computer_deck.push_back(Monster(cardnum));
		}
		

		// STARTING THE GAME
		if (startgame == 1) {
			// DEFINING NEW COMPUTER OPPONENT
			Player computer("VILLAIN", 4000);
			cout << "\n||** STARTING NEW GAME **||\n\n";
			while (1) {
				// Player Selection Tools
				while (1) {
					if (user.showhealth() > 0) {
						int test = 0;
						int choice;
						cout << "\nPlease select one of the options:";
						cout << "\n1 - Draw a New Card (Once Per Turn)";
						cout << "\n2 - View Cards";
						cout << "\n3 - View Card Information";
						cout << "\n4 - View Rules";
						cout << "\n5 - Set a Card Down";
						cout << "\n6 - Next Phase" << endl;
						cin >> choice;
						cout << endl;

						// Draw a New Card from Deck
						if (choice == 1) {
							if (deck_check == 1) {
								cout << "You've already drawn a deck of cards. Please select another option, or move on to next turn.\n";
							}
							else {
								int draw_new_card = 1 + (rand() % 2);

								// DRAWING A RANDOM MONSTER CARD
								if (draw_new_card == 1) {
									cardnum = 1 + (rand() % 11);
									player_deck.push_back(Monster(cardnum));
								}
				
								// DRAWING A RANDOM SPELL CARD
								else if (draw_new_card == 2) {
									cardnum = 1 + (rand() % 7);
									player_deck.push_back(Spell(cardnum));
								}

								deck_check = 1;
								cout << "A new card has been added to your deck!\n";
							}

						}
						// View Cards in Deck
						else if (choice == 2) {
							for (auto x : player_deck) {
								cout << x.showcardnumber() << ": " << x.showname() << endl;
							}
						}
						// View Specific Card Info
						else if (choice == 3) {
							cout << "Enter the number of the card that you wish to view: ";
							cin >> card_number;

							// format for is similar to using for loop
							for (auto x : player_deck) {
								if (x.showcardnumber() == card_number) {
									cout << "Card Name: " << x.showname() << endl;
									cout << "Description: " << x.showdescription() << endl;
									test = 1;
								}
							}
							// print that card is not in deck
							if (test == 0) {
								cout << "The card you are looking for is not in your deck." << endl;
							}
							cout << endl;
						}
						// Viewing the Rules
						else if (choice == 4) {
							cout << "Rules: " << endl;
							cout << "1. This is a turn based card game that players will go one after another to fight with monsters. " << endl;
							cout << "2. Players Will select on monster card to send out, along with spell/trap cards to support the current monster out on the field. " << endl;
							cout << "3. if a battle is underway, the victorus monster will not be destroyed, and the margin of victory will be dealt as damage to the losing user's life points." << endl;
						}
						// Setting a Card Down
						else if (choice == 5) {
							if (card_per_turn == 0) {
								cout << "Which card would you like to put down?" << endl;
								cin >> place_card;

								// Searching deck for card number
								for (auto x : player_deck) {
									if (x.showcardnumber() == place_card) {
										cout << "Your card " << x.showname() << " has been placed"<<endl;


										test = 1;

									}
								}
								// print that card is not in deck
								if (test == 0) {
									cout << "The card you are looking for is not in your deck." << endl;
								}
								cout << endl;
							}
							else if (card_per_turn == 1) {
								cout << "You've already placed down a card. Please select another option, or move on to next turn.\n";
							}
						}
						// Moving to Next Turn
						else if (choice == 6) {
							cout << "Moving to Next Phase . . .\n" << endl;
							deck_check = 0;
							card_per_turn = 0;
							break;
						}
						// Invalid Option
						else {
							cout << "Invalid option. Please try again." << endl;
						}
					}
				}
				deck_check = 0;
				// COMPUTER SELECTIONS
				int computer_done = 0;

				while (1) {
					srand((unsigned)time(NULL));
					int num = 0;
					cardplace = 0;
					num = 1 + (rand() % 2);	//This line produces a number from 1 to 5
					cardplace = 1 + (rand() % 7); //deciding what monster to place
					if (computer.showhealth() <= 0) {
						break;
					}
					else if (computer.showhealth() > 0) {
						// COMPUTER DRAWS A CARD
						if (num == 1) {
							if (deck_check == 1) {
								continue;
							}
							else {

								// DRAWING A RANDOM MONSTER CARD
								cardnum = 1 + (rand() % 11);
								computer_deck.push_back(Monster(cardnum));


								deck_check = 1;
								computer_done++;
							}
						}
						// COMPUTER PLACES CARD ON DECK
						else if (num == 2) {

							// PLACE CARD DOWN FOR COMPUTER
							for (auto x : computer_deck) {
								if (x.showcardnumber() == cardplace) {
									cpu_card = cardplace;
									
								}
							}
							computer_done++;
						}
						// COMPUTER SKIPS TO NEXT TURN
						if (computer_done == 2) {
							cout << "\nComputer is moving to next turn . . .\n\n";
							break;
						}
					}
				}
				deck_check = 0;
				//batttle

				Monster inplay(place_card);
				Monster cpu(cardplace);
				for (auto x : player_deck) {
					if (x.showcardnumber() == place_card) {
						Spell user;
						cout << "would u like to apply a spell to your monster?(y/n)" << endl;
						string ans;
						cin >> ans;
						if (ans == "y") {
							cout << "select a card to apply to your monster" << endl;
							cin >> card_number;
							for (auto x : player_deck) {
								if (x.showcardnumber() == card_number) {
									if (card_number == 12 || card_number == 16) {
										user.apply(card_number, cpu);
									}
									else {
										user.apply(card_number, inplay);
									}
								}
							}
						}
						else {
							cout << "you did not apply a spell"<<endl;
							card_number = 0;
						}


						test = 1;

					}
				}
				int computer_remover = cpu_card;
				int condition = card_number;
				if (condition == 15) {
					cout<<"Due to Spell Effect, Battle Sequence does not occur this turn." << endl;
					cout << inplay.showname() << " vs. " << cpu.showname() << " Does not occur" << endl;
				}
				else if (condition == 18) {
					cout << "YOU ATTACK YOUR OPPONENT DIRECTLY" << endl;
					computer.removehealth(inplay.showattackpoints());
				}
				else {
					int dif = 0;
					cout << inplay.showname() << " vs. " << cpu.showname() << endl;
					cout << inplay.showname() << ": " << inplay.showattackpoints() << " Attack Points" << endl;
					cout << cpu.showname() << ": " << cpu.showattackpoints() << " Attack Points" << endl;
					if (inplay.showattackpoints() > cpu.showattackpoints()) {

						dif = loss(inplay.showattackpoints(), cpu.showattackpoints());

						cout << inplay.showname() << " won the battle!" << endl;
						cout << computer.showname() << " lost " << dif << " health" << endl;
						computer.removehealth(dif);
						
					}
					else {

						cout << "LOSER" << endl;
						dif = loss(cpu.showattackpoints(), inplay.showattackpoints());
						cout << cpu.showname() << " won the battle!" << endl;
						cout << user.showname() << " lost " << dif << " health" << endl;
						user.removehealth(dif);
						
					}
				}

				//check health
				cout << "user"<<user.showhealth() << endl;
				cout << "comp"<<computer.showhealth() << endl;

				//remve player card
				list <Card>::iterator p = player_deck.begin();
				
				while (p != player_deck.end()) {
					if (place_card == p->showcardnumber()) {
						cout << "Removing " << p->showname() << endl;
						p = player_deck.erase(p);
						break;
					}
					p++;
				}
				//remove cpu card
				list <Card>::iterator j = computer_deck.begin();

				while (j != computer_deck.end()) {
					if (computer_remover == j->showcardnumber()) {
						cout << "Removing " << j->showname() << endl;
						j = computer_deck.erase(j);
						break;
					}
					j++;
				}

				//remove spell
				list <Card>::iterator h = player_deck.begin();

				while (h != player_deck.end()) {

					if (card_number == h->showcardnumber()) {
						cout << "Removing " << h->showname() << endl;
						h = player_deck.erase(h);
						break;
					}
					h++;
				}

				

				if (user.showhealth() <= 0) {
					cout << "You have lost the duel" << endl;
					computer_deck.clear();
					player_deck.clear();
					break;
				}
				if (computer.showhealth() <= 0) {
					cout << "You WON the duel"<<endl;
					computer_deck.clear();
					player_deck.clear();
					break;
				}
			}

		}


		// EXITING THE GAME
		else if (startgame == 2) {
			cout << "\nExiting . . . Thank you for playing!\n\n";
			return 0;
		}
		// INVALID OPTION
		else {
			cout << "Invalid option.Please try again\n\n";
		}

	}

	return 0;
}


int loss(int greater, int lesser) {
	int dif;
	dif = greater - lesser;
	return dif;
}
