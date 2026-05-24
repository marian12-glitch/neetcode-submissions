class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        L = 0
        R = len(s1)
        dict1 = {}
        dict2 = {}

        for i in range(len(s1)):
            dict1[s1[i]] = dict1.get(s1[i], 0) + 1
        
        for i in range(L, R):
                dict2[s2[i]] = dict2.get(s2[i], 0) + 1


        while R < len(s2):
            if dict1 == dict2:
                return True

            else:
                dict2[s2[L]] -= 1
                if dict2[s2[L]] == 0:
                    del dict2[s2[L]]
                dict2[s2[R]] = dict2.get(s2[R], 0) + 1
                R += 1
                L += 1

        return dict1 == dict2