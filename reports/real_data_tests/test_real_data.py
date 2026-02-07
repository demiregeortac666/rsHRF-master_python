"""
Test rsHRF iterative Wiener deconvolution with real fMRI data
Compare old vs new implementation (MATLAB v2.5 port)
"""

import sys
sys.path.insert(0, '/Users/ortach/Desktop/Z_Z_Z_rshrf/python/rsHRF-master_python')

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from rsHRF.iterative_wiener_deconv import rsHRF_iterative_wiener_deconv
from rsHRF.canon.canon_hrf2dd import wgr_spm_get_canonhrf
import warnings

warnings.filterwarnings('ignore')

print("="*70)
print("REAL fMRI DATA TEST - Old vs New Implementation")
print("="*70)

# Parameters
TR = 2.0  # From JSON metadata
data_path = '/Users/ortach/Desktop/Z_Z_Z_rshrf/test_data/sub-10171/func/sub-10171_task-rest_bold_space-MNI152NLin2009cAsym_preproc.nii'

# Load real fMRI data
print("\n1. Loading BOLD data...")
try:
    img = nib.load(data_path)
    data = img.get_fdata()
    print(f"   Data shape: {data.shape}")
    print(f"   Data type: {data.dtype}")

    # Extract a voxel with good signal (center of brain, avoid edges)
    # Use middle coordinates to find active voxels
    x, y, z = data.shape[0]//2, data.shape[1]//2, data.shape[2]//2

    # Find voxel with reasonable variance (active brain region)
    best_var = 0
    best_coords = None
    for dx in range(-5, 6):
        for dy in range(-5, 6):
            for dz in range(-5, 6):
                voxel = data[x+dx, y+dy, z+dz, :]
                if np.std(voxel) > best_var and not np.any(np.isnan(voxel)):
                    best_var = np.std(voxel)
                    best_coords = (x+dx, y+dy, z+dz)

    if best_coords is None:
        print("   WARNING: Could not find good voxel, using center")
        best_coords = (x, y, z)

    print(f"   Selected voxel: {best_coords}")
    print(f"   Voxel std: {best_var:.4f}")

    # Extract time series
    y = data[best_coords[0], best_coords[1], best_coords[2], :].flatten()
    print(f"   Time series length: {len(y)} points")
    print(f"   Time series range: [{np.min(y):.2f}, {np.max(y):.2f}]")
    print(f"   Mean: {np.mean(y):.2f}, Std: {np.std(y):.2f}")

except Exception as e:
    print(f"   ERROR loading data: {e}")
    sys.exit(1)

# Generate HRF
print("\n2. Generating HRF...")
try:
    # Use rsHRF's canonical HRF function
    xBF = {
        'dt': TR,
        'T': 16,
        'len': 32,
        'TD_DD': 0
    }
    hrf = wgr_spm_get_canonhrf(xBF)[:, 0]
    print(f"   HRF length: {len(hrf)} points")
    print(f"   HRF range: [{np.min(hrf):.4f}, {np.max(hrf):.4f}]")

except Exception as e:
    print(f"   ERROR generating HRF: {e}")
    sys.exit(1)

# Test OLD implementation (backward compatibility mode)
print("\n3. Testing OLD implementation (no new parameters)...")
try:
    # Old API: just y and h, with Iterations parameter
    y_old = y.copy()
    result_old = rsHRF_iterative_wiener_deconv(y_old, hrf, Iterations=50)

    print(f"   Result shape: {result_old.shape}")
    print(f"   NaN values: {np.any(np.isnan(result_old))}")
    print(f"   Inf values: {np.any(np.isinf(result_old))}")
    print(f"   Range: [{np.min(result_old):.4f}, {np.max(result_old):.4f}]")
    print(f"   Mean: {np.mean(result_old):.4f}, Std: {np.std(result_old):.4f}")

except Exception as e:
    print(f"   ERROR: {e}")
    result_old = None

# Test NEW implementation - Rest mode with auto-recommendations
print("\n4. Testing NEW implementation (Rest mode, auto-recommendations)...")
try:
    y_new = y.copy()
    result_new_rest = rsHRF_iterative_wiener_deconv(
        y_new, hrf,
        TR=TR,
        MaxIter=50,
        Tol=1e-4,
        Mode='rest'
    )

    print(f"   Result shape: {result_new_rest.shape}")
    print(f"   NaN values: {np.any(np.isnan(result_new_rest))}")
    print(f"   Inf values: {np.any(np.isinf(result_new_rest))}")
    print(f"   Range: [{np.min(result_new_rest):.4f}, {np.max(result_new_rest):.4f}]")
    print(f"   Mean: {np.mean(result_new_rest):.4f}, Std: {np.std(result_new_rest):.4f}")

    # Calculate auto-recommended parameters
    fs = 1.0 / TR
    nyquist = fs / 2.0
    smooth_rec = max(int(np.round(4.0 / TR)), 3)
    lowpass_rec = min(0.2, 0.8 * nyquist)
    print(f"   Auto-recommendations: Smooth={smooth_rec}, LowPass={lowpass_rec:.3f} Hz")

except Exception as e:
    print(f"   ERROR: {e}")
    result_new_rest = None

# Test NEW implementation - Task mode
print("\n5. Testing NEW implementation (Task mode)...")
try:
    y_new = y.copy()
    result_new_task = rsHRF_iterative_wiener_deconv(
        y_new, hrf,
        TR=TR,
        MaxIter=50,
        Tol=1e-4,
        Mode='task'
    )

    print(f"   Result shape: {result_new_task.shape}")
    print(f"   NaN values: {np.any(np.isnan(result_new_task))}")
    print(f"   Inf values: {np.any(np.isinf(result_new_task))}")
    print(f"   Range: [{np.min(result_new_task):.4f}, {np.max(result_new_task):.4f}]")
    print(f"   Mean: {np.mean(result_new_task):.4f}, Std: {np.std(result_new_task):.4f}")

    # Calculate auto-recommended parameters
    smooth_rec = max(int(np.round(2.0 / TR)), 2)
    lowpass_rec = min(0.35, 0.9 * nyquist)
    print(f"   Auto-recommendations: Smooth={smooth_rec}, LowPass={lowpass_rec:.3f} Hz")

except Exception as e:
    print(f"   ERROR: {e}")
    result_new_task = None

# Test NEW implementation - Custom parameters
print("\n6. Testing NEW implementation (Custom parameters)...")
try:
    y_new = y.copy()
    result_new_custom = rsHRF_iterative_wiener_deconv(
        y_new, hrf,
        TR=TR,
        MaxIter=100,
        Tol=1e-5,
        Mode='rest',
        Smooth=5,
        LowPass=0.15
    )

    print(f"   Result shape: {result_new_custom.shape}")
    print(f"   NaN values: {np.any(np.isnan(result_new_custom))}")
    print(f"   Inf values: {np.any(np.isinf(result_new_custom))}")
    print(f"   Range: [{np.min(result_new_custom):.4f}, {np.max(result_new_custom):.4f}]")
    print(f"   Mean: {np.mean(result_new_custom):.4f}, Std: {np.std(result_new_custom):.4f}")
    print(f"   Custom parameters: Smooth=5, LowPass=0.15 Hz, MaxIter=100")

except Exception as e:
    print(f"   ERROR: {e}")
    result_new_custom = None

# Comparison
print("\n" + "="*70)
print("COMPARISON SUMMARY")
print("="*70)

if result_old is not None and result_new_rest is not None:
    # Calculate correlation
    corr_old_rest = np.corrcoef(result_old, result_new_rest)[0, 1]
    print(f"\nCorrelation (Old vs New-Rest): {corr_old_rest:.4f}")

    # Calculate differences
    diff_old_rest = result_new_rest - result_old
    print(f"Difference stats (New-Rest - Old):")
    print(f"  Mean diff: {np.mean(diff_old_rest):.6f}")
    print(f"  Std diff: {np.std(diff_old_rest):.6f}")
    print(f"  Max abs diff: {np.max(np.abs(diff_old_rest)):.6f}")

if result_new_rest is not None and result_new_task is not None:
    corr_rest_task = np.corrcoef(result_new_rest, result_new_task)[0, 1]
    print(f"\nCorrelation (New-Rest vs New-Task): {corr_rest_task:.4f}")

if result_new_rest is not None and result_new_custom is not None:
    corr_rest_custom = np.corrcoef(result_new_rest, result_new_custom)[0, 1]
    print(f"Correlation (New-Rest vs New-Custom): {corr_rest_custom:.4f}")

# Save results for visualization
print("\n" + "="*70)
print("Saving results...")
output_file = '/private/tmp/claude-501/-Users-ortach-Desktop-Z-Z-Z-rshrf/cfcc1275-67fc-4b6a-a924-be664c51e0da/scratchpad/real_data_test_results.npz'
np.savez(
    output_file,
    original=y,
    hrf=hrf,
    result_old=result_old if result_old is not None else np.array([]),
    result_new_rest=result_new_rest if result_new_rest is not None else np.array([]),
    result_new_task=result_new_task if result_new_task is not None else np.array([]),
    result_new_custom=result_new_custom if result_new_custom is not None else np.array([]),
    TR=TR,
    voxel_coords=best_coords
)
print(f"Results saved to: {output_file}")

print("\n" + "="*70)
print("TEST COMPLETE")
print("="*70)
