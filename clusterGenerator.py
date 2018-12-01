import random as rnd
import numpy as np
import math as mth
import matplotlib.pyplot as plt

#Cluster field metrics
clustFieldXSize = 3
clustFieldYSize = 3

#Cluster metrics
numberOfClusters = 2
numberOfPointsPerCluster = 30
stnDev = 1

#Cluster centers array
xCenter = []
yCenter = []

#Cluster arrays
xPoints = []
yPoints = []

#Create a Gaussian density function
def nrmlDist(x, mean, stanDev):
	ampli = (2 * mth.pi * stanDev ** 2) ** (-0.5)
	expon = -((x - mean) ** 2) / (2 * stanDev ** 2)
	return ampli * mth.e ** expon

#Generate cluster centers in a region specified by the field metrics
for i in range(numberOfClusters):
	xCenter.append(rnd.uniform(0, clustFieldXSize))
	yCenter.append(rnd.uniform(0, clustFieldYSize))

#Generate cluster point x and y arrays
for i in range(numberOfClusters):
	for x in range(numberOfPointsPerCluster):
		for y in range(numberOfPointsPerCluster):
			theta = rnd.uniform(0,2 * mth.pi)
			xPoints.append(xCenter[i] + rnd.random() * nrmlDist(0.1, 0, stnDev) * mth.cos(theta))
			yPoints.append(yCenter[i] + rnd.random() * nrmlDist(0.1, 0, stnDev) * mth.sin(theta))

#Plot the results
plt.plot(xPoints, yPoints, 'r.')
plt.show()

#Numpy print options to supress scientific notation
np.set_printoptions(suppress = True, formatter = {'float_kind':'{:f}'.format})

#Set as a 2d array
a = np.asarray([xPoints,yPoints])
np.savetxt("clust.csv", np.transpose(a), delimiter = ",")

#Save the centers array
centArray = np.asarray([xCenter,yCenter])
np.savetxt("cent.csv", np.transpose(centArray), delimiter = ",")
