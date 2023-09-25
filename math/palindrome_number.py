class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

    isPalindrome(0, x=-121)


class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        else:
            reversed_num = 0
            while x > reversed_num:
                reversed_num = (reversed_num * 10) + (x % 10)
                x //= 10

            return reversed_num == x or reversed_num // 10 == x

    isPalindrome(0, x=-121)
