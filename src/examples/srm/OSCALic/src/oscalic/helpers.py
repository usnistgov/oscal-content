from uuid import uuid4
from yaml import safe_load,YAMLError,dump
from .validation import Validation

# import simplejson as json


class Helper:
    def get_uuid():
        return uuid4()


    def from_yaml(model, yaml_content, construct=False):
        result = None

        try:
            loaded_yaml = safe_load(yaml_content)
        except YAMLError as e:
            # print(f"YAML ERROR: Could not interpret ({e.problem}).\n")
            raise

        if type(loaded_yaml) == list:
            loaded_yaml = loaded_yaml[0]

        if construct:
            result = model.construct(**loaded_yaml)
        else:
            try:
                result = model(**loaded_yaml)
            except Validation.OSCALValidationError as e:
                # print(f"VALIDATION ERROR: {e.json()}\n")
                raise

        return result


    def to_yaml(model):
        return dump(model.dict(by_alias=True,exclude_unset=True), sort_keys=False)
    

    
    # def from_json(model, json_content, construct=False):
    #     result = None

    #     try:
    #         loaded_json = json.loads(json.dumps(json_content))
    #     except json.JSONDecodeError as e:
    #         # print(f"YAML ERROR: Could not interpret ({e.problem}).\n")
    #         raise

    #     if type(loaded_json) == list:
    #         loaded_json = loaded_json[0]

    #     if construct:
    #         result = model.construct(**loaded_json)
    #     else:
    #         try:
    #             result = model(**loaded_json)
    #         except Validation.OSCALValidationError as e:
    #             # print(f"VALIDATION ERROR: {e.json()}\n")
    #             raise

    #     return result


    # def to_json(model):
    #     return json.dump(model.dict(by_alias=True,exclude_unset=True), sort_keys=False)