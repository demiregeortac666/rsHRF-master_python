# Git Commit Guide - Unit Tests Update

## Summary

Comprehensive unit test suite for MATLAB v2.5 Wiener deconvolution features.

---

## Files to Commit

### Modified Files (1)
- `rsHRF/unit_tests/test_iterative_wiener_deconv.py` - Updated with 23 comprehensive tests
  - Expanded from 1 test to 23 tests
  - Added 15 lines → 422 lines
  - All tests passing ✅

**Total:** 1 modified file

---

## Commit Message (Copy This)

```
Add comprehensive unit tests for v2.5 deconvolution

Expand unit test suite from 1 test to 23 comprehensive tests covering all
MATLAB v2.5 features and edge cases.

Test Categories:
1. Backward Compatibility (2 tests)
   - Original API still works
   - Deprecated Iterations parameter with warning

2. New API Features (11 tests)
   - TR parameter and auto-recommendations
   - Rest mode vs Task mode
   - Custom parameters (Smooth, LowPass)
   - Convergence detection
   - Different TR values (0.72s to 3.0s)
   - Mode case-insensitivity
   - Invalid mode error handling
   - Defaults when TR not provided

3. Edge Cases and Robustness (6 tests)
   - Short signals (20 points)
   - Long signals (500 points)
   - HRF longer than signal
   - Zero HRF
   - Signal with NaN values
   - Consistent output shapes

4. Regression Tests (1 test)
   - Consistency between old and new API

5. Parameter Validation (2 tests)
   - MaxIter parameter
   - Tolerance parameter

6. Feature-Specific Tests (3 tests)
   - Mean-centering with DC offset
   - 2D input handling
   - Output is real-valued

Test Results:
- 23/23 tests PASSED ✅
- Execution time: ~2 seconds
- 2 expected warnings (NaN handling test)

Coverage:
- All new parameters tested
- All modes tested (rest/task)
- Edge cases covered
- Backward compatibility verified

```

---

## Test Summary

### Tests Added

**Original (15 lines):**
```python
def test_rsHRF_iterative_wiener_deconv():
    # Basic validation test
```

**New (422 lines, 23 tests):**
1. `test_rsHRF_iterative_wiener_deconv` - Backward compatibility
2. `test_deprecated_iterations_parameter` - Deprecation warning
3. `test_new_api_with_tr` - TR parameter
4. `test_rest_mode` - Rest mode auto-recommendations
5. `test_task_mode` - Task mode auto-recommendations
6. `test_custom_parameters` - Custom Smooth/LowPass
7. `test_convergence_detection` - Early stopping
8. `test_different_tr_values` - Multiple TR values
9. `test_mode_case_insensitive` - Case handling
10. `test_invalid_mode` - Error validation
11. `test_no_tr_defaults` - Default behavior
12. `test_short_signals` - 20-point signals
13. `test_long_signals` - 500-point signals
14. `test_hrf_longer_than_signal` - HRF truncation
15. `test_zero_hrf` - Edge case handling
16. `test_signal_with_nan` - NaN robustness
17. `test_consistent_output_shape` - Shape validation
18. `test_consistency_old_vs_new_api` - Regression test
19. `test_maxiter_validation` - MaxIter parameter
20. `test_tolerance_parameter` - Tol parameter
21. `test_mean_centering` - DC offset handling
22. `test_2d_input_handling` - Array flattening
23. `test_output_is_real` - Real-valued output

---

## GitHub Desktop Instructions

### Step 1: Open GitHub Desktop
- Repository: `rsHRF-master_python`
- Branch: `feature/wiener-deconv-v2.5-update` ✅

### Step 2: Review Changes
You should see **1 file**:

**Modified:**
- ✅ rsHRF/unit_tests/test_iterative_wiener_deconv.py (+407 lines)

### Step 3: Stage File
- Check the box to select the file

### Step 4: Commit Message

**Summary:**
```
Add comprehensive unit tests for v2.5 deconvolution
```

**Description:**
```
Expand unit test suite from 1 test to 23 comprehensive tests covering all
MATLAB v2.5 features and edge cases.

Test Categories:
1. Backward Compatibility (2 tests)
   - Original API still works
   - Deprecated Iterations parameter with warning

2. New API Features (11 tests)
   - TR parameter and auto-recommendations
   - Rest mode vs Task mode
   - Custom parameters (Smooth, LowPass)
   - Convergence detection
   - Different TR values (0.72s to 3.0s)
   - Mode case-insensitivity
   - Invalid mode error handling
   - Defaults when TR not provided

3. Edge Cases and Robustness (6 tests)
   - Short signals (20 points)
   - Long signals (500 points)
   - HRF longer than signal
   - Zero HRF
   - Signal with NaN values
   - Consistent output shapes

4. Regression Tests (1 test)
   - Consistency between old and new API

5. Parameter Validation (2 tests)
   - MaxIter parameter
   - Tolerance parameter

6. Feature-Specific Tests (3 tests)
   - Mean-centering with DC offset
   - 2D input handling
   - Output is real-valued

Test Results:
- 23/23 tests PASSED ✅
- Execution time: ~2 seconds
- 2 expected warnings (NaN handling test)

Coverage:
- All new parameters tested
- All modes tested (rest/task)
- Edge cases covered
- Backward compatibility verified

```

### Step 5: Commit
- Click "Commit to feature/wiener-deconv-v2.5-update"

### Step 6: Push (Optional)
- Click "Push origin" to backup to GitHub

---

## Test Execution Results

```
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.4.2
collected 23 items

rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_rsHRF_iterative_wiener_deconv PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_deprecated_iterations_parameter PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_new_api_with_tr PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_rest_mode PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_task_mode PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_custom_parameters PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_convergence_detection PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_different_tr_values PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_mode_case_insensitive PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_invalid_mode PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_no_tr_defaults PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_short_signals PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_long_signals PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_hrf_longer_than_signal PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_zero_hrf PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_signal_with_nan PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_consistent_output_shape PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_consistency_old_vs_new_api PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_maxiter_validation PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_tolerance_parameter PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_mean_centering PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_2d_input_handling PASSED
rsHRF/unit_tests/test_iterative_wiener_deconv.py::test_output_is_real PASSED

======================== 23 passed, 2 warnings in 1.95s ========================
```

---

## Verification

After committing, verify:
1. Commit appears in History tab
2. File included in commit
3. Still on feature branch (not main)

---

## Next Steps

After this commit:
- ✅ All implementation complete
- ✅ All tests passing
- ⏭️ Ready to merge feature branch to main

---

**Date:** February 7, 2026
**Files:** 1 modified (+407 lines)
**Tests:** 23/23 PASSED ✅
**Status:** Ready to commit
