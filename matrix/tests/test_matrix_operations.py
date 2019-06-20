"""
Testing here assumes that numpy is ALWAYS correct!!!!

If running from PyCharm you can place the following line in "Additional Arguments" for the pytest run configuration
-vv -m mat_ops -p no:cacheprovider
"""

# standard libraries
import numpy as np
import pytest

# Custom/local libraries
from matrix import matrix_operation as matop

mat_a = [[12, 10], [3, 9]]
mat_b = [[3, 4], [7, 4]]
mat_c = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
mat_d = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
mat_e = [[3, 0, 2], [2, 0, -2], [0, 1, 1], [2, 0, -2]]
mat_f = [1]
mat_h = [2]


@pytest.mark.mat_ops
@pytest.mark.parametrize(('mat1', 'mat2'), [(mat_a, mat_b), (mat_c, mat_d), (mat_d, mat_e),
                                            (mat_f, mat_h)])
def test_addition(mat1, mat2):
    # Catch when user enters a single integer value rather than a mat
    # Check for known errors
    if (np.array(mat1)).shape < (2, 2) or (np.array(mat2)).shape < (2, 2):
        with pytest.raises(TypeError):
            assert matop.add(mat1, mat2)
    elif (np.array(mat1)).shape == (np.array(mat2)).shape:
        act = (np.array(mat1) + np.array(mat2)).tolist()
        theo = matop.add(mat1, mat2)
        assert theo == act
    else:
        # matrices have different dimensions
        # Check for known errors
        with pytest.raises(ValueError):
            assert matop.add(mat1, mat2)


@pytest.mark.mat_ops
@pytest.mark.parametrize(('mat1', 'mat2'), [(mat_a, mat_b), (mat_c, mat_d), (mat_d, mat_e),
                                            (mat_f, mat_h)])
def test_subtraction(mat1, mat2):
    # Catch when user enters a single integer value rather than a mat
    # Check for known errors
    if (np.array(mat1)).shape < (2, 2) or (np.array(mat2)).shape < (2, 2):
        with pytest.raises(TypeError):
            assert matop.add(mat1, mat2)
    elif (np.array(mat1)).shape == (np.array(mat2)).shape:
        act = (np.array(mat1) - np.array(mat2)).tolist()
        theo = matop.subtract(mat1, mat2)
        assert theo == act
    else:
        # matrices have different dimensions
        # Check for known errors
        with pytest.raises(ValueError):
            assert matop.subtract(mat1, mat2)


@pytest.mark.mat_ops
@pytest.mark.parametrize(('mat1', 'mat2'), [(mat_a, mat_b), (mat_c, mat_d), (mat_d, mat_e),
                                            (mat_f, mat_h)])
def test_multiplication(mat1, mat2):
    # Catch when user enters a single integer value rather than a mat
    # Check for known errors
    if (np.array(mat1)).shape < (2, 2) or (np.array(mat2)).shape < (2, 2):
        with pytest.raises(TypeError):
            assert matop.add(mat1, mat2)
    elif (np.array(mat1)).shape == (np.array(mat2)).shape:
        act = (np.matmul(mat1, mat2)).tolist()
        theo = matop.multiply(mat1, mat2)
        assert theo == act
    else:
        # matrices have different dimensions
        # Check for known errors
        with pytest.raises(ValueError):
            assert matop.subtract(mat1, mat2)
