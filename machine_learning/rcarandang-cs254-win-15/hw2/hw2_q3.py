import math
from PIL import Image
from scipy.cluster.vq import vq, kmeans, whiten
import matplotlib.pyplot as plt
import numpy as np

# Problem 2
def get_centroids():
        # 2a read in as arrays
	in_image = Image.open('hw2-data/mandrill-small.tiff')
	i1 = np.asarray(in_image)
	i1_reshape = i1.reshape(16384,3)

	in_image = Image.open('hw2-data/mandrill-large.tiff')
	i2 = np.asarray(in_image)

        # 2b get cluster centroid with kmeans
	centroids, dist = kmeans(i1_reshape, 16, iter=100, thresh=1e-06)

	return i1, i2, centroids, dist

def get_cluster_rep(x, centroids):
	cluster_rep= x
	min_so_far = 1000
	for color in centroids:
		distance = np.linalg.norm(np.array(color)- np.array(x))
		if distance < min_so_far:
			min_so_far = distance
			cluster_rep = color
	return cluster_rep

# 2c
# Save compressed image "my-output-mandrill-large.tiff"
i1, i2, centroids, dist = get_centroids()
nrows = len(i2)
npix = len(i2[0])

out_array = np.zeros((nrows, npix, 3))

for i in range(nrows):
        for j in range(npix):
                out_array[i][j] = get_cluster_rep(i2[i][j], centroids)

out_array = np.uint8(out_array)
out_image = Image.fromarray(out_array, "RGB")
out_image.save("my-output-mandrill-large.tiff")
