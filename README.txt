----------------------------------------Welcome to my Pokémon Game----------------------------------------

I started this project to advance my Python skills in OOP. Based on a YouTube Tutorial
'Python Object Oriented Example Project' on Channel 'CodingNomads' by 'Martin Breuss'.
The video can be found under following link: 
https://www.youtube.com/watch?v=2AK7j8pIh-0&t=21s&ab_channel=CodingNomads
I followed Mr. Breuss introduction and added more functionality to the Game.

As the game starts, a set of Pokémon with various attributes is instantiated from a csv-file. In the
beginning, the Player chooses a name and how many Pokémon will fight for him in this round, as well as
whether he want to pick his/her Pokémon, or they get randomly assigned. The opponent gets the same number
of randomly assigned Pokémon.

The Player has different types of actions he/she can execute: (fight, train, heal,
show Pokémon-type relationships, show Pokémon, quit). After every action all Pokémon for both players
will be displayed with their attributes: number of Pokémon (for selection), name, type, max. & current HP,
damage, status.

Pokémon-Types:
There are five different Pokémon-types: fire, water, grass, electric and rock. Each type as advantage
over two other types and disadvantage over two other types.

Fight:
If fight is selected, the player can choose one of his/her active Pokémon. If only one active Pokémon
remains, it is selected automatically. The Pokémon will fight against an active, randomly selected Pokémon
of the opponent. If a Pokémon has a type-advantage over the other, it deals double damage. The Pokémon
in disadvantage deals normal damage. If the HP of a Pokémon drops to or below zero, the status of that
Pokémon changes to KO and it can't be selected for any further action.

Train:
If train is selected, the Player selects an active Pokémon. Again, if only one active Pokémon remains,
it is selected automatically. The trained Pokémon from now on deals a predefined amount more damage in
every fight. An active, randomly selected Pokémon from the opponent becomes equally trained. The player
can train a predefined number of times.

Heal:
If heal is selected, the Player selects an active Pokémon, which has not full HP. If no such Pokémon is
in the player's list, the game return to the action selection. Again, if only one active Pokémon with
less than full HP remains, it is selected automatically. The healed Pokémon receives a health potion and
fills up a predefined amount of HP. An active, randomly selected Pokémon with less than full HP from the 
opponent becomes equally healed. If no such Pokémon exists, the opponent heals no Pokémon. The player
can heal a predefined number of times.

Show Pokémon-Type-Relationships:
shows a table of the relationships between the different types. Each type has advantage over two types,
disadvantage over two other types and a neutral relationship to itself.

Show:
Shows the status with all attributes of all Pokémon from both players.

Quit:
Immediately ends the game.

The game is over, as soon as each Pokémon of one or both players are KO, or the player leaves the
game through the quit action.

I created this game in a graphically appealing manner, as much as the VS Code console can spare.
I hope you enjoy playing the game and if you have any questions or suggestions, feel free to comment.

Acknowledgement to Martin Breuss, who created the tutorial on which this game is based on. 
It was my first practical experience with classes in Python.