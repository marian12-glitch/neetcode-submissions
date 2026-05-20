class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use L and R pointer
        L, R = 0, len(s) -1 
        #while loop L<R
        while L < R:
            if not(s[L].isalnum()):
                L += 1

            if not(s[R].isalnum()):
                R -= 1

            #handle all non alnum
            #if not alphanumeric skip
            #compare L to R if not same return false
            if (s[L].isalnum() and s[R].isalnum()):
                if (s[L].lower() == s[R].lower()):
                    L += 1
                    R -= 1

                else:
                    return False
            
        #return True After loop runs
        return True
