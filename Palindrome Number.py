class Solution:
    def isPalindrome(self, x: int) -> bool:
        list = []
        flag = 0
        
        if x<0:
            flag=1
        else:
            while x/10 != 0:
                list.append(x%10)
                x = x//10
            for i in range(0,len(list)//2):
                    if list[i] != list[len(list)-i-1]:
                        flag = 1
            
        if flag == 0:
            return True
        if flag == 1:
            return False
