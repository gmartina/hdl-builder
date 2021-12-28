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
from field import Field, Field_data

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

@dataclass
class Register_data:
    name: str
    offset: int
    Field_data: List[Field_data]


@dataclass
class Entity_data:
    Name: str
    BaseAddress: str
    Description: str
    Register_data: List[Register_data]


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




