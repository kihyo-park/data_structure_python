import os

"""This prints out a direct subdirectory only"""
# def print_subdirectiories(directory_name): 

#     for filename in os.listdir(directory_name):
#         if os.path.isdir(filename):
#             path = os.path.join(directory_name, filename)
#             print(path)

"""This prints out subdirectories"""
# def print_subdirectiories(directory_name): 

#     for filename in os.listdir(directory_name):
#         if os.path.isdir(filename):
#             path = os.path.join(directory_name, filename)
#             print(path)

#             for filename2 in os.listdir(path):
#                 path2 = os.path.join(path, filename2)
#                 if os.path.isdir(path2):
#                     print(path2)

# This O(n^2). We need to be efficient.

"""Recursion prints out subdirectories"""
def print_subdirectiories(directory_name): 

    for filename in os.listdir(directory_name):
        path = os.path.join(directory_name, filename)
        if os.path.isdir(path):
            print(path)
            print_subdirectiories(path)

print_subdirectiories(".")
