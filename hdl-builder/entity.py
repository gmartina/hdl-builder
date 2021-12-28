# ----------------------------------------------------------------------------
# Created By  : Gustavo Martin
# Created Date: 28/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------


class Entity:

    def __init__(self):
        pass


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






