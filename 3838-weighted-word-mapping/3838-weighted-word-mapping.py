class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n = len(words)
        ans=[]
        for i in range(n):
            sum=0
            string_element=words[i]
            for element in string_element:
                sum+=weights[ord(element) - ord('a')]
            if sum!=0:
                sum = sum%26
                sum=26-sum
            ans.append(chr(97+sum-1))
        return "".join(ans)
