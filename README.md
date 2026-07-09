# Choroid Plexus SPHARM-PDM Meshes

Spherical-harmonic (SPHARM-PDM) surface meshes of the **choroid plexus (ChP)**,
produced with **SlicerSALT 6.0.0** and released as an open reference for shape
morphometry of this structure.

Part of the Darby Lab (Vanderbilt) study of choroid-plexus shape and volume in
behavioral-variant frontotemporal dementia (bvFTD), Alzheimer's disease / aMCI,
and healthy aging, and its relationship to sleep and glymphatic function.

## What's here

| File | Description |
|---|---|
| `meshes/real_C00_L_SPHARM_ellalign.vtk` | Left ChP, subject C00, SPHARM ellipsoid-aligned surface |
| `meshes/real_C01_L_SPHARM_ellalign.vtk` | Left ChP, subject C01, SPHARM ellipsoid-aligned surface |
| `figures/real_spharm_meshes.png` | Rendering of the two meshes + a point-wise displacement map |

Each mesh has **1002 corresponded vertices** and **2000 triangular faces**.
Because the parameterization is spherical-harmonic, **vertex _i_ denotes the same
anatomical location across every mesh** — so vertex-wise statistics (displacement,
group contrasts) can be computed directly, with no additional registration.

Generated at **SPHARM degree 15, subdivision level 10** (the standard SlicerSALT
SPHARM-PDM setting that yields 1002 points). The `_ellalign` meshes are aligned
to the first-order ellipsoid, the recommended input for population shape analysis.

> **Note on these specific meshes.** These are technical-validation surfaces from
> synthetic/phantom ChP masks used to verify the pipeline end-to-end; they are
> **not** patient anatomy and carry no PHI. They demonstrate the mesh format,
> resolution, and correspondence that the study pipeline produces. Patient-derived
> meshes are held privately under IRB #180185.

## Reading a mesh

VTK legacy PolyData (ASCII). Any of:

```python
# PyVista
import pyvista as pv
m = pv.read("meshes/real_C00_L_SPHARM_ellalign.vtk")
print(m.n_points, m.n_cells)          # 1002 2000
pts = m.points                        # (1002, 3) — vertex i is corresponded

# VTK
import vtk
r = vtk.vtkPolyDataReader(); r.SetFileName("meshes/real_C00_L_SPHARM_ellalign.vtk"); r.Update()
poly = r.GetOutput()

# nibabel-free numpy: parse POINTS block directly (see scripts/load_mesh.py)
```

## How they were made

Binary ChP label -> topology repair (genus-0) -> binarize -> SlicerSALT
SPHARM-PDM (`SegPostProcess` -> `GenParaMesh` -> `ParaToSPHARMMesh`) run headless:

```
SlicerSALT --no-splash --no-main-window --python-script SPHARM-PDM.py params.ini
```

The full retargetable pipeline (segmentation, topology repair, pre-SPHARM
alignment, SPHARM driver, and vertex-wise shape statistics) lives in the study
repository. It is adapted from **`kedar-codes/hippo_morph`** (GPL-3.0) and
retargeted from the hippocampus to the choroid plexus.

## Method references

- Styner et al. (2006), *Framework for the Statistical Shape Analysis of Brain
  Structures using SPHARM-PDM.* Insight Journal.
- SlicerSALT — https://salt.slicer.org

## License

- **Meshes and figures** (`meshes/`, `figures/`): CC BY 4.0.
- **Code** (`scripts/`): GPL-3.0, inherited from `hippo_morph`.
