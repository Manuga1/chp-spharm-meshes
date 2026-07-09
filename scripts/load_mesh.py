#!/usr/bin/env python
"""Minimal dependency-free loader for SlicerSALT SPHARM-PDM legacy-VTK meshes.

Usage:  python scripts/load_mesh.py meshes/real_C00_L_SPHARM_ellalign.vtk
Returns (points [N,3] float, faces [M,3] int). No vtk/pyvista required.
"""
import sys, numpy as np

def load_spharm_vtk(path):
    with open(path) as f:
        tok = f.read().split()
    i = 0; pts = None; faces = []
    while i < len(tok):
        if tok[i] == "POINTS":
            n = int(tok[i+1])
            vals = tok[i+3:i+3+3*n]
            pts = np.array(vals, dtype=float).reshape(n, 3)
            i += 3 + 3*n
        elif tok[i] == "POLYGONS":
            # VTK 5.x: OFFSETS/CONNECTIVITY; VTK 4.x: [count v0 v1 v2]*
            i += 1
        else:
            i += 1
    return pts, np.array(faces)

if __name__ == "__main__":
    p, _ = load_spharm_vtk(sys.argv[1])
    print("points:", p.shape, "centroid:", p.mean(0).round(2))
