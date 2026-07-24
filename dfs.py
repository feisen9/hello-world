"""
Depth-First Search (DFS) Implementation in Python

This module provides a basic implementation of the Depth-First Search algorithm
for traversing or searching graph data structures.
"""

def dfs_recursive(graph, node, visited=None):
    """
    Perform DFS recursively on a graph.
    
    Args:
        graph: A dictionary representing the adjacency list of the graph.
               Example: {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
        node: The starting node for DFS traversal.
        visited: A set to keep track of visited nodes (used internally).
    
    Returns:
        A list of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()
    
    visited.add(node)
    result = [node]
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    Perform DFS iteratively using a stack.
    
    Args:
        graph: A dictionary representing the adjacency list of the graph.
        start: The starting node for DFS traversal.
    
    Returns:
        A list of nodes in the order they were visited.
    """
    if start not in graph:
        return []
    
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors to stack in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


# Example usage
if __name__ == "__main__":
    # Sample graph represented as an adjacency list
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print("Graph:", sample_graph)
    print("\nDFS Recursive (starting from 'A'):")
    recursive_result = dfs_recursive(sample_graph, 'A')
    print("Traversal order:", " -> ".join(recursive_result))
    
    print("\nDFS Iterative (starting from 'A'):")
    iterative_result = dfs_iterative(sample_graph, 'A')
    print("Traversal order:", " -> ".join(iterative_result))
