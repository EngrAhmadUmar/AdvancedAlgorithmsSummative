# Importing heapq which we will be using to sort this problem out
import heapq

edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]

# Initializing my function that i will use to create an adjacency matrix to help represent the graph
def createAdjacencyMatrix(edges):
    # Storing our graph as a list of tuples with all the different edges as keys
    # And values being the edges they're related to and their weight
    graph = {}
    for i in range(1, len(edges)+1):
        graph[i] = []
    # Looping through the edges array
    for i in edges:
        a, b, c = i[0], i[1], i[2]
        # We map them against each other because we have undirected linked edges.
        # Tuples are used to hold the content of the values, such as the connecting edge and weight.
        if a not in graph or b not in graph:
            # Storing an as key and (b,c) as value for the first
            # Occurrence of a and b, and vice versa for b
            graph[a] = (b, c)
            graph[b] = (a, c)
        else:
            # If we have seen the edge we just append it
            graph[a].append((b, c))
            graph[b].append((a, c))

    # Returning our result
    return graph

# Creating a function that will take in the number of edges, the list of edges and the starting point.
# Then it return the shortest path
def shortestPath(n, edges, s):
    # Initializing a dictionary to keep track of our shortest path.
    answer = {}
    for a in range(1, n + 1):
        answer[a] = float('inf')

    # We initialize s's position in dictionary to zero because we start at that position.
    answer[s] = 0

    # We create an adjacency matrix of the with to represent the graph of our edges array.
    graph = createAdjacencyMatrix(edges)

    # Initializing the heap and adding the weight and the starting node.
    heap = [(0, s)]

    # We run a Breadth First Search while our heap is not empty.
    while heap:
        t = heapq.heappop(heap)
        for h in graph[t[1]]:
            # Set the connecting edge weight to the total of the original weight of the edge plus the current weight
            # If the connecting edge weight is larger than the original weight of the edge plus the current weight.
            if answer[h[0]] > answer[t[1]] + h[1]:
                answer[h[0]] = answer[t[1]] + h[1]
                # If the tuple is already in the heap, delete it and sort the heap using the heapify() function.
                if (h[1], h[0]) in heap:
                    heap.remove((h[1], h[0]))
                    heapq.heapify(heap)
                # Adding the edge and its current weight to the heap
                heapq.heappush(heap, (answer[h[0]], h[0]))

    # Initializing our result array
    shortest_reach = []
    # We go through the dictionary with values as the shortest path and add the values to our result array.
    for i in answer:
        shortest_reach.append(answer[i])
    # Returning our result
    return shortest_reach[1:]


s = 1
print("The shortest paths followed for the three nodes 2, 3 and 4 are as follows :")
print(shortestPath(len(edges), edges, s))
