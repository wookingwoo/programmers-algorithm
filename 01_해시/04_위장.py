def solution(clothes):
    hash_map = {}

    for clothes_name, clothes_type in clothes:
        if clothes_type in hash_map:
            hash_map[clothes_type] += 1
        else:
            hash_map[clothes_type] = 1

    # print("hash_map:", hash_map)

    answer = 1
    for clothes_type in hash_map:
        answer *= (hash_map[clothes_type] + 1)

    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
