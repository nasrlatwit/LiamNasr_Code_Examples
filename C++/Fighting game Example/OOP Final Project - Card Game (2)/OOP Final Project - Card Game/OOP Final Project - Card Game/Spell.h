#pragma once
#include "Card.h"
#include "Monster.h"

class Spell :
    public Card
{
    friend class Monster;
public:
    // attributes
    Spell();
    Spell(int in_num);

    // method
    string showname();
    int showcardnumber();
    string showdescription();
    void apply(int card_num, Monster& user);

    // destructor
    ~Spell();
};