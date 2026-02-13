from pymindlab import transform, util
import numpy as np
import imageio


def dyadic_cube(filename='./testImages/cell.png', rType='TV', alpha=0.5, snr=30, seed=123):
    np.random.seed(seed)
    X = np.double(imageio.imread(filename))
    X /= np.max(X)
    sz = X.shape
    sigma = 1/snr
    Xnoisy = X + sigma * np.random.normal(scale=1, size=sz)

    sgmh = util.stdIm(Xnoisy)

    cube = transform.Cube(sz)
    th = cube.msQuantile(alpha, seed=seed)[0]
    Xrec = cube.multiscale(Xnoisy, sgmh*th, rType=rType)

    return Xrec


def small_cube(filename='./testImages/cell.png', rType='TV', alpha=0.5, snr=30, seed=123):
    np.random.seed(seed)
    X = np.double(imageio.imread(filename))
    X /= np.max(X)
    sz = X.shape
    sigma = 1 / snr
    Xnoisy = X + sigma * np.random.normal(scale=1, size=sz)

    sgmh = util.stdIm(Xnoisy)

    cube = transform.Cube(sz, ctype='scale', param=np.arange(1, 31))
    th = cube.msQuantile(alpha, seed=seed)[0]
    Xrec = cube.multiscale(Xnoisy, sgmh * th, rType=rType)

    return Xrec


def wavelet(filename='./testImages/cell.png', rType='TV', alpha=0.5, snr=30, seed=123):
    np.random.seed(seed)
    X = np.double(imageio.imread(filename))
    X /= np.max(X)
    sz = X.shape
    sigma = 1 / snr
    Xnoisy = X + sigma * np.random.normal(scale=1, size=sz)

    sgmh = util.stdIm(Xnoisy)

    wave = transform.Wavelet(sz)
    th = wave.msQuantile(alpha, seed=seed)[0]
    Xrec = wave.multiscale(Xnoisy, sgmh * th, rType=rType)

    return Xrec


def shearlet(filename='./testImages/cell.png', rType='TV', alpha=0.5, snr=30, seed=123):
    np.random.seed(seed)
    X = np.double(imageio.imread(filename))
    X /= np.max(X)
    sz = X.shape
    sigma = 1 / snr
    Xnoisy = X + sigma * np.random.normal(scale=1, size=sz)

    sgmh = util.stdIm(Xnoisy)

    shear = transform.Shearlet(sz)
    th = shear.msQuantile(alpha, seed=seed)[0]
    Xrec = shear.multiscale(Xnoisy, sgmh * th, rType=rType)

    return Xrec