
class Solution(object):
    def makeFancyString(self, s: str) -> str:
        ls = list(s)
        remove_idx = []
        current_char = ''
        counter = 0
        for idx, char in enumerate(ls):
            if current_char == char:
                counter += 1
                if counter > 1:
                    remove_idx.append(idx)
            else:
                counter = 0
                current_char = char
        for idx in remove_idx[::-1]:
            ls.pop(idx)
        return ''.join(ls)
            
            
if __name__ == '__main__':
    solution = Solution()
    s1 = "leeetcode"
    s2 = "aaabaaaa"
    s3="aab"
    print(solution.makeFancyString(s1))
    print(solution.makeFancyString(s2))
    print(solution.makeFancyString(s3))
    
