import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    dim = np.ndim(arr)
    if dim == 1 and norm_type == 'frobenius':
        raise ValueError
    norms = {
            'l1': float(np.sum(np.abs(arr))),
            'l2': np.sqrt(np.sum(arr**2)),
            'linf': float(np.max(np.abs(arr)))
        }
        
    norms['frobenius'] = np.sqrt(np.sum(arr**2))
    return norms[norm_type]