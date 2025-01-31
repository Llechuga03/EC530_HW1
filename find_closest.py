from scipy.spatial import KDTree #Library with the KD-tree data structure

#Function that finds the closest points, using a K tree and kth nearest neighbor algorithm
def find_closest_points(pointsA, pointsB):
    tree = KDTree(pointsB) #Construct the tree
    closest_indices = tree.query(pointsA)[1] #storing the closest point in pointsB to pointsA
    return [pointsB[i] for i in closest_indices] #returns nearest neighbors in pointsB
