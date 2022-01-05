# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------


import dataclasses
import json
from dataclasses import dataclass, asdict
from typing import List
from c_gen import C_gen as cgen
from field import Field, Field_data, FieldType_data
from register import Register, Register_data
from entity import Entity, Entity_data
from fpga import Fpga, FPGA_data
import logging

# class FieldType_data:
#     data = "data"
#     enum = "enum"
#
#
# @dataclass
# class Field_data:
#     name: str
#     info: str
#     read: str
#     write: str
#     offset: int
#     type: int    # FieldType: data or enumerator
#     Enum: List[str]


c_my_map = {
    "Name": "",
    "BaseAddress": "",
    "Description": "",
    "Register_data": [
        {
            "name": "",
            "offset": 0,
            "Field_data": [
                {
                    "name": "",
                    "info": "",
                    "read": "",
                    "write": "",
                    "offset": 0,
                    "type": "",  # FieldType: data or enumerator
                    "Enum": [""],
                }
            ]
        }
    ]
}




def hdl_build():
    print("hdl_build()")


def class_test():


    field1 = Field()
    field1.set_name("trigger_fuse")
    field1.set_write("true")
    field1.set_read("false")
    field1.set_offset(4)
    field1.set_width(4)
    field1.set_type(FieldType_data.enum)
    field1.add_enum("START")
    field1.add_enum("STOP")
    field1.add_enum("FIRE")
    field1.add_enum("HOLD")
    print(field1.get_dict())
    field2 = Field()
    field2.set_offset(5)
    field2.set_width(5)
    field2.set_type(FieldType_data.data)

    register1 = Register()
    register1.set_name("triggers")
    register1.set_offset(3)
    register1.set_description("Register for all triggers")
    register1.add_field(field1.get_dict())
    register1.add_field(field2.get_dict())

    print(register1.get_dict())

    entity1 = Entity()
    entity1.set_name("fuse_entity")
    entity1.set_baseaddress("0x40000000")
    entity1.set_description("This is a fuse entity")
    entity1.add_register(register1.get_dict())
    entity1.add_register(register1.get_dict())

    print(entity1.get_dict())

    fpga1 = Fpga()
    fpga1.set_name("LET")
    fpga1.set_description("FPGA....")
    fpga1.add_entity(entity1.get_dict())

    # Write json with dict
    with open('fpga_out.json', 'w') as json_file:
        json.dump(fpga1.get_dict(), json_file, indent=4)

    cgen.gen_entity_header_file(entity1.get_dict())



def json_test():
    map1 = Entity_data(**c_my_map)
    print(map1)
    with open('map.json') as f:
        map1 = json.load(f)

    print(map1)
    print(map1["BaseAddress"])
    print(map1["Description"])
    #print(map1["Register"][0]["name"])
    #regs = map1["Register"]
    #print(regs)
    #my_reg = {"name": "flags", "offset": 5}
    #new_reg = Register(**my_reg)
    # Convert Dataclass Register to Dict
    #reg_dict = dataclasses.asdict(new_reg)
    map_dict = map1
    print(map_dict)
    #map1["Register"].append(new_reg)
    #print(map1["Register"])

    # Write json with dict
    #with open('map_out.json', 'w') as json_file:
    #    json.dump(map1, json_file, indent=4)

    cgen.gen_entity_header_file(map_dict)

    field1=Field()
    field1.set_name("pwr")
    field1.set_write("false")
    field1.set_info("Info text...")
    field1.set_offset(4)

    print(field1.get_dict())
    print(field1.get_name())




