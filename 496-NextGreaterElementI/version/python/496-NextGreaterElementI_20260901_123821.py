# Last updated: 9/1/2026, 12:38:21 PM
1class Solution:
2    def findRelativeRanks(self, score):
3        n = len(score)
4        M = 0
5        for x in score:
6            if x > M:
7                M = x
8        score_idx = [0] * (M + 1)
9        for i in range(n):
10            score_idx[score[i]] = i + 1
11
12        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
13
14        rank = ["" for _ in range(n)]
15        place = 1
16        for i in range(M, -1, -1):
17            if score_idx[i] != 0:
18                org_idx = score_idx[i] - 1
19                if place < 4:
20                    rank[org_idx] = medals[place - 1]
21                else:
22                    rank[org_idx] = str(place)
23                place += 1
24        return rank