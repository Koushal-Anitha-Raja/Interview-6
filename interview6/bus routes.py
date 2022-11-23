class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
         # if source is equal to destination 
        if source == target:
            return 0
        #hashmap creating
        hmp = defaultdict(set)
        # creating the hashmap of frequencies of the bus and routes
        for bus, route in enumerate(routes): 
            for stop in route:
                #adding the hashmap value 
                hmp[stop].add(bus)
         # creating the deque
        q = deque()
        # appending the source and destination to queue
        q.append((source, 0)) 
         # a empty set 
        visited = set()
         # adding the source to visited
        visited.add(source)
        bus_seen = set() 

        #until queue is empty
        while q:
            stop, count = q.popleft()
             # if stop is equal to target then return count
            if stop == target:
                return count
            # for bus in hashmap of stop
            for bus in hmp[stop]:  
                # if bus is not in seen the add it in the seen
                if bus not in bus_seen:
                    #adding the bus value to set
                    bus_seen.add(bus)
                     # for every neighbour in routes and not in visted append the neighbour and count to q
                    for neighbor in routes[bus]:
                        #if neighbour in routes of bus
                        if neighbor not in visited:
                            #append the neighbour to queue and increse count to one
                            q.append((neighbor, count + 1))
                             # add the neighbour in the visited
                            visited.add(neighbor)
        return -1 # else return -1
        