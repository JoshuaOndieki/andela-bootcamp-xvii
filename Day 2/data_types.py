#data types lab

def data_type(inputs):
    if type(inputs) == str:
        return len(inputs)
    elif type(inputs) == bool:
        return inputs
    elif type(inputs) == int:
        if inputs < 100:
            return "less than 100"
        elif inputs == 100:
            return "equal to 100"
        else:
            return "more than 100"
    elif type(inputs) == list:
        if len(inputs) < 3:
            return None
        else:
            return inputs[2]
    else:
        return "no value"