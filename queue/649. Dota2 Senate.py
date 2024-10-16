class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n_senate = len ( senate )

        r_arr = [i for i in range ( n_senate ) if senate[i] == 'R']
        d_arr = [j for j in range ( n_senate ) if senate[j] == 'D']

        while r_arr and d_arr:
            r = r_arr.pop ( 0 )
            d = d_arr.pop ( 0 )
            if r < d:
                r_arr.append ( n_senate + r )
            else:
                d_arr.append ( n_senate + d )
        return 'Radiant' if r_arr else 'Dire'
