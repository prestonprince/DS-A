# Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. 
# Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. 
# Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a 
# single semester, as long the prerequisites of a course are satisfied before taking it.

# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. 
# You must take A in some semester before B.

# You can assume that it is possible to eventually complete all courses.

num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]


def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    distance = {}

    for course in graph:
        if len(graph[course]) == 0:
             distance[course] = 1
    
    for course in range(num_courses):
        traverse(graph, course, distance)
    
    return max(distance.values())


def traverse(graph, node, distance):
    if node in distance:
        return distance[node]


    longest = 0
    for neighbor in graph[node]:
        length = traverse(graph, neighbor, distance)
        if length > longest: longest = length
    
    distance[node] = 1 + longest
    return distance[node]


def build_graph(num_courses, prereqs):
    graph = {}

    for course in range(num_courses):
        graph[course] = []
    
    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


print(semesters_required(num_courses, prereqs)) # -> 3
