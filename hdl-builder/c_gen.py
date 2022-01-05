# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------


from entity import Entity
from register import Register
from field import Field, FieldType_data

class C_gen:

    def __init__(self):
        print("Creating C code generator...")

    @classmethod
    def calc_hex_mask(cls, offset: int, width: int):
        acum = 0
        bit = 1
        for ii in range(width):
            acum += 2 ** ii

        mask = acum * (2 ** offset)
        return "0x"+format(mask, '08X')

    @classmethod
    def offset2address(cls, offset: int):
        return "0x" + format(offset*4, '08X')

    @classmethod
    def create_entity_info_comment(cls, entity_dict: dict):
        entity_name         = Entity.get_name_from_dict(entity_dict)
        entity_description  = Entity.get_description_from_dict(entity_dict)
        comment = f"/*    This file has been created with HDL-BUILDER    */ \n"
        comment += f"/* Entity: "+ entity_name + " */ \n"
        comment += f"/* Description: "+ entity_description + " */ \n\n\n"
        return comment

    @classmethod
    def create_register_info_comment(cls, register_dict: dict, prefix: str):
        comment = ""
        register_name         = Register.get_name_from_dict(register_dict)
        register_description  = Register.get_description_from_dict(register_dict)
        register_offset       = Register.get_offset_from_dict(register_dict)

        comment += f"/* Register: "+ register_name + " */ \n"
        comment += f"/* Description: "+ register_description + " */ \n"
        comment += "#define " + prefix.upper() + "_" + register_name.upper() + "_OFFSET " + C_gen.offset2address(register_offset)

        return comment

    @classmethod
    def create_field_info_comment(cls, field_dict: dict, prefix: str):
        comment = ""
        field_name  = Field.get_name_from_dict(field_dict)
        field_info  = Field.get_info_from_dict(field_dict)
        field_read  = Field.get_read_property_from_dict(field_dict)
        field_write = Field.get_write_property_from_dict(field_dict)
        field_offset = Field.get_offset_from_dict(field_dict)
        field_width = Field.get_width_from_dict(field_dict)
        field_type = Field.get_type_from_dict(field_dict)
        field_enum = Field.get_enum_from_dict(field_dict)

        comment += f"/* " + field_name + ": " + field_info + " */ \n"
        comment += f"/* Type: " + field_type + " */ \n"
        comment += "#define " + prefix.upper() + "_" + field_name.upper() + "_BIT_OFFSET " + str(field_offset)  + "\n"
        comment += "#define " + prefix.upper() + "_" + field_name.upper() + "_BIT_WIDTH " + str(field_width)  + "\n"
        comment += "#define " + prefix.upper() + "_" + field_name.upper() + "_BIT_MASK " \
                   + C_gen.calc_hex_mask(field_offset, field_width)  + "\n"

        if field_type == FieldType_data.enum:
            comment += "/* Enum values: */\n"
            for value, enumx in enumerate(field_enum):
                comment += "#define " + prefix.upper() + "_" + field_name.upper() + "_" + str(enumx).upper() \
                           + " " + str(value) + "\n"

        return comment

    @classmethod
    def gen_entity_header_file(cls, entity_dict: dict):
        entity_name = Entity.get_name_from_dict(entity_dict)
        entity_baseaddress = Entity.get_baseaddress_from_dict(entity_dict)
        print(f"Entity name: " + entity_name)
        print(f"Number of registers: " + str(Entity.get_number_of_registers_from_dict(entity_dict)))
        file_name=entity_name + ".h"
        with open(file_name, 'w') as f:
            comment = C_gen.create_entity_info_comment(entity_dict)
            f.write(comment)
            str_baseaddress = "#define " + entity_name.upper() + "_BASEADDRESS " + entity_baseaddress
            f.write(str_baseaddress)
            f.write("\n\n")
            regs = Entity.get_registers_from_dict(entity_dict)

            for reg in regs:
                comment = C_gen.create_register_info_comment(reg, entity_name)
                f.write(comment)
                f.write("\n\n")
                f.write(f"/* Fields: */ \n")
                fields = Register.get_field_data_from_dict(reg)
                for fielx in fields:
                    comment = C_gen.create_field_info_comment(fielx, entity_name)
                    f.write(comment)
                    f.write("\n\n")


            f.close()
















