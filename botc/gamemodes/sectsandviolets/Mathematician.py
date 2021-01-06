"""Contains the Mathematician Character class"""

import json
from botc import Character, Townsfolk
from ._utils import SectsAndViolets, SnVRole

with open('botc/gamemodes/sectsandviolets/character_text.json') as json_file:
    character_text = json.load(json_file)[SnVRole.mathematician.value.lower()]


class Mathematician(Townsfolk, SectsAndViolets, Character):
    """Mathematician: Each night, you learn how many players' abilities worked abnormally (since dawn) due to another character's ability.
    """

    def __init__(self):

        Character.__init__(self)
        SectsAndViolets.__init__(self)
        Townsfolk.__init__(self)

        self._desc_string = character_text["description"]
        self._examp_string = character_text["examples"]
        self._instr_string = character_text["instruction"]
        self._lore_string = character_text["lore"]

        self._art_link = "https://bloodontheclocktower.com/wiki/images/3/3c/Mathematician_Token.png"
        self._wiki_link = "https://bloodontheclocktower.com/wiki/Mathematician"

        self._role_enum = SnVRole.mathematician
