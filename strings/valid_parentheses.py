class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        dic = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in "([{":
                lst.append(i)
            elif lst:
                if dic[i] == lst[-1]:
                    lst.pop()
                else:
                    return False
            else:
                return False

        return not lst


    isValid(0, '()[]{}')