#pragma once
#include "Card.h"
class Monster :
    public Card
{
    friend class Spell;
    int attack_points ;
    int defense_points;

public:
    // constructor
    Monster();
    Monster(int in_num);

    // method
    string showname();
    int showcardnumber();
    string showdescription();
    int showattackpoints();
    int showdefensepoints();

    // destructor
    ~Monster();
};

