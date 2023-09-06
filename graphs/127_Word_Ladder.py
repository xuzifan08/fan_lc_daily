class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # created a adjacent list for the patterns of each word
        word_pattern = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                word_pattern[pattern].append(word)


        # use queue to count the num of transformations and use a visited set to store the visited word in order to avoid redundent visits
        visited = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
           
            for i in range(len(q)):
                # visit layer by layer
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    # for each pattern
                    pattern = word[:j] + '*' + word[j + 1:]
                    for nei in word_pattern[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1

        return 0