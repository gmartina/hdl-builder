#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------
import dataclasses
from typing import List
from dataclasses import dataclass, asdict
from field import Field_data, Field

@dataclass
class Register_data:
    name: str
    offset: int
    description: str
    Field_data: List[Field_data]


class Register:
    def __init__(self):
        self.__register_data = Register_data(
                    name= "",
                    offset= 0,
                    description= "",
                    Field_data= [],
                )


    def health_check(self, register):
        print("Health check of: " + register.get_name())
        for ff in self.__register_data.Field_data:
            limit = ff.offset + ff.width - 1



    def create_field(self):
        pass


    def add_field(self, field: Field_data):
        #field.health_check()
        self.__register_data.Field_data.append(field)


    def clear_fields(self):
        self.__register_data.Field_data.clear()


    @classmethod
    def get_name_from_dict(cls, entity_dict: dict):
        return entity_dict["name"]


    @classmethod
    def get_offset_from_dict(cls, entity_dict: dict):
        return entity_dict["offset"]


    @classmethod
    def get_description_from_dict(cls, entity_dict: dict):
        return entity_dict["description"]


    @classmethod
    def get_field_data_from_dict(cls, entity_dict: dict):
        return entity_dict["Field_data"]


    def set_name(self, name: str):
        self.__register_data.name = name


    def set_offset(self, offset: int):
        if offset >= 0:
            self.__register_data.offset = offset
        else:
            raise Exception('Offset must be greater than 0.')


    def set_description(self, description: str):
        self.__register_data.description = description


    def set_field_data(self, field_data: List):
        self.__register_data.Field_data = field_data

    def get_name(self):
        return self.__register_data.name

    def get_description(self):
        return self.__register_data.description

    def get_offset(self):
        return self.__register_data.offset

    def get_field_data(self):
        return self.__register_data.Field_data


    def get_dict(self):
        return dataclasses.asdict(self.__register_data)

    def add_field(self, new_field: Field_data):
        self.__register_data.Field_data.append(new_field)

