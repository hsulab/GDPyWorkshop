#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nequip.ase import NequIPCalculator
models = "/users/40247882/repository/GDPy/examples/expedition/offline/dynamics/allegro/deployed_model.pth"
calc = NequIPCalculator.from_deployed_model(
    model_path=models
)

from ase.build import bulk
atoms = bulk("Pd", "fcc", a=3.6)
atoms.calc = calc
stress = atoms.get_stress()
print(stress)

if __name__ == '__main__':
    pass
