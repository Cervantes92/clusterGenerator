import random as rnd
import numpy as np

#Cluster field metrics
clustFieldXSize = 10
clustFieldYSize = 10

#Cluster metrics
numberOfClusters = 5
numberOfPointsPerCluster = 100
maxDistanceFromCenter = 4

#Cluster centers array
xCenter = []
yCenter = []

#Cluster arrays
xPoints = []
yPoints = []



#Generate cluster centers in a region specified by the field metrics
for i in range(numberOfClusters):
	xCenter.append(rnd.uniform(0, clustFieldXSize))
	yCenter.append(rnd.uniform(0, clustFieldYSize))

#Generate cluster point x and y arrays
for i in range(numberOfClusters):
	for x in range(numberOfPointsPerCluster):
		for y in range(numberOfPointsPerCluster):
			xPoints.append(xCenter[i] + rnd.uniform(-maxDistanceFromCenter,maxDistanceFromCenter))
			yPoints.append(yCenter[i] + rnd.uniform(-maxDistanceFromCenter,maxDistanceFromCenter))


#Set as a 2d array
a = np.asarray([xPoints, yPoints])
np.savetxt("clust.csv", a, delimiter = ",")