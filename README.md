# Basin-wide-rock-physics---3D



This Jupyter notebook extends the Rock Physics Template (RPT) calculation from 1D to 3D: [RPT_3D_2.ipynb](/RPT_3D_2.ipynb)

Description:

In this notebook, we build a 3D model grid populated with a rock physics template (RPT) for both shale and sand. The model includes a sand body containing gas and oil, with clearly defined gas-oil-contact (GOC) and oil-water-contact (OWC) within the sand body.

First, we utilize Dutta’s model to compute the 3D RPT for shale based on varying pore pressure gradients, from hydrostatic conditions (8.6 ppg) up to 17 ppg. This creates the background velocity model for the shale.

Next, we use the Raymer-Hunt-Gardner (RHG) model to calculate the 3D sand properties, varying the clay volume (Vclay) between 0% and 100%, with the pore fluid initially saturated with water. We then apply Gassmann’s equation for fluid substitution to replace the pore fluid with gas and oil, applying these changes to the sand body.

Finally, we compute the 3D rock properties such as Vp (P-wave velocity), Ip (Acoustic Impedance), Pr (Poisson's Ratio), and Density, capturing the characteristics of the sand body and its fluid content.

The figures below present the 3D lithology and fluid model, along with extracted profiles at the well location. Here, lithology = 1 represents sand, lithology = 0 represents shale, fluid = 2 represents gas, fluid = 1 represents oil, and fluid = 0 represents water.
![image](https://github.com/user-attachments/assets/9d727591-084e-4577-865f-e28041ce7b84)
![image](https://github.com/user-attachments/assets/9f4f7df9-10ae-4fd2-8a7f-1ffb2ab4115d)
![image](https://github.com/user-attachments/assets/0ae3e22c-8ab4-4921-ad44-903f06a864e3)

The figures below display the 3D hydrostatic velocity model and the 12 ppg velocity model, along with the extracted velocity profiles from the 3D RPT, covering a range from hydrostatic conditions to 9 ppg and up to 17 ppg.
![image](https://github.com/user-attachments/assets/c1f692a8-9018-428b-be94-7780bd833d57)
![image](https://github.com/user-attachments/assets/93108398-cf2e-4c7a-9263-7e45d64d469b)
![image](https://github.com/user-attachments/assets/54a18499-7a47-4b87-acde-694f75db9f9e)

The figures below illustrate the Vp and Density models, with the sand body saturated by gas and oil.
![image](https://github.com/user-attachments/assets/bcd50b9f-28ab-467a-809d-ccc5c4d92af1)
![image](https://github.com/user-attachments/assets/411dfeeb-3d3a-4fbb-a1c2-3bb260f42847)

The figures below show the extracted Ip and Pr at the well location. The Pr anomaly in the gas and oil-saturated zone is apparent.
![image](https://github.com/user-attachments/assets/d45042b3-fc8f-48b6-9781-7fb2ba8cc3ec)
![image](https://github.com/user-attachments/assets/9eea8e35-5651-4fad-933a-eca73a9baa90)

Depending on the shale index (controlled by ppg) and the sand index (controlled by Vclay), the resulting rock properties will vary, leading to different AVO responses.

Below are examples of different combinations of ppg and Vclay indices:

1. ppg_index = 1, Vclay_index = 2: This indicates a pore pressure gradient of 9 ppg and a Vclay of 20%. The resulting AVO response is shown below, displaying a Class III AVO anomaly due to the low Ip and low Pr at the top of the gas sand.
![image](https://github.com/user-attachments/assets/601e8f99-8780-42d2-a67d-19d52ac0111d)
2. ppg_index = 0, Vclay_index = 1: This represents a hydrostatic pore pressure gradient and a Vclay of 10%. In this scenario, the AVO anomaly remains Class III due to the lower Ip and Pr at the top of the gas sand.
![image](https://github.com/user-attachments/assets/f125559e-5034-4f4e-a940-cbaf6e3235d4)
3. ppg_index = 0, Vclay_index = 0: This indicates a hydrostatic pore pressure gradient with a Vclay of 0%. In this case, a Class II AVO anomaly (polarity reversal) appears due to the higher Ip at the top of the gas sand. The Pr remains low at the gas sand top, showing a strong Pr anomaly.
![image](https://github.com/user-attachments/assets/c8238254-7af0-4f78-a222-4e493867c4b0)

As the ppg_index increases, the shale Ip decreases, which can cause the AVO anomaly to shift towards Class I.

Additional modeling scenarios to consider include:

What happens if gas at the top of the reservoir is replaced by oil or water?
Do flat spots due to the oil-water contact (OWC) or gas-oil contact (GOC) always exist?
The stack often shows a flat spot resulting from the gas-oil contact or the oil-water contact:
![image](https://github.com/user-attachments/assets/01d72c7b-8bc7-4d02-8a7c-c46c45954ccc)
