# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:42:03 2014

@author: Eric

2014-02-16: okay, you have the Gaussian cloud, but add some noise to it!
"""

import math
import matplotlib.pyplot as plt
import numpy as np



def main(plotDistributionL = True):
    """Creates a simple distribution comprised of three Gaussian-noise, Gaussian-shaped probability clouds with a Gaussian-noise background."""

    numXPoints = 200
    numYPoints = 200
    distributionM = abs(np.random.randn(numXPoints, numYPoints))
    
    # Add background noise
    cloudCenter2C = np.array([[30, 15],
                              [20, 30],
                              [100, 100]])
    cloudMagnitudeC = np.array([10, 7, 15])
    cloudWidthC = np.array([7, 7, 7])
    
    # Add Gaussian clouds with Gaussian noise
    numClouds = cloudCenter2C.shape[0]
    for lCloud in range(numClouds):
        additionalDistributionM = np.array(np.empty(distributionM.shape))
        additionalDistributionM.fill(np.nan)
        # Create empty array containing the amount by which this cloud adds onto the existing distribution
        
        for lXPoint in range(numXPoints):
            for lYPoint in range(numYPoints):
                
                # Setting up the exponential
                squaredDistance = \
                    math.sqrt((lXPoint-cloudCenter2C[lCloud, 0])**2 +
                    (lYPoint-cloudCenter2C[lCloud, 1])**2)
                sigma = cloudWidthC[lCloud]
                magnitude = cloudMagnitudeC[lCloud]
                additionalDistributionM[lXPoint, lYPoint] = \
                    magnitude/(sigma*math.sqrt(2*math.pi)) * \
                    math.exp(-squaredDistance/(2*sigma**2))
                    
        distributionM += additionalDistributionM
        
    if plotDistributionL:
        plot_sample_distribution(distributionM)
        
    return distributionM
    
    
    
def plot_sample_distribution(distributionM):
    plt.imshow(distributionM)
    
    

if __name__ == "__main__":
    main(plotDistributionL = True)