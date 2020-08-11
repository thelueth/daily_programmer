def same_necklace(original, new):
    words = []
    word = original
    for i in range(len(original)):
        first = word[0]
        word = word[1:]+first
        words.append(word)
    
    if new in words:
        return True
    elif original == "" and new == "":
        return True
    else: 
        return False


print(same_necklace("nicole", "icolen"))
print(same_necklace("nicole", "lenico"))
print(same_necklace("nicole", "coneli"))
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
print(same_necklace("abc", "cba"))
print(same_necklace("xxyyy", "xxxyy"))
print(same_necklace("xyxxz", "xxyxz"))
print(same_necklace("x", "x"))
print(same_necklace("x", "xx"))
print(same_necklace("x", ""))
print(same_necklace("", ""))