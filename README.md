# Basin-wide-rock-physics---3D



This Jupyter notebook extends the Rock Physics Template (RPT) calculation from 1D to 3D.

Description:

In this notebook, we create a small 3D model grid filled with a rock physics template (RPT) for both shale and sand. The model includes a sand body containing gas and oil, with distinct gas-oil-contact (GOC) and oil-water-contact (OWC) visible within the sand body.

We first use Dutta’s model to calculate the 3D RPT for shale as a function of various pore pressure gradients, ranging from hydrostatic conditions (9 ppg) to 17 ppg. These calculations form the background velocity model for the shale.

Next, we apply the Raymer-Hunt-Gardner (RHG) model to compute the 3D sand properties, varying the clay volume (Vclay) from 0% to 100%, with the pore fluid initially saturated with water. Then, using Gassmann’s equation for fluid substitution, we replace the pore fluid with gas and oil and apply these changes to the sand body.

Finally, the 3D rock properties such as Vp (P-wave velocity), Ip (Acoustic Impedance), Pr (Poisson's Ratio), and Density are computed, reflecting the characteristics of the sand body and its fluid content.

The figures below show the 3D lithology and fluid model and the extracted profiles at the well location.
![image](https://github.com/user-attachments/assets/9d727591-084e-4577-865f-e28041ce7b84)
![image](https://github.com/user-attachments/assets/9f4f7df9-10ae-4fd2-8a7f-1ffb2ab4115d)
![image](https://github.com/user-attachments/assets/0ae3e22c-8ab4-4921-ad44-903f06a864e3)

The figures below show the hydrostatic velocity model and 12 ppg velocity model in 3D and the extracted velocity profiles from the 3D RPT ranging from hydrostatic, 9 ppg to 17 ppg.
![image](https://github.com/user-attachments/assets/c1f692a8-9018-428b-be94-7780bd833d57)
![image](https://github.com/user-attachments/assets/93108398-cf2e-4c7a-9263-7e45d64d469b)
![image](https://github.com/user-attachments/assets/54a18499-7a47-4b87-acde-694f75db9f9e)

The figures below show the Vp and Density models with sand body saturated by gas and oil.
![image](https://github.com/user-attachments/assets/bcd50b9f-28ab-467a-809d-ccc5c4d92af1)
![image](https://github.com/user-attachments/assets/411dfeeb-3d3a-4fbb-a1c2-3bb260f42847)

The figures below show the extracted Ip and Pr at well location.
![image](https://github.com/user-attachments/assets/d45042b3-fc8f-48b6-9781-7fb2ba8cc3ec)
![image](https://github.com/user-attachments/assets/9eea8e35-5651-4fad-933a-eca73a9baa90)
