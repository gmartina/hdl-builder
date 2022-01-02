# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------
import dataclasses
from typing import List
from dataclasses import dataclass, asdict
from register import Register_data, Register

@dataclass
class Entity_data:
    Name: str
    BaseAddress: str
    Description: str
    Register_data: List[Register_data]


class Entity:

    def __init__(self):
        self.__entity_data = Entity_data(
                    Name= "",
                    BaseAddress= "",
                    Description= "",
                    Register_data= [""],
                )


    @classmethod
    def health_check(cls, map):
        pass

    def create_entity(self):
        pass

    @classmethod
    def get_name(cls, entity_dict: dict):
        return entity_dict["Name"]


    @classmethod
    def get_baseaddress(cls, entity_dict: dict):
        return entity_dict["BaseAddress"]


    @classmethod
    def get_description(cls, entity_dict: dict):
        return entity_dict["Description"]


    @classmethod
    def get_number_of_registers(cls, entity_dict: dict):
        return len(entity_dict["Register_data"])


    @classmethod
    def get_registers(cls, entity_dict: dict):
        return entity_dict["Register_data"]


    def set_name(self, name: str):
        self.__entity_data.Name = name


    def set_baseaddress(self, baseaddress: str):
        self.__entity_data.BaseAddress = baseaddress


    def set_description(self, description: str):
        self.__entity_data.Description = description


    def set_register_data(self, register_data: List):
        self.__entity_data.Register_data = register_data

    def get_name(self):
        return self.__entity_data.Name

    def get_description(self):
        return self.__entity_data.Description

    def get_baseaddress(self):
        return self.__entity_data.BaseAddress

    def get_register_data(self):
        return self.__entity_data.Register_data


    def get_dict(self):
        return dataclasses.asdict(self.__entity_data)

    def add_register(self, new_register: Register_data):
        self.__entity_data.Register_data.append(new_register)