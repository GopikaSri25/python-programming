class Solution(object):
    def makeEqual(self, words):
        char_cnt = defaultdict(int)
        for w in words:
            for c in w:
                char_cnt[c] += 1
        for count in char_cnt.values():

            if count % len(words):
                return False
        
        return True
