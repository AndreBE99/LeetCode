#
# O(NLogN)
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    strs=sorted(strs)
    result=""
    first=strs[0]
    last=strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i]!=last[i]:
            return(result)
        result=result+first[i]
    return(result)

if __name__ == '__main__':
    test_strings = [
        "flower",
        "flow",
        "flight"
    ]

    print(f'Input: {test_strings}')
    print(f'Output: {longestCommonPrefix(test_strings)}')