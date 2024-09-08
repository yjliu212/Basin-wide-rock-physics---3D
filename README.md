# Basin-wide-rock-physics---3D



This Jupyter notebook extends the Rock Physics Template (RPT) calculation from 1D to 3D.

Description:

In this notebook, we create a small 3D model grid filled with a rock physics template (RPT) for both shale and sand. The model includes a sand body containing gas and oil, with distinct gas-oil-contact (GOC) and oil-water-contact (OWC) visible within the sand body.

We first use Dutta’s model to calculate the 3D RPT for shale as a function of various pore pressure gradients, ranging from hydrostatic conditions (9 ppg) to 17 ppg. These calculations form the background velocity model for the shale.

Next, we apply the Raymer-Hunt-Gardner (RHG) model to compute the 3D sand properties, varying the clay volume (Vclay) from 0% to 100%, with the pore fluid initially saturated with water. Then, using Gassmann’s equation for fluid substitution, we replace the pore fluid with gas and oil and apply these changes to the sand body.

Finally, the 3D rock properties such as Vp (P-wave velocity), Ip (Acoustic Impedance), Pr (Poisson's Ratio), and Density are computed, reflecting the characteristics of the sand body and its fluid content.

