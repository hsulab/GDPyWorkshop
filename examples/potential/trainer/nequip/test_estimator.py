#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GDPy.potential.managers.nequip import NequipManager

# - test uncertainty estimator
trainer_params = dict(
    size = 4
)
calc_params = dict(
    backend="lammps",
    command="lmp_cat -in in.lammps 2>&1 > lmp.out"
)
potter = NequipManager()
potter.register_calculator(calc_params)
potter.register_trainer(trainer_params)
potter.freeze(
    train_dir="/mnt/scratch2/users/40247882/ZnCuOx/PtWater/nequip/nequip-gpu/aqueous/s22w/init/t0"
)
print(potter._estimator.directory)

from ase.io import read, write
frames = read("/mnt/scratch2/users/40247882/ZnCuOx/PtWater/nequip/nequip-gpu/init-data.xyz", ":4")

new_frames = potter._estimator.estimate(frames)
for atoms in new_frames:
    print(atoms.info["max_devi_f"])


if __name__ == "__main__":
    pass
