# Basin-wide-rock-physics---3D



This Jupyter notebook extends the Rock Physics Template (RPT) calculation from 1D to 3D: [RPT_3D_2.ipynb](/RPT_3D_2.ipynb)

Description:

In this notebook, we create a small 3D model grid filled with a rock physics template (RPT) for both shale and sand. The model includes a sand body containing gas and oil, with distinct gas-oil-contact (GOC) and oil-water-contact (OWC) visible within the sand body.

We first use Dutta’s model to calculate the 3D RPT for shale as a function of various pore pressure gradients, ranging from hydrostatic conditions (8.6 ppg) and 9 ppg to 17 ppg. These calculations form the background velocity model for the shale.

Next, we apply the Raymer-Hunt-Gardner (RHG) model to compute the 3D sand properties, varying the clay volume (Vclay) from 0% to 100%, with the pore fluid initially saturated with water. Then, using Gassmann’s equation for fluid substitution, we replace the pore fluid with gas and oil and apply these changes to the sand body.

Finally, the 3D rock properties such as Vp (P-wave velocity), Ip (Acoustic Impedance), Pr (Poisson's Ratio), and Density are computed, reflecting the characteristics of the sand body and its fluid content.

The figures below show the 3D lithology and fluid model and the extracted profiles at the well location. Here lithology = 1 represents sand, and lithology = 0 represents shale, and fluid = 2 represents gas, fluid = 1 represents oil and fluid = 0 represents water.

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

The figures below show the extracted Ip and Pr at well location. The Pr anoamly for gas and oil saturated zone is apperant.
![image](https://github.com/user-attachments/assets/d45042b3-fc8f-48b6-9781-7fb2ba8cc3ec)
![image](https://github.com/user-attachments/assets/9eea8e35-5651-4fad-933a-eca73a9baa90)

Depends on the shale index (controled by ppg) and sand index (controled by vclay), the resulting rock properties will be different and lead to different AVO response.

Below we show a few example of different combinations of ppg and vclay index.

1. ppg_index = 1, vclay_index = 2: meaning pore pressure gradient is 9 ppg, and vclay = 20%
The resulting AVO response is shown as below: A class III AVO anomaly due to low Ip and low Pr at gas sand top.
![image](https://github.com/user-attachments/assets/274247f5-8f50-494a-b0d2-2219c7ba0d74)
2. ppg_index = 0, vclay_index = 0: meaning pore pressure gradient is hydrostatic, and vclay = 0%
The resulting AVO response is shown as below: A class II AVO anomaly due to high IP and low Pr at gas sand top.
![image](https://github.com/user-attachments/assets/c8238254-7af0-4f78-a222-4e493867c4b0)
3. ppg_index = 0, vclay_index = 1: meaning pore pressure gradient is hydrostatic, and vclay = 10%
In this case, the AVO anomaly goes back to class III due to lower Ip and low Pr at gas sand top.
![image](https://github.com/user-attachments/assets/f125559e-5034-4f4e-a940-cbaf6e3235d4)

The stack usually contains a flat spot due to the gas-oil-contact or the oil-water-contact:
![image](https://github.com/user-attachments/assets/01d72c7b-8bc7-4d02-8a7c-c46c45954ccc)
