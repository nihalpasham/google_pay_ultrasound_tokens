
# based on example from matlab sinc function and
# interpolate.m by H. Hobæk (1994).
#
# this implementation is similar to the matlab sinc-example, but
# calculates the values sequentially and not as a single matrix
# matrix operation for all the values.
#

import scipy as sc
import numpy as np


def upsample (x, k):
  """
  Upsample the signal to the given ratio using a sinc kernel
  input:
    x   a vector or matrix with a signal in each row
    k   ratio to resample to
    returns
    y   the up or downsampled signal
    when downsampling the signal will be decimated using scipy.signal.decimate
  """

  assert k >= 1, 'k must be equal or greater than 1'

  mn = x.shape
  if len(mn) == 2:
    m = mn[0]
    n = mn[1]
  elif len(mn) == 1:
    m = 1
    n = mn[0]
  else:
    raise ValueError ("x is greater than 2D")

  nn = n * k

  xt = np.linspace (1, n, n)
  xp = np.linspace (1, n, nn)

  return interp (xp, xt, x)


def interp (xp, xt, x):
  """
  Interpolate the signal to the new points using a sinc kernel
  input:
  xt    time points x is defined on
  x     input signal column vector or matrix, with a signal in each row
  xp    points to evaluate the new signal on
  output:
  y     the interpolated signal at points xp
  """

  mn = x.shape
  if len(mn) == 2:
    m = mn[0]
    n = mn[1]
  elif len(mn) == 1:
    m = 1
    n = mn[0]
  else:
    raise ValueError ("x is greater than 2D")

  nn = len(xp)

  y = np.zeros((m, nn))

  for (pi, p) in enumerate (xp):
    si = np.tile(np.sinc (xt - p), (m, 1))
    y[:, pi] = np.sum(si * x)

  return y.squeeze ()

