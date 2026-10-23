class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_string = ''.join(sorted(s))
        second_string = ''.join(sorted(t))
        if len(first_string) is len(second_string):
            for i in range(len(first_string)):
                if first_string[i] != second_string[i]:
                    return False
            return True
        else:
            return False