# Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. 
# Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be 
# taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]

def prereqs_possible(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    visited = set()
    
    for node in graph:
        if is_cycle(graph, node, set(), visited):
            return False
    return True

def is_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if is_cycle(graph, neighbor, visiting, visited):
            return True
    
    visited.add(node)
    visiting.remove(node)
    return False

def build_graph(num_courses, prereqs):
    graph = {}

    for course in range(num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph

print(prereqs_possible(numCourses, prereqs)) # -> True
