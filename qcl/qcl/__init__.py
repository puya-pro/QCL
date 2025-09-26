 
"""
The QuearaContestLib For Cheating In Queara Coding Race
-------------------------------------------------------
    By :
        Ali DianatSeresht
        Arad Asgary
        Puya Taati    
"""

class QuearaContestLib:
    def SortBy(self,order, words):
        """For Quearanumic Question"""
        rank = {ch: i for i, ch in enumerate(order)}

        fallback = len(order) + 1000
        def key_func(word):
            return tuple(rank.get(ch, fallback + ord(ch)) for ch in word)

        return sorted(words, key=key_func)
    