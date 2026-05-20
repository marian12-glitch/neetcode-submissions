class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use pointers L and R
        L, R = 0, len(s) - 1
        # use a while loop whil L < R
        while L<R:
            if (s[L].isalnum() and s[R].isalnum()):
                #compare L to R, if not same return false
                if s[L].lower() != s[R].lower():
                    return False
                else:
                    L +=1
                    R -=1
            elif not(s[L].isalnum()):
                L +=1
            
            elif not(s[R].isalnum()):
                R -=1
           
            # if L is not alphanumeric move forward
            #if R is not alphanumeric move backward
            
        #return true when the while loop ends
        return True

