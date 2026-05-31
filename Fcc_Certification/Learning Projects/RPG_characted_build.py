full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
            return "The character name should not contain spaces"
    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    else: 
         return name + "\n" + "STR " + strength*full_dot+empty_dot*(10-strength) + "\n" + "INT " + intelligence*full_dot+empty_dot*(10-intelligence) + "\n" + "CHA " + charisma*full_dot+empty_dot*(10-charisma)
    
# Test cases
print(create_character("Aragorn", 3, 2, 2))
print(create_character("", 3, 2, 2))
print(create_character("Legolas", 5, 1, 1))
print(create_character("Gimli", 2, 3, 2))
print(create_character("Frodo", 1, 4, 2))