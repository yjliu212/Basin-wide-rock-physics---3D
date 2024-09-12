import matplotlib.pyplot as plt
import numpy as np

def plot_model_sections(model_name, x_grid, y_grid, depth_grid, surface_array, x_well, y_well, name='name', y_index=25, x_index=25):
    """
    Plots inline and crossline sections of a given 3D model.

    Parameters:
    model_name (numpy.ndarray): 3D model (e.g., velocity_model or lithology_model) with shape (len(x_grid), len(y_grid), len(depth_grid)).
    x_grid (numpy.ndarray): 1D array of x-axis grid points.
    y_grid (numpy.ndarray): 1D array of y-axis grid points.
    depth_grid (numpy.ndarray): 1D array of depth points.
    surface_array (numpy.ndarray): 2D array of surface depths with shape (len(x_grid), len(y_grid)).
    x_well (float): x-coordinate of the well location.
    y_well (float): y-coordinate of the well location.
    y_index (int, optional): Index for y position to plot the inline section. Defaults to 25.
    x_index (int, optional): Index for x position to plot the crossline section. Defaults to 25.
    """
    
    plt.figure(figsize=(13, 5))
    
    # Plot inline section (constant y)
    plt.subplot(1, 2, 1)
    plt.contourf(x_grid, depth_grid, model_name[:, y_index, :].T)
    plt.gca().invert_yaxis()
    plt.xlabel('X (m)')
    plt.ylabel('Depth (m)')
    plt.colorbar(label=f'{name}')
    plt.title(f'{name} Model at y={y_grid[y_index]}')
    plt.plot(x_grid, surface_array[:, y_index], '-y', label='Water Bottom')
    plt.axvline(x=x_well, color='white', linestyle='--', linewidth=2, label='Well Location')
    plt.legend()
    
    # Plot crossline section (constant x)
    plt.subplot(1, 2, 2)
    plt.contourf(y_grid, depth_grid, model_name[x_index, :, :].T)
    plt.gca().invert_yaxis()
    plt.xlabel('Y (m)')
    plt.ylabel('Depth (m)')
    plt.colorbar(label=f'{name}')
    plt.title(f'{name} Model at x={x_grid[x_index]}')
    plt.plot(y_grid, surface_array[x_index, :], '-y', label='Water Bottom')
    plt.axvline(x=y_well, color='white', linestyle='--', linewidth=2, label='Well Location')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Example usage
# plot_model_sections(velocity_model, x_grid, y_grid, depth_grid, surface_array, x_well, y_well)
