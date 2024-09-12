import numpy as np
import matplotlib.pyplot as plt

def plot_well_profiles(model_1, model_2, x_grid, y_grid, depth_grid, model_1_name='Model 1', model_2_name='Model 2', x_well=50, y_well=50):
    """
    Extracts and plots profiles from two models at the well location with dynamic labels.

    Parameters:
    model_1 (numpy.ndarray): 3D model 1 with shape (len(x_grid), len(y_grid), len(depth_grid)).
    model_2 (numpy.ndarray): 3D model 2 with shape (len(x_grid), len(y_grid), len(depth_grid)).
    x_grid (numpy.ndarray): 1D array of x-axis grid points.
    y_grid (numpy.ndarray): 1D array of y-axis grid points.
    depth_grid (numpy.ndarray): 1D array of depth points.
    model_1_name (str, optional): Name of model 1 to use in the plot labels. Defaults to 'Model 1'.
    model_2_name (str, optional): Name of model 2 to use in the plot labels. Defaults to 'Model 2'.
    x_well (float, optional): x-coordinate of the well location. Defaults to 50.
    y_well (float, optional): y-coordinate of the well location. Defaults to 50.
    """
    
    # Find the nearest indices to the well location
    well_x_index = np.argmin(np.abs(x_grid - x_well))
    well_y_index = np.argmin(np.abs(y_grid - y_well))
    
    # Extract profiles from model_1 and model_2 at the well location
    extracted_profile_1 = model_1[well_x_index, well_y_index, :]
    extracted_profile_2 = model_2[well_x_index, well_y_index, :]
    
    # Plot the profiles
    plt.figure(figsize=(12, 5))
    
    # Model 1 profile
    plt.subplot(1, 2, 1)
    plt.plot(extracted_profile_1, depth_grid, label=f'Extracted from {model_1_name}', color='red', linestyle='--')
    plt.xlabel(f'{model_1_name}')
    plt.ylabel('Depth (m)')
    plt.title(f'{model_1_name} QC at Well Location (X={x_well}, Y={y_well})')
    plt.gca().invert_yaxis()  # Depth increases downwards
    plt.legend()
    plt.grid(True)
    
    # Model 2 profile
    plt.subplot(1, 2, 2)
    plt.plot(extracted_profile_2, depth_grid, label=f'Extracted from {model_2_name}', color='red', linestyle='--')
    plt.xlabel(f'{model_2_name}')
    plt.ylabel('Depth (m)')
    plt.title(f'{model_2_name} QC at Well Location (X={x_well}, Y={y_well})')
    plt.gca().invert_yaxis()  # Depth increases downwards
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Example usage
# plot_well_profiles(model_1, model_2, x_grid, y_grid, depth_grid, model_1_name='Lithology Model', model_2_name='Fluid Model')
