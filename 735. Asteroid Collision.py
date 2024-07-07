class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            while ans and i < 0 and ans[-1] > 0:
                if ans[-1] > abs ( i ):
                    break
                elif ans[-1] == abs ( i ):
                    ans.pop ()
                    break
                else:
                    ans.pop ()
            else:
                ans.append ( i )

        return ans

