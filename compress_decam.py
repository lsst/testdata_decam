#!/usr/bin/env python
"""Zero out the imageHDUs in the calibrations, and then tile compress the files.

Note: due to an astropy/cfitsio segfault, the FITS files have to be `funpack`ed
first.
"""
from __future__ import absolute_import, division, print_function

from astropy.io import fits
import glob
import os.path
import subprocess

files = glob.glob("hits2015/*.fits")
for file in files:
    newfile = os.path.join("hits2015-zeroed", os.path.basename(file))
    data = fits.open(file)
    print("Processing:", file)
    for i, hdu in enumerate(data):
        if isinstance(hdu, fits.ImageHDU) or isinstance(hdu, fits.CompImageHDU):
            hdu.data[:] = i
    print("Blanked Image HDUs...")
    import ipdb; ipdb.set_trace();
    with open(newfile, 'wb') as outfile:
        data.writeto(outfile, overwrite=True)
    print("Wrote file...")
    # fpack the file, using gzip and "-q 0" because it did better than the
    # other options when I did a comparison test.
    subprocess.call(["fpack", "-w", "-g2", "-q", "0", newfile])
