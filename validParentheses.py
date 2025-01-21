# Valid Parentheses
# Solucion 1:
# def isValid(s: str) -> bool:
#   counter = 0
#   parentheses = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}

#   for i in range(len(s)):
#     counter += parentheses[s[i]]

#   if counter == 0: return True
#   return False

# Solucion 2
# Time complexity: O(n)
def isValid(s: str) -> bool:
  pairs = {')': '(', '}': '{', ']': '['}
  stack = []
  for char in s:
    if char in pairs.values(): stack.append(char)
    elif char in pairs:
      if not stack or stack.pop() != pairs[char]: return False
  
  return len(stack) == 0

if __name__ == '__main__':
  test_strings = [
    '()',
    '()[]{}',
    '(]',
    '([])'
  ]
  for s in test_strings:
    print(f'Input string: {s}')
    print(f'Output: {isValid(s)}')