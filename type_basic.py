from typing import List, Dict, Tuple, Union


# STEP1 Variable
# STEP1-1
variable_int: int = 1
variable_float: float = 3.14
variable_str: str = "俺は人間を止めるぞジョジョ"
variable_bool: bool = True

variable_int = "DIO"  # Pylance Error
variable_int = 1.41  # Pylance Error

variabel_int_float: Union[int, float] = 1
variabel_int_float: Union[int, float] = 3.14


# STEP1-2
variable_list: list = ["Hirose", "Okuyasu", "Kishibe"]
variable_dict: dict = {"Hirose": "Echoes",
                       "Okuyasu": "The Hnad",
                       "Kishibe": "Heaven's Door"}

variable_list = "Jonathan Jostar"  # Pylance Error


# STEP1-3
variable_int_list: List[int] = [1, 10, 100, 1000]
variable_str_int_dict: Dict[str, int] = {"Zeppeli": 1838,
                                         "LisaLisa": 1888,
                                         "Speedwagon": 1863}

variable_int_list = [1, 2, 1.73]  # Pylance Error
variable_str_int_dict = {"Speedwagon": "Phantom Blood"}  # Pylance Error


# STEP1-4
variable_int_tuple: Tuple[int, int, int] = (1, 2, 3)

variable_int_tuple = (1, 2, 3.14)  # Pylance Error


# STEP2 Function
# STEP2-1
def add(x1: int, x2: int) -> int:
    return x1 + x2


y = add(100, 200)
y = add(1.11 + 2.22)  # Pylance Error


# STEP2-2
def print_Stroheim_description(word: str) -> None:
    print(f"シュトロハイムは{word}です")


print_Stroheim_description("不死身")  # シュトロハイムは不死身です
