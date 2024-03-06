# Find Max
class SparseTableMax:
  def __init__(self, array):
      self.array = array
      self.n = len(array)
      self.k = (self.n).bit_length()  # Number of levels in the sparse table
      self.table = [[0] * self.k for _ in range(self.n)]

      # Initializing the sparse table with the original array
      for i in range(self.n):
          self.table[i][0] = array[i]

      # Preprocessing to fill the sparse table
      for j in range(1, self.k):
          for i in range(self.n - (1 << j) + 1):
              self.table[i][j] = max(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])

  def query(self, left, right):
      """
      Returns the maximum value in the range [left, right] (inclusive).
      """
      length = right - left + 1
      k = length.bit_length() - 1  # Finding the highest power of 2 less than or equal to length
      return max(self.table[left][k], self.table[right - (1 << k) + 1][k])

# Find Min
class SparseTableMin:
  def __init__(self, array):
      self.array = array
      self.n = len(array)
      self.k = (self.n).bit_length()  # Number of levels in the sparse table
      self.table = [[0] * self.k for _ in range(self.n)]

      # Initializing the sparse table with the original array
      for i in range(self.n):
          self.table[i][0] = array[i]

      # Preprocessing to fill the sparse table with minimum values
      for j in range(1, self.k):
          for i in range(self.n - (1 << j) + 1):
              self.table[i][j] = min(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])

  def query(self, left, right):
      """
      Returns the minimum value in the range [left, right] (inclusive).
      """
      length = right - left + 1
      k = length.bit_length() - 1  # Finding the highest power of 2 less than or equal to length
      return min(self.table[left][k], self.table[right - (1 << k) + 1][k])
