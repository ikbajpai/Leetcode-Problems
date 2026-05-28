class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_len = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # function to update best candidate
        def update(node, idx):
            word_len = len(wordsContainer[idx])
            if (word_len < node.best_len or 
               (word_len == node.best_len and idx < node.best_index)):
                node.best_len = word_len
                node.best_index = idx

        # 🔹 Build Trie
        for i, word in enumerate(wordsContainer):
            node = root
            rev_word = word[::-1]

            update(node, i)

            for ch in rev_word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                update(node, i)
        ans = []

        for query in wordsQuery:
            node = root
            res = node.best_index

            for ch in query[::-1]:
                if ch not in node.children:
                    break
                node = node.children[ch]
                res = node.best_index

            ans.append(res)

        return ans