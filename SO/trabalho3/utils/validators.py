def validate_integer_value(user_input: str, zfill_value: int, min_value: int, max_value: int) -> str:
    invalid_message = ""
    try:
        value = int(user_input)
        if (value >= min_value and value <= max_value):
            return str(value).zfill(zfill_value)
        else:
            invalid_message = f"Valor deve estar entre {min_value} e {max_value}!"
    except:
        invalid_message = "Entrada inválida"

    raise ValueError(invalid_message)


def validate_string_value(user_input: str, max_length: int) -> str:
    invalid_message = ""
    if (len(user_input) <= max_length):
        return user_input.ljust(max_length)
    else:
        invalid_message = f"Entrada maior que {max_length} caracteres!"

    raise ValueError(invalid_message)
