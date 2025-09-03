def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_frequency(text):
    frequency = {}
    for char in text:
        char = char.lower()
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sort_char_report_on(item):
    return item["count"]

def generate_report(char_freq):
    result = []
    for char in char_freq:
        result.append({
            "char": char,
            "count": char_freq[char]
        })
    result.sort(key=sort_char_report_on, reverse=True)
    return result