#!/usr/bin/env python
# Create a gen3 exports.yaml file from an existing gen3 decam repo.

import lsst.daf.butler as dafButler
import os.path


butler = dafButler.Butler(os.path.expandvars('$TESTDATA_DECAM_DIR/repo/butler.yaml'), instrument="DECam")


with butler.export(filename="repo/exports.yaml") as export:
    # Raw data
    export.saveDatasets(butler.registry.queryDatasets(collections="DECam/raw/all",
                                                      datasetType="raw"))
    # Calibrations
    for calib in ['camera', 'cpBias', 'cpFlat', 'fringe', 'defects', 'crosstalk', 'linearizer']:
        export.saveDatasets(butler.registry.queryDatasets(calib, collections=...))

    # export.saveDatasets(butler.registry.queryDatasets('camera', collections=...))
    # export.saveDatasets(butler.registry.queryDatasets('cpBias', collections=...))
    # export.saveDatasets(butler.registry.queryDatasets('cpFlat', collections=...))
    # export.saveDatasets(butler.registry.queryDatasets('fringe', collections=...))
    # export.saveDatasets(butler.registry.queryDatasets('defects', collections=...))
    # export.saveDatasets(butler.registry.queryDatasets('crosstalk', collections=...))
    # export.saveDatasets(butler.registry.queryDatasets('linearizer', collections=...))

    # Collections
    export.saveCollection('DECam/raw/all')
    export.saveCollection('DECam/calib')
    export.saveCollection('skymaps')

    # Dimension data
    for name in butler.registry.dimensions.getStaticElements():
        if str(name).startswith('visit'):
            records = butler.registry.queryDimensionRecords(visit_dim)
            export.saveDimensionData(visit_dim, records)
