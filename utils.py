from skimage import filters
import numpy as np

def sharpest_frame_laplacian(stack):
    """Find the index of the sharpest frame using Laplacian variance."""
    sharpness = [filters.laplace(frame).var() for frame in stack]
    return np.argmax(sharpness)  # Index of the sharpest frame

def mask_from_df(df, shape, prefix=''):
    """
    Generates a labeled mask from a dataframe containing regionprops-style information.

    This function reconstructs a full-sized labeled mask from region-level 
    information (e.g., bounding boxes and corresponding subregion masks) typically 
    produced by `regionprops_table`. It places each labeled object at its correct 
    location in the full image.

    Parameters
    ----------
    df : pandas.DataFrame
        A dataframe with region-level data. Expected to contain at least the following 
        columns, optionally prefixed:
        - '<prefix>bbox-0', '<prefix>bbox-1', '<prefix>bbox-2', '<prefix>bbox-3' : 
          Bounding box coordinates (min_row, min_col, max_row, max_col).
        - '<prefix>image' : A 2D boolean or integer array representing the object mask 
          within its bounding box.
        - '<prefix>label' : An integer label identifying the object.
    
    shape : tuple of int
        The shape (height, width) of the full-size output mask.

    prefix : str, optional
        A string prefix prepended to column names in the dataframe, useful if multiple 
        regionprops outputs are stored in a single dataframe (default is '').

    Returns
    -------
    numpy.ndarray
        A 2D `np.uint16` array of the same shape as `shape`, where each object is 
        placed according to its bounding box and assigned its corresponding label.
    """
    
    mask = np.zeros(shape, dtype=np.uint16)
    for i, row in df.iterrows():
        row_start = int(row[f'{prefix}bbox-0'])
        row_stop = int(row[f'{prefix}bbox-2'])
        col_start = int(row[f'{prefix}bbox-1'])
        col_stop = int(row[f'{prefix}bbox-3'])
        patch = mask[row_start:row_stop, col_start:col_stop]
        mask[row_start:row_stop, col_start:col_stop] = patch + row[f'{prefix}image']*row[f'{prefix}label']
    return mask