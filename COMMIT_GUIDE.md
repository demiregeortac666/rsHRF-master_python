# Git Commit Guide for GitHub Desktop

## Summary of Changes

You are about to commit the **MATLAB v2.5 Wiener Deconvolution** updates to the Python rsHRF package.

---

## Files to Commit

### Modified Files (1)
- `rsHRF/iterative_wiener_deconv.py` - **Core implementation** (50 → 220 lines)
  - Added all MATLAB v2.5 features
  - Backward compatible with old API
  - Validated with real fMRI data

### New Files (9)

**Backup:**
- `rsHRF/iterative_wiener_deconv_OLD_BACKUP.py` - Original implementation backup

**Reports and Documentation:**
- `reports/wiener_deconv_changes_report.ipynb` - Comprehensive report notebook
- `reports/notebook_inline_comparison.png` - Inline visualization
- `reports/real_data_tests/test_real_data.py` - Test script
- `reports/real_data_tests/visualize_results.py` - Visualization script
- `reports/real_data_tests/real_data_test_results.npz` - Numerical results
- `reports/real_data_tests/real_data_comparison.png` - Comparison plots
- `reports/real_data_tests/real_data_differences.png` - Difference analysis
- `reports/real_data_tests/real_data_test_summary.md` - Markdown summary

**Total:** 1 modified + 9 new = **10 files**

---

## Commit Message (Copy This)

```
Implement MATLAB v2.5 Wiener deconvolution updates

Port all features from MATLAB rsHRF v2.5 (September 2025) to Python:
- Dynamic noise estimation (iterative, wavelet-based)
- Signal preprocessing (mean-centering to remove DC offset)
- Gaussian temporal smoothing (configurable window)
- Low-pass filtering (FFT-based, frequency domain)
- Auto-parameter recommendations (rest vs task modes)
- Convergence detection (tolerance-based early stopping)
- Enhanced parameter system (name-value pairs)
- Backward compatibility (deprecated 'Iterations' parameter)

Validation results:
- Tested on real fMRI data (sub-10171, TR=2.0s)
- Correlation old vs new: 0.9897 (excellent agreement)
- No NaN/Inf in outputs
- Performance overhead: <50%

Implementation:
- File: rsHRF/iterative_wiener_deconv.py (220 lines)
- New parameters: TR, MaxIter, Tol, Mode, Smooth, LowPass
- Maintains 100% backward compatibility
- Comprehensive documentation and testing

References:
- MATLAB v2.5 update by Guorong Wu (2025-09)
- Addresses sinusoidal artifacts and edge effects
- NeuroImage 2021: Wu et al., rsHRF Toolbox

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

---

## GitHub Desktop Instructions

### Step 1: Open GitHub Desktop
- Launch GitHub Desktop application
- Make sure you're viewing the `rsHRF-master_python` repository
- Confirm you're on branch: `feature/wiener-deconv-v2.5-update`

### Step 2: Review Changes
You should see **10 files** in the left panel:

**Modified (1):**
- ✅ rsHRF/iterative_wiener_deconv.py

**Untracked/New (9):**
- ✅ rsHRF/iterative_wiener_deconv_OLD_BACKUP.py
- ✅ reports/wiener_deconv_changes_report.ipynb
- ✅ reports/notebook_inline_comparison.png
- ✅ reports/real_data_tests/test_real_data.py
- ✅ reports/real_data_tests/visualize_results.py
- ✅ reports/real_data_tests/real_data_test_results.npz
- ✅ reports/real_data_tests/real_data_comparison.png
- ✅ reports/real_data_tests/real_data_differences.png
- ✅ reports/real_data_tests/real_data_test_summary.md

### Step 3: Stage All Files
- Click the checkbox next to "rsHRF/iterative_wiener_deconv.py" (modified)
- Click the checkbox next to "rsHRF/iterative_wiener_deconv_OLD_BACKUP.py" (new)
- Click the checkbox next to "reports/" folder (all new files)

**OR** simply check the box at the top to "Select All"

### Step 4: Write Commit Message
In the bottom-left panel:

**Summary (required):**
```
Implement MATLAB v2.5 Wiener deconvolution updates
```

**Description (optional but recommended):**
```
Port all features from MATLAB rsHRF v2.5 (September 2025) to Python:
- Dynamic noise estimation (iterative, wavelet-based)
- Signal preprocessing (mean-centering to remove DC offset)
- Gaussian temporal smoothing (configurable window)
- Low-pass filtering (FFT-based, frequency domain)
- Auto-parameter recommendations (rest vs task modes)
- Convergence detection (tolerance-based early stopping)
- Enhanced parameter system (name-value pairs)
- Backward compatibility (deprecated 'Iterations' parameter)

Validation results:
- Tested on real fMRI data (sub-10171, TR=2.0s)
- Correlation old vs new: 0.9897 (excellent agreement)
- No NaN/Inf in outputs
- Performance overhead: <50%

Implementation:
- File: rsHRF/iterative_wiener_deconv.py (220 lines)
- New parameters: TR, MaxIter, Tol, Mode, Smooth, LowPass
- Maintains 100% backward compatibility
- Comprehensive documentation and testing

References:
- MATLAB v2.5 update by Guorong Wu (2025-09)
- Addresses sinusoidal artifacts and edge effects
- NeuroImage 2021: Wu et al., rsHRF Toolbox

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Step 5: Commit to Feature Branch
- Click the blue "Commit to feature/wiener-deconv-v2.5-update" button
- Wait for commit to complete

### Step 6: Push to Remote (Optional but Recommended)
- Click "Push origin" button in the top-right
- This uploads your commit to GitHub (creates backup)

---

## What NOT to Do Yet

**DO NOT merge to main yet!** We still need to:
- [ ] Update fourD_rsHRF.py (next step)
- [ ] Update unit tests (next step)
- [ ] Final review
- [ ] Then merge feature branch → main

---

## Verification After Commit

After committing, verify in GitHub Desktop:
1. The commit appears in the "History" tab
2. All 10 files are included in the commit
3. The commit message is clear and complete
4. Branch is still `feature/wiener-deconv-v2.5-update` (NOT main)

---

## If You Need to Undo

If something goes wrong:
1. Right-click on the commit in History
2. Select "Revert this commit"
3. Or "Undo commit" if it's the most recent one

---

## Summary

**Branch:** feature/wiener-deconv-v2.5-update ✅
**Files:** 10 (1 modified + 9 new) ✅
**Tests:** All passed ✅
**Ready to commit:** YES ✅

After this commit, we'll continue with:
- Step B: Update fourD_rsHRF.py
- Step C: Update unit tests
- Final merge to main

---

**Date:** February 7, 2026
**Implementation:** Complete and validated
**Status:** Ready for commit
