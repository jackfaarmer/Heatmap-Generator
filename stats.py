## Stats module
##
## Author: Jack Farmer

import matplotlib.pyplot as plt

def getStats(xvals, areaSize):
    print("\nCalculating heatmap...")

    # generate regions to sift values into
    size = len(xvals)
    area0size = areaSize
    area1size = areaSize * 2
    area2size = areaSize * 3
    area3size = areaSize * 4
    area4size = areaSize * 5

    labels = ['Left', 'Left-Center', 'Center', 'Right-Center', 'Right']
    areacounts = [0, 0, 0, 0, 0]

    # sift values into correct regions
    for val in xvals:
        if val <= area0size: areacounts[0] += 1
        elif val > area0size and val <= area1size: areacounts[1] += 1
        elif val > area1size and val <= area2size: areacounts[2] += 1
        elif val > area2size and val <= area3size: areacounts[3] += 1
        elif val > area3size and val <= area4size: areacounts[4] += 1
    
    # calculate percentage values for each region
    areacounts[0] = areacounts[0] / size * 100
    areacounts[1] = areacounts[1] / size * 100
    areacounts[2] = areacounts[2] / size * 100
    areacounts[3] = areacounts[3] / size * 100
    areacounts[4] = areacounts[4] / size * 100

    # configure graph
    figure, axis = plt.subplots()
    axis.bar(labels, areacounts)

    # Set the title and labels for the graph
    axis.set_title('Heatmap Generation')
    axis.set_xlabel('Region')
    axis.set_ylabel('% Time spent')

    # show graph
    plt.show()
