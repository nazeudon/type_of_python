from typing import Dict, List, NamedTuple, Tuple, TypedDict, Final, Union


# STEP3 TypeDict
# STEP3-1
class StandDictBasic(TypedDict):
    person: str
    ability: str


CrazyDiamondDictBasic: StandDictBasic = {"person": "Josuke",
                                         "ability": "Fix broken things"}


# STEP3-2
class StandDictRequired(TypedDict):
    person: str
    ability: str


class StandDictOptional(TypedDict, total=False):
    sound: str


class StandDictAdvance(StandDictRequired, StandDictOptional):
    pass


CrazyDiamondDictAdvance: StandDictAdvance = {"person": "Josuke",
                                             "ability": "Fix broken things"}
StarPlatinumDictAdvance: StandDictAdvance = {"person": "Jotaro",
                                             "ability": "Move at light speed",
                                             "sound": "OraOra"}


# STEP4 NamedTuple
class StandTuple(NamedTuple):
    person: str
    ability: str
    sound: str


TheWorldTuple: StandTuple = StandTuple(
    "DIO", "Stop time quite a bit", "MudaMuda"
)

print(TheWorldTuple.person)  # "DIO"
print(TheWorldTuple.ability)  # "Stop time quite a bit"
print(TheWorldTuple.sound)  # "MudaMuda"


# STEP5 Final
Cards: Final[str] = "Stopped thinking"

Cards = "Want to back to the Earth"  # Pylance Error


PillarMans: Final[List[str]] = ["Cards", "Wamuu", "Esidisi", ""]
PillarMans[3] = "Santana"

PillarMans = "want to redefine"  # Pylance Error


JOJO: Final[Tuple[str, str, str, str]] = (
    "Jonathan", "Josef", "Jotaro", "Josuke"
)

JOJO[3] = "Joko"  # Pylance Error
JOJO = "want to redefine"  # Pylance Error


# STEP6 Alias(エイリアス)
HandleTime = Dict[str, Dict[str, Union[str, int]]]

Character: HandleTime = {
    "Dio": {"stand": "The World",
            "birth": 1867},
    "Kira": {"stand": "Killer Queen",
             "birth": 1966},
    "Diavolo": {"stand": "King Crimson",
                "birth": 1967},
}
