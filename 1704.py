class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lenght = len(s) // 2
        vowels_a, vowels_b = 0, 0
        for i in range(0, lenght):
            if s[i].lower() in 'aeiou':
                vowels_a += 1
        for i in range(lenght, len(s)):
            if s[i].lower() in 'aeiou':
                vowels_b += 1
        return vowels_a == vowels_b 
