class Solution(object):
  def isValid(self, s):
        t={
        ')' : '(',
        '}' : '{',
        ']' : '[',
        }
        r = []
        for x in s:
            if x in t:
                if  not r or  r.pop() != t[x] :
                    return False
            else:
                r.append(x)
        return not r
