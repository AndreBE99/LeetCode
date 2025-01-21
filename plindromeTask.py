def isPalindrome(s: str) -> bool:
  aux = str(s)
  if aux == aux[::-1]:
    return True
  return False


if __name__ == '__main__':
  s = 'aulua'
  print(f'Output: {isPalindrome(s)}')