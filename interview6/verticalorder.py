# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #empty array
        result = []
        #creating a hashmap
        hashmap= defaultdict(list)
        q = deque()
        #create queue and providing it root values
        q.append((root,0))

        #until queue is empty
        while q:
            #size parameter for each stage
            size=len(q)
            #level array to store at each level
            level=[]
            #iterate throgugh the size
            for _ in range(size):
                #pop from queue and store it in node
                node,v = q.popleft()
                #then add value to hashmap
                hashmap[v].append(node.val)
                #if leftnode is present
                if node.left:
                    level.append((node.left,v-1)) 
                    #if right node is present
                if node.right:
                    level.append((node.right,v+1))
                    #level array sort with lamda function
            level.sort(key = lambda x: (x[1], x[0].val))
            q = deque(level)
            #hashmap is sorted with hashmap key and values
        hashmap = OrderedDict(sorted(hashmap.items()))
        print(hashmap)
        #iterate through key and value pairs
        for k,v in hashmap.items():
            #append the result with values
            result.append(v)

        return result

        
       
                    
            
        
        