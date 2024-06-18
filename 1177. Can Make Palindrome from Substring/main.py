class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        #print(s)
        #print(queries)
        boolean_list = []
        for query in queries:
            left = query[0]
            right = query[1]
            changes = query[2]
            substring = list(s)[left:right+1]
            if changes == 0:                
                reverse_substring = substring[::-1]
                #print(substring, reverse_substring)
                if ''.join(substring) == ''.join(reverse_substring):
                    boolean_list.append(True)
                else:
                    boolean_list.append(False)
            else:
                no_changes = 0   
                length = right-left+1
                print(length)
                print("substring", substring)            
                for j in range(0, (length//2)):
                    print("inside for")
                    if substring[j] != substring[length-j-1]:
                        no_changes += 1
                if no_changes > changes:
                    boolean_list.append(False)
                else:
                    boolean_list.append(True)
        return boolean_list
        