import warnings
import re

def twitter(code_gen, credientials, missing_key_list):
    # Making sure the all the keys are provided by the users in the yaml file
    unprovided_keys = []
    for each in missing_key_list:
        key = each.lower().removeprefix("your_")
        if key not in credientials:
            unprovided_keys.append(key)
    if len(unprovided_keys) > 0:
        warning_msg = "List of keys need to provided in the yaml file: " + (",").join(unprovided_keys), 
        warnings.warn(warning_msg)
        return None
    
    # Start parsing
    for each in missing_key_list:
        key = each.lower().removeprefix("your_")
        code_gen = re.sub(re.escape(key + " = ") + r"\"(.*?)\"", key + " = " + "\"" + credientials[key] + "\"", code_gen)
    return code_gen