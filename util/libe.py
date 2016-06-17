import numpy as np
import numpy.linalg as la


'''
Perform the PCA on the data matrix.  Return the leading ('v[1]') and 
subleading ('v[0]') principal components (pc's) and a two-element array ('w') 
storing the fraction of total variation described by each pc.
'''
def pca_2(data_matrix):
    
    # Center the data.
    means = np.mean(data_matrix, 1)
    data_matrix = np.array(
        [data_matrix[i] - means[i] for i in xrange(len(means))])
    
    # Calculate the covariance matrix. (The covariances of time series for 
    # each node in the network with all other times series.)
    cov_matrix = data_matrix.dot(data_matrix.T)
    
    # Calculate the eigenvalues (w) and eigenvectors (v) of the covariance 
    # matrix.  The function 'la.eigh' returns 'w' sorted in ascending order
    # with eigenvalue w[0] corresponding to eigenvector v[0], w[1] to v[1], etc.
    w, v = la.eigh(cov_matrix)
    
    # Normalize the eigenvalues such that 'w' sums to 1.  The elements of 'w'
    # now describe the fraction of total variation in the data described by 
    # each of pc (i.e., each element of 'v').
    w /= np.sum(w)
    
    # Return information on the first two pc's only.
    return w[-2:], v[:, -2:]              
    
  
'''  
Define a function takes a single pc as an argument and return an array of 
RGB colors and opacities to use in displaying the pc on a map.
Note: The overall sign of the pc's is arbitrary.  Here, I choose to plot 
positive components in blue and negative components in red.  
'''
def make_color_array(pc):
    
    # Each row of color_array is a 4-component vector of values between 0 and 1.
    # The first 3 components specify RGB color fractions.  The third component
    # specifies opacity.
    color_array = np.zeros((len(pc), 4)) 
    
    norm = abs(max(pc)) if abs(max(pc)) > abs(min(pc)) else abs(min(pc))
        
    for j, val in enumerate(pc):
        
        if val > 0.:  
                  
            color_array[j, 0] = 0. # Red fraction.
            color_array[j, 1] = 0. # Green fraction.
            color_array[j, 2] = 1. # Blue fraction.
            color_array[j, 3] = val / norm # Opacity.
        
        else:
            
            color_array[j, 0] = 1. # Red fraction.
            color_array[j, 1] = 0. # Green fraction.
            color_array[j, 2] = 0. # Blue fraction.
            color_array[j, 3] = -val / norm # Opacity.       
        
    return color_array    


if __name__ == "__main__":
    
    pass
    