def count_character_occurrence(string, character):
    count = 0
    for i in string:
        if i == character:
            count += 1
    return count
print(count_character_occurrence("hello", "l"))  # 2