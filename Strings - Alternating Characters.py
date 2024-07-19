def alternating_characters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

if _name_ == "_main_":
    s = "AABAAB"
    print(alternating_characters(s))

