#!/bin/env bash

# Script to do the conversion from gen2 to gen3.
# Requires w_2022_28 + DM-34862 of obs_decam (or later weekly after merge).

butler convert repo --gen2root "./rawData" --calibs "./cpCalib" -t relsymlink

# Need to re-certify calibs because default is incorrect.
python $TESTDATA_DECAM_DIR/scripts/decertify_calibs.py

butler certify-calibrations --begin-date 1990-01-01 --end-date 2030-01-01 repo/ DECam/calib/20130901T000000Z DECam/calib cpBias
butler certify-calibrations --begin-date 1990-01-01 --end-date 2030-01-01 repo/ DECam/calib/20130901T000000Z DECam/calib cpFlat
butler certify-calibrations --begin-date 1990-01-01 --end-date 2030-01-01 repo/ DECam/calib/20131115T000000Z DECam/calib fringe

# butler define-visits repo lsst.obs.decam.DarkEnergyCamera
