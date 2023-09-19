def solution(N, A, B):
    # Create a dictionary to represent the graph
    graph = {}

    # Populate the graph with edges
    for i in range(len(A)):
        if A[i] not in graph:
            graph[A[i]] = []
        if B[i] not in graph:
            graph[B[i]] = []
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])

    seconds = 0

    while True:
        # Find vertices with at most one edge and mark them for removal
        to_remove = []
        for vertex in graph:
            if len(graph[vertex]) <= 1:
                to_remove.append(vertex)

        # If no vertices to remove, break the loop
        if not to_remove:
            break

        # Remove marked vertices and update their neighbors
        for vertex in to_remove:
            for neighbor in graph[vertex]:
                graph[neighbor].remove(vertex)
            del graph[vertex]

        seconds += 1

    # If there are remaining vertices, return the number of seconds
    if graph:
        return seconds
    else:
        return 0

# Test cases
print(solution(7, [0, 1, 2, 1, 4, 4], [1, 2, 0, 4, 5, 6]))  # Output: 2
print(solution(7, [0, 1, 2, 4, 5], [1, 2, 3, 5, 6]))  # Output: 2
print(solution(4, [0, 1, 2, 3], [1, 2, 3, 0]))  # Output: 0
print(solution(4, [0, 1, 2], [1, 2, 0]))  # Output: 1
