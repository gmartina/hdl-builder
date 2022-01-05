# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 02/01/2021
# version ='1.0'
# ---------------------------------------------------------------------------

import dataclasses
from typing import List
from dataclasses import dataclass, asdict
from entity import Entity, Entity_data

@dataclass
class FPGA_data:
    Name: str
    Description: str
    Entity_data: List[Entity_data]


class Fpga:

    def __init__(self):
        self.__fpga_data = FPGA_data(
                    Name= "",
                    Description= "",
                    Entity_data= [],
                )


    @classmethod
    def get_name(cls, fpga_dict: dict):
        return fpga_dict["Name"]


    @classmethod
    def get_description(cls, fpga_dict: dict):
        return fpga_dict["Description"]


    @classmethod
    def get_entity(cls, fpga_dict: dict):
        return fpga_dict["Entity_data"]


    @classmethod
    def get_number_of_registers(cls, fpga_dict: dict):
        return len(fpga_dict["Entity_data"])


    def set_name(self, name: str):
        self.__fpga_data.Name = name


    def set_description(self, description: str):
        self.__fpga_data.Description = description


    def set_entity_data(self, entity_data: List):
        self.__fpga_data.Entity_data = entity_data


    def get_name(self):
        return self.__fpga_data.Name

    def get_description(self):
        return self.__fpga_data.Description

    def get_entity_data(self):
        return self.__fpga_data.Entity_data


    def get_dict(self):
        return dataclasses.asdict(self.__fpga_data)

    def add_entity(self, new_entity: Entity_data):
        self.__fpga_data.Entity_data.append(new_entity)


















