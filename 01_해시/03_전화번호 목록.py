def solution(phone_book):
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[:i] in hash_map:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))  # True
print(solution(["12", "123", "1235", "567", "88"]))  # False
