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


class FieldType_data:
    data = "data"
    enum = "enum"


@dataclass
class Field_data:
    name: str
    info: str
    read: str
    write: str
    offset: int
    type: str    # FieldType: data or enumerator
    Enum: List[str]


class Field:

    def __init__(self):
        self.__field_data = Field_data(
                    name= "",
                    info= "",
                    read= "",
                    write= "",
                    offset= 0,
                    type= "",
                    Enum= [""],
                )


    @classmethod
    def health_check(cls, map):
        pass

    def create_field(self):
        pass

    @classmethod
    def get_name(cls, field_dict: dict):
        return field_dict["name"]


    @classmethod
    def get_info(cls, field_dict: dict):
        return field_dict["info"]


    @classmethod
    def get_read_property(cls, field_dict: dict):
        return field_dict["read"]

    @classmethod
    def get_write_property(cls, field_dict: dict):
        return field_dict["write"]

    @classmethod
    def get_offset(cls, field_dict: dict):
        return field_dict["offset"]

    @classmethod
    def get_type(cls, field_dict: dict):
        return field_dict["type"]


    @classmethod
    def get_type(cls, field_dict: dict):
        return field_dict["type"]


    @classmethod
    def get_enum(cls, field_dict: dict):
        return field_dict["Enum"]


    @classmethod
    def get_fields(cls, field_dict: dict):
        return field_dict["Field_data"]


    def set_name(self, name: str):
        self.__field_data.name = name

    def set_info(self, info: str):
        self.__field_data.info = info

    def set_read(self, read: str):
        if read == "true" or read == "false":
            self.__field_data.read = read
        else:
            raise Exception('Read can only be true or false.')


    def set_write(self, write: str):
        if write == "true" or write == "false":
            self.__field_data.write = write
        else:
            raise Exception('Write can only be true or false.')


    def set_offset(self, offset: int):
        if offset >= 0 or offset <= 31:
            self.__field_data.offset = offset
        else:
            raise Exception('Offset can only be between 0 and 31')


    def set_type(self, type: str):
        if type == "data" or type == "enum":
            self.__field_data.type = type
        else:
            raise Exception('Field type can only be data or enum.')

    def set_enum(self, enum: List):
        self.__field_data.Enum = enum

    def get_name(self):
        return self.__field_data.name

    def get_info(self):
        return self.__field_data.info

    def get_read(self):
        return self.__field_data.read

    def get_write(self):
        return self.__field_data.write

    def get_offset(self):
        return self.__field_data.offset

    def get_type(self):
        return self.__field_data.type

    def get_enum(self):
        return self.__field_data.Enum


    def get_dict(self):
        return dataclasses.asdict(self.__field_data)

