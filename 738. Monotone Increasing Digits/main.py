class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums_list = list(str(n))
        length = len(nums_list)
        print(nums_list)
        flag = False
        pointer_9 = length
        if length == 1:
            return n
        for i in range(length-1, -1, -1):
            if flag == True:
                nums_list[i] = str(int(nums_list[i]) - 1)
                flag = False
                print("true flag",nums_list[i])
            if nums_list[i] < nums_list[i-1] and i!=0:
                flag = True
                pointer_9 = i

        for j in range(pointer_9, length):
            nums_list[j] = "9"
                #print("less than",nums_list[i])       
        #nums_list = list(map(str, nums_list))
        n = int(''.join(nums_list))
        return n
                #nums_list[i-1] = 
        '''for i in range(0,length-1):
            if nums_list[i+1] <= nums_list[i]:
                flag = True
                if flag == True:
                    first_digit = str(int(nums_list[0])-1)
                    result_number = int(first_digit + "9"*(length-1))
                    return result_number'''
        #if flag == False:
        