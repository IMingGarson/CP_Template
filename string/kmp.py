def kmp(search, target):
  ret = []
  if not target:
      return ret
  
  n = len(target)
  lps = [0 for i in range(n)]
  
  i = 0
  j = 1
  
  while j < n:
      if target[i] == target[j]:
          lps[j] = lps[i] + 1
          i += 1
          j += 1
      else:
          if i == 0:
              j += 1
          else:
              i = lps[i-1]
  
  i = 0
  j = 0
  
  while i < len(search):
      if search[i] == target[j]:
          i += 1
          j += 1
      else:
          if j == 0:
              i += 1
          else:
              j = lps[j - 1]
      
      if j == len(target):
          ret.append(i - j)
          j = lps[j - 1]
  
  return ret
