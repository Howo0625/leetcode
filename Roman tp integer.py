class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        flag = 0
        for i in range(len(s)-1,-1,-1):
            if flag == 1:
                flag = 0
                continue
            if s[i] == 'I':
                if flag == 0:
                    sum += 1
            elif s[i] == 'V':
                    if flag == 0:
                        if s[i-1] != 'I':
                            sum += 5
                        elif i == 0:
                            sum += 5
                        else:
                            sum += 4
                            i -= 1
                            flag = 1
            elif s[i] == 'X':
                if flag == 0:
                        if s[i-1] != 'I':
                            sum += 10
                        elif i == 0:
                            sum += 10
                        else:
                            sum += 9
                            i -= 1
                            flag = 1
            elif s[i] == 'L':
                if flag == 0:
                    if s[i-1] != 'X':
                        sum += 50
                    elif i == 0:
                        sum += 50
                    else:
                        sum += 40
                        i -= 1
                        flag = 1
            elif s[i] == 'C':
                if flag == 0:
                    if s[i-1] != 'X':
                        sum += 100
                    elif i == 0:
                        sum += 100
                    else:
                        sum += 90
                        i -= 1
                        flag = 1
            elif s[i] == 'D':
                if flag == 0:
                    if s[i-1] != 'C':
                        sum += 500
                    elif i == 0:
                        sum += 500
                    else:
                        sum += 400
                        i -= 1
                        flag = 1
            else :
                if flag == 0:
                    if s[i-1] != 'C':
                        sum += 1000
                    elif i == 0:
                        sum += 1000
                    else:
                        sum += 900
                        i -= 1
                        flag = 1
            print(i,sum)
        return sum
