# coding = utf-8
'''

@author: wenlong
'''
class Solution(object):
    
    def __init__(self):
        
        lineStr1 = "qwertyuiop"
        lineStr2 = "asdfghjkl"
        lineStr3 = "zxcvbnm"
        
        lineStrArr = [ lineStr1, lineStr2, lineStr3 ]
        
        self.charValMap = {}
        
        i = 0
        for strVal in lineStrArr:
            for charVal in strVal:
                self.charValMap[charVal] = i
                self.charValMap[charVal.upper()] = i
            i = i + 1
            
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        retArr = []
        for word in words:
            index = -1
            for char in word:
                if index == -1:
                    index = self.charValMap[char]
                elif not index == self.charValMap[char]:
                    index = -1
                    break
            if index >= 0:
                retArr.append(word)
        return retArr
            
if __name__ == '__main__':
    xx = Solution()
    print xx.findWords(["qwee"])
    pass