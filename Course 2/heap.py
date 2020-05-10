# Operations that a heap needs to support:
# 1. Insert
# 2. Extract-Min
# 3. Heapify Up
# 4. Heapify Down
# 5. Delete

import heapq

li = [22, 45, 87, 2, 4]

heapq.heapify(li)

print(li)

# How many nodes can be there at nth level 2^k....
