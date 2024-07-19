import Counter

def check_magazine(magazine, note):
    magazine_count = Counter(magazine)
    note_count = Counter(note)
    
    for word in note_count:
        if note_count[word] > magazine_count.get(word, 0):
            return "No"
    return "Yes"

# Example usage
if _name_ == "_main_":
    magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
    note = ['give', 'one', 'grand', 'today']
    print(check_magazine(magazine, note))  
