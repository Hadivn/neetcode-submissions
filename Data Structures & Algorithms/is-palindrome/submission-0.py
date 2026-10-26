class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        reversedString = ''.join(reversed(s))

        cleanedString = ''.join(filter(str.isalnum, s))
        reversedCleanedString = ''.join(filter(str.isalnum, reversedString))

        print(cleanedString.lower())
        print(reversedCleanedString.lower())
        if cleanedString.lower() == reversedCleanedString.lower():
            return True
        return False
        