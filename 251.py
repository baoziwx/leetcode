# 251. Flatten 2D Vector

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = vec2d
        self.row_pos = 0
        self.col_pos = 0


#     def next(self):
#         """
#         :rtype: int
#         """

# #         if len(self.data[self.row_pos]) == 0:
# # #           current row  empty
# #             self.col_pos +=
#         self.row_pos, self.col_pos = self.getNextPos()
#         print self.row_pos, self.col_pos, len(self.data)
#         res = self.data[self.row_pos][self.col_pos]

#         # if self.col_pos == len(self.data[self.row_pos]) - 1:
#         #     self.row_pos += 1
#         #     self.col_pos = 0
#         # else:
#         #     self.col_pos += 1
#         return res
        # @return {integer}
    def next(self):
        result = self.data[self.row_pos][self.col_pos]
        self.col_pos += 1
        return result

    # @return {boolean}
    def hasNext(self):
        while self.row_pos < len(self.data):
            if self.col_pos < len(self.data[self.row_pos]):
                return True

            self.col_pos = 0
            self.row_pos += 1

        return False

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         new_row, new_col = self.getNextPos()
#         # print
#         return len(self.data) > new_row
#         # print self.row_pos, self.col_pos, len(self.data)
#         # return len(self.data) > self.row_pos + 1 and len(self.data[self.row_pos]) > 0 #or (len(self.data) == self.row_pos and len(self.data[self.row_pos]) > self.col_pos)

#     def getNextPos(self):
#         row_pos, col_pos = self.row_pos, self.col_pos
#         if col_pos < len(self.data[row_pos]):
#             col_pos += 1
#         while row_pos < len(self.data) and col_pos >= len(self.data[row_pos]):
#             row_pos += 1
#             col_pos = 0
#         return (row_pos, col_pos)


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())