upper_case = [chr(x) for x in range(65, 91)]
lower_case = [chr(x) for x in range(97, 123)]

numbers = [chr(x) for x in range(48, 58)]

others1 = [chr(x) for x in range(33, 48)]
others2 = [chr(x) for x in range(58, 65)]
others3 = [chr(x) for x in range(91, 97)]

special_characters = others1 + others2 + others3

print(special_characters)