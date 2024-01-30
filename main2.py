"""
2707. Extra Characters in a String
"""

class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """

        d2 = [word for word in dictionary if word in s]
        seqs = list(self.permutations(d2))[:500]

        length = len(s)
        for d in seqs:
            print(d)
            sub = s
            l = len(sub)
            for word in d:
                if word in s:
                    sub = sub.replace(word, "").strip()
                    print(len(sub))
                    if len(sub) < l:
                        l = len(sub)
                        if l < length:
                            length = l
            if l == 1:
                break
        return length

    def permutations(self, elementos):
        if len(elementos) == 0:
            return [[]]  # Lista vazia representa uma permutação vazia

        resultado = []
        for i in range(len(elementos)):
            elemento_atual = elementos[i]
            restante = elementos[:i] + elementos[i + 1:]

            for p in self.permutations(restante):
                resultado.append([elemento_atual] + p)

        return resultado


if __name__ == '__main__':
    s = "octncmdbgnxapjoqlofuzypthlytkmchayflwky"
    dictionary = ["qz","tpf","hlrc","j","l","tew","xbn","a","uzypt","uvln","mchay","onnbi","hlytk","pjoqlo","dxsjr","u","uj"]

    sol = Solution()
    print(sol.minExtraChar(s, dictionary))
