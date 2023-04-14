#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nequip.ase import NequIPCalculator
models = "/mnt/scratch2/users/40247882/pbe-oxides/nq-train/neq-ensemble/model-2/deployed_model.pth"
calc = NequIPCalculator.from_deployed_model(
    model_path=models
)

from ase.build import bulk
atoms = bulk("Pt", "fcc", a=3.6)
atoms.calc = calc
stress = atoms.get_stress()
print(stress)

if __name__ == '__main__':
    pass
