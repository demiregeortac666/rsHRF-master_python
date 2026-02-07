"""
Visualize comparison between old and new Wiener deconvolution implementations
"""

import numpy as np
import matplotlib.pyplot as plt

# Load results
data = np.load('/private/tmp/claude-501/-Users-ortach-Desktop-Z-Z-Z-rshrf/cfcc1275-67fc-4b6a-a924-be664c51e0da/scratchpad/real_data_test_results.npz')

original = data['original']
hrf = data['hrf']
result_old = data['result_old']
result_new_rest = data['result_new_rest']
result_new_task = data['result_new_task']
result_new_custom = data['result_new_custom']
TR = float(data['TR'])
voxel_coords = data['voxel_coords']

# Time vectors
t_signal = np.arange(len(original)) * TR
t_hrf = np.arange(len(hrf)) * TR

# Create comprehensive visualization
fig = plt.figure(figsize=(16, 12))

# 1. Original signal and HRF
ax1 = plt.subplot(3, 3, 1)
ax1.plot(t_signal, original, 'k-', linewidth=1.5, label='Original BOLD')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Signal Intensity')
ax1.set_title(f'Original BOLD Signal\nVoxel: {voxel_coords}')
ax1.grid(True, alpha=0.3)
ax1.legend()

ax2 = plt.subplot(3, 3, 2)
ax2.plot(t_hrf, hrf, 'r-', linewidth=2, label='Canonical HRF')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
ax2.set_title('Hemodynamic Response Function')
ax2.grid(True, alpha=0.3)
ax2.legend()

# 2. Deconvolution results comparison
ax3 = plt.subplot(3, 3, 3)
ax3.plot(t_signal, result_old, 'b-', linewidth=1.5, alpha=0.7, label='Old Implementation')
ax3.plot(t_signal, result_new_rest, 'r-', linewidth=1.5, alpha=0.7, label='New (Rest mode)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Deconvolved Signal')
ax3.set_title('Old vs New (Rest Mode)')
ax3.grid(True, alpha=0.3)
ax3.legend()

# 3. Zoomed comparison (first 50 seconds)
ax4 = plt.subplot(3, 3, 4)
idx_zoom = int(50 / TR)
ax4.plot(t_signal[:idx_zoom], result_old[:idx_zoom], 'b-', linewidth=2, alpha=0.7, label='Old')
ax4.plot(t_signal[:idx_zoom], result_new_rest[:idx_zoom], 'r--', linewidth=2, alpha=0.7, label='New (Rest)')
ax4.set_xlabel('Time (s)')
ax4.set_ylabel('Deconvolved Signal')
ax4.set_title('Comparison (First 50s)')
ax4.grid(True, alpha=0.3)
ax4.legend()

# 4. Difference between old and new (rest)
ax5 = plt.subplot(3, 3, 5)
diff = result_new_rest - result_old
ax5.plot(t_signal, diff, 'g-', linewidth=1.5)
ax5.axhline(y=0, color='k', linestyle='--', linewidth=1)
ax5.set_xlabel('Time (s)')
ax5.set_ylabel('Difference')
ax5.set_title(f'New-Rest minus Old\n(Mean: {np.mean(diff):.4f}, Std: {np.std(diff):.4f})')
ax5.grid(True, alpha=0.3)

# 5. Mode comparison (Rest vs Task)
ax6 = plt.subplot(3, 3, 6)
ax6.plot(t_signal, result_new_rest, 'r-', linewidth=1.5, alpha=0.7, label='Rest mode')
ax6.plot(t_signal, result_new_task, 'b-', linewidth=1.5, alpha=0.7, label='Task mode')
ax6.set_xlabel('Time (s)')
ax6.set_ylabel('Deconvolved Signal')
ax6.set_title('Mode Comparison')
ax6.grid(True, alpha=0.3)
ax6.legend()

# 6. All new implementations
ax7 = plt.subplot(3, 3, 7)
ax7.plot(t_signal, result_new_rest, 'r-', linewidth=1.5, alpha=0.6, label='Rest')
ax7.plot(t_signal, result_new_task, 'b-', linewidth=1.5, alpha=0.6, label='Task')
ax7.plot(t_signal, result_new_custom, 'g-', linewidth=1.5, alpha=0.6, label='Custom')
ax7.set_xlabel('Time (s)')
ax7.set_ylabel('Deconvolved Signal')
ax7.set_title('All New Implementations')
ax7.grid(True, alpha=0.3)
ax7.legend()

# 7. Correlation scatter plot
ax8 = plt.subplot(3, 3, 8)
ax8.scatter(result_old, result_new_rest, alpha=0.5, s=20)
min_val = min(result_old.min(), result_new_rest.min())
max_val = max(result_old.max(), result_new_rest.max())
ax8.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2)
corr = np.corrcoef(result_old, result_new_rest)[0, 1]
ax8.set_xlabel('Old Implementation')
ax8.set_ylabel('New Implementation (Rest)')
ax8.set_title(f'Correlation Scatter\nr = {corr:.4f}')
ax8.grid(True, alpha=0.3)
ax8.axis('equal')

# 8. Statistical summary
ax9 = plt.subplot(3, 3, 9)
ax9.axis('off')

stats_text = f"""
STATISTICAL SUMMARY

Original Signal:
  Mean: {np.mean(original):.2f}
  Std: {np.std(original):.2f}
  Range: [{original.min():.2f}, {original.max():.2f}]

Old Implementation:
  Mean: {np.mean(result_old):.4f}
  Std: {np.std(result_old):.4f}
  Range: [{result_old.min():.2f}, {result_old.max():.2f}]

New (Rest mode):
  Mean: {np.mean(result_new_rest):.4f}
  Std: {np.std(result_new_rest):.4f}
  Range: [{result_new_rest.min():.2f}, {result_new_rest.max():.2f}]

New (Task mode):
  Mean: {np.mean(result_new_task):.4f}
  Std: {np.std(result_new_task):.4f}

New (Custom):
  Mean: {np.mean(result_new_custom):.4f}
  Std: {np.std(result_new_custom):.4f}

Correlations:
  Old vs New-Rest: {np.corrcoef(result_old, result_new_rest)[0,1]:.4f}
  Rest vs Task: {np.corrcoef(result_new_rest, result_new_task)[0,1]:.4f}
  Rest vs Custom: {np.corrcoef(result_new_rest, result_new_custom)[0,1]:.4f}
"""

ax9.text(0.05, 0.95, stats_text, transform=ax9.transAxes,
         fontsize=9, verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig('/private/tmp/claude-501/-Users-ortach-Desktop-Z-Z-Z-rshrf/cfcc1275-67fc-4b6a-a924-be664c51e0da/scratchpad/real_data_comparison.png',
            dpi=150, bbox_inches='tight')
print("Visualization saved to: real_data_comparison.png")
plt.close()

# Create a second figure focusing on differences
fig2 = plt.figure(figsize=(14, 8))

# Histogram of differences
ax1 = plt.subplot(2, 2, 1)
diff_rest = result_new_rest - result_old
diff_task = result_new_task - result_old
diff_custom = result_new_custom - result_old

ax1.hist(diff_rest, bins=30, alpha=0.5, label='Rest - Old', color='red')
ax1.hist(diff_task, bins=30, alpha=0.5, label='Task - Old', color='blue')
ax1.hist(diff_custom, bins=30, alpha=0.5, label='Custom - Old', color='green')
ax1.axvline(x=0, color='k', linestyle='--', linewidth=2)
ax1.set_xlabel('Difference')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of Differences from Old Implementation')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Time series of differences
ax2 = plt.subplot(2, 2, 2)
ax2.plot(t_signal, diff_rest, 'r-', linewidth=1, alpha=0.7, label='Rest - Old')
ax2.plot(t_signal, diff_task, 'b-', linewidth=1, alpha=0.7, label='Task - Old')
ax2.plot(t_signal, diff_custom, 'g-', linewidth=1, alpha=0.7, label='Custom - Old')
ax2.axhline(y=0, color='k', linestyle='--', linewidth=1)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Difference')
ax2.set_title('Temporal Evolution of Differences')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Power spectrum comparison
ax3 = plt.subplot(2, 2, 3)
freq = np.fft.rfftfreq(len(original), d=TR)
power_old = np.abs(np.fft.rfft(result_old))**2
power_new_rest = np.abs(np.fft.rfft(result_new_rest))**2
power_new_task = np.abs(np.fft.rfft(result_new_task))**2

ax3.semilogy(freq, power_old, 'b-', linewidth=1.5, alpha=0.7, label='Old')
ax3.semilogy(freq, power_new_rest, 'r-', linewidth=1.5, alpha=0.7, label='New (Rest)')
ax3.semilogy(freq, power_new_task, 'g-', linewidth=1.5, alpha=0.7, label='New (Task)')
ax3.axvline(x=0.2, color='r', linestyle='--', linewidth=1, label='Rest LowPass=0.2Hz')
ax3.axvline(x=0.225, color='g', linestyle='--', linewidth=1, label='Task LowPass=0.225Hz')
ax3.set_xlabel('Frequency (Hz)')
ax3.set_ylabel('Power')
ax3.set_title('Power Spectrum Comparison')
ax3.set_xlim([0, 0.25])
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Summary statistics table
ax4 = plt.subplot(2, 2, 4)
ax4.axis('off')

summary_text = f"""
IMPLEMENTATION COMPARISON METRICS

Difference Statistics (New - Old):

Rest Mode:
  Mean difference: {np.mean(diff_rest):.6f}
  Std difference: {np.std(diff_rest):.6f}
  Max abs difference: {np.max(np.abs(diff_rest)):.6f}
  RMSE: {np.sqrt(np.mean(diff_rest**2)):.6f}

Task Mode:
  Mean difference: {np.mean(diff_task):.6f}
  Std difference: {np.std(diff_task):.6f}
  Max abs difference: {np.max(np.abs(diff_task)):.6f}
  RMSE: {np.sqrt(np.mean(diff_task**2)):.6f}

Custom Parameters:
  Mean difference: {np.mean(diff_custom):.6f}
  Std difference: {np.std(diff_custom):.6f}
  Max abs difference: {np.max(np.abs(diff_custom)):.6f}
  RMSE: {np.sqrt(np.mean(diff_custom**2)):.6f}

Relative Changes:
  Old Std: {np.std(result_old):.4f}
  Rest Std: {np.std(result_new_rest):.4f} ({100*(np.std(result_new_rest)/np.std(result_old)-1):.2f}%)
  Task Std: {np.std(result_new_task):.4f} ({100*(np.std(result_new_task)/np.std(result_old)-1):.2f}%)
"""

ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
         fontsize=9, verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

plt.tight_layout()
plt.savefig('/private/tmp/claude-501/-Users-ortach-Desktop-Z-Z-Z-rshrf/cfcc1275-67fc-4b6a-a924-be664c51e0da/scratchpad/real_data_differences.png',
            dpi=150, bbox_inches='tight')
print("Difference analysis saved to: real_data_differences.png")
plt.close()

print("\nVisualization complete!")
