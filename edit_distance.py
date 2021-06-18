class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # if n == 0 and m == 0:
            # return 0
        # elif n > 0 and m == 0:
            # return n
        # elif n == 0 and m > 0:
            # return m
        # elif word1[-1] == word2[-1]:
            # return self.minDistance(word1[:-1], word2[:-1])
        # else:
            # insert_char = self.minDistance(word1 + word2[-1], word2)
            # delete_char = self.minDistance(word1[:-1], word2)
            # replace_char = self.minDistance(word1[:-1] + word2[-1], word2)

            # return 1 + min(insert_char, delete_char, replace_char)

        e = [[0 for j in range(m+1)] for i in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    e[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    e[i][j] = e[i-1][j-1]
                else:
                    e[i][j] = 1 + min(e[i-1][j], e[i][j-1], e[i-1][j-1])

        return e[n][m]


print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("intention", "execution"))
print(Solution().minDistance("dinitrophenylhydrazine", "benzalphenylhydrazone"))
