#!/bin/env python

import lsst.daf.butler as dafButler


butler = dafButler.Butler('repo', instrument='DECam', writeable=True)

butler.registry.decertify('DECam/calib', 'cpBias', dafButler.Timespan(None, None))
butler.registry.decertify('DECam/calib', 'cpFlat', dafButler.Timespan(None, None))
butler.registry.decertify('DECam/calib', 'fringe', dafButler.Timespan(None, None))
