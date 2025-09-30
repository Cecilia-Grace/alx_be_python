def count_vowels():
    vowels = "a","e","i","o","u"
    word = input("Enter a word: ").lower()

    for vowel in vowels:
        if vowel in word:
            count = word.count(vowel)
            if count > 0:
                print(f"{vowel}: {count}")
 
        
count_vowels() 