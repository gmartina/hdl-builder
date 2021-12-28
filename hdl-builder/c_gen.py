# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------


from entity import Entity


class C_gen:

    def __init__(self):
        print("Creating C code generator...")

    @classmethod
    def create_entity_info_comment(cls, entity_dict: dict):
        entity_name         = Entity.get_name(entity_dict)
        entity_description  = Entity.get_description(entity_dict)
        comment = f"/*    This file has been created with HDL-BUILDER    */ \n"
        comment += f"/* Entity: "+ entity_name + " */ \n"
        comment += f"/* Description: "+ entity_description + " */ \n\n\n"
        return comment

    @classmethod
    def create_register_info_comment(cls, entity_dict: dict):
        pass


    @classmethod
    def gen_entity_header_file(cls, entity_dict: dict):
        entity_name = Entity.get_name(entity_dict)
        entity_baseaddress = Entity.get_baseaddress(entity_dict)
        print(f"Entity name: " + entity_name)
        print(f"Number of registers: " + str(Entity.get_number_of_registers(entity_dict)))
        file_name=entity_name + ".h"
        with open(file_name, 'w') as f:
            comment = C_gen.create_entity_info_comment(entity_dict)
            f.write(comment)
            str_baseaddress = "#define " + entity_name.upper() + "_BASEADDRESS " + entity_baseaddress
            f.write(str_baseaddress)















