import streamlit as st
import pandas as pd

st.title("Testing")
st.write("Get to know the generation base: Generation purpose, Medical data used, Generative model used.")
st.warning('Limitations in the medical dataset used for generation may be reflected in the generated data, resulting in underrepresentation, bias and shortcomings cases.', icon=":material/warning:", width="stretch")

st.header("Generation purpose", help="The reason the synthetic data was generated")

purpose = """
| Purpose                                                     |
|--------------------------------------------------------------|
| To evaluate the generative ability of the model              |
| To balance the presence of diabetic retinopathy levels and/or glaucoma diseases in other datasets |
| To produce images with different characteristics (e.g. high contrast, blurred, colorful, etc.) to test the robustness of classification models. |
"""

st.markdown(purpose, unsafe_allow_html=True)

st.header("Medical data used", help="The real medical data used to train the generative model")

real_dataset = """
| Title                | Retina Fundus Data |
|----------------------|--------------------|
| Description          | Compilation of two publicly available retina fundus photography datasets EyePACS and EyePACS AIRGOS. Each image has an associated text prompt indicating the presence or the lack of a disease. Additional quality indications are provided for each instance. |
| Data acquisition     | Retina Fundus photography |
| Target disease(s)    | - Diabetic retinopathy: severity from 0 (healthy) to 4 (proliferative); <br> - Glaucoma: referable (glaucomatous) and no referable glaucoma (healthy) |
| Data annotation      | Human annotation: <br> - Diabetic Retinopathy: 0-4 <br> - Glaucoma presence: 0-1 <br> - Subjective quality annotation: 0-2| 
| Spatial coverage     | - USA (patients with different ethnic backgrounds, i.e., African descent,Caucasian, Asian, Latin American and Native American individuals <br> - Indian Subcontinent (unspecified regions) |                
| Limitations          | - Great variance in image characteristics, which might hamper modelperformance or usability. <br> - Annotation by different specialists might produce inappropriate classlabel classifications. <br> - Some images are unusable due to poor acquisition conditions. <br>  - Glaucoma images might not reflect real world scenarios, as imageswere acquired in the frame of diabetic retinopathy screeningprograms. <br> - No additional information of patients’ age, sex, comorbidities or otherfactors that might influence the diagnosis. |
| Biases               | - Ungradable images were excluded from the final datasets. <br>  - Annotations may be biased because they were annotated and disagreements were resolved by several specialists.| 
"""

st.markdown(real_dataset, unsafe_allow_html=True)

st.header("Generative model used", help="The generative model used to create the synthetic data")

generative_model = """
| Title                        | SD20 ZSNR|
|------------------------------|--------------------|
| Description                  | Multipurpose Stable Diffusion model trained on Retinal Fundus Images for Diabetic Retinopathy Grading and Glaucoma Classification. |
| Generation options available | Disease Intensity (one of): <br> - mild/moderate/severe/proliferative diabetic retinopathy <br> - glaucomatous/healthy <br> - no diabetic retinopathy <br> <br> Quality Attributes (one or more of): <br> - contrast (low/medium/high) <br> - brightness (dark/medium/bright) <br> - color (colorless/medium/colorful) <br> - sharpness (blurred/medium/sharp) <br> - perceptual quality (low/medium/high) <br> Following are some examples of prompts used in the generation: “retinal fundus image, high contrast, colorful, sharp” “moderate diabetic retinopathy retinal fundus image, blurred, bright” “glaucomatous retinal fundus image, high perceptual quality, normal|
| Limitations                  | - Some image quality descriptions conflict with each other during training. <br> - Asking the model to generate images with specific qualitycharacteristics might lead to unwanted behavior. <br> - Model was trained on a large-scale image dataset which is severely unbalanced. <br> - Images with high diabetic retinopathy levels may not be realistic. <br> - Model only accepts English prompts with a fixed structure.|
| Biases                       | - Model is biased to the specifications/models of the machines used to acquire the images. <br> - Model is biased to the population of the acquired images. <br> - In some cases, image characteristics may not be aligned with real world scenarios. |
"""

st.markdown(generative_model, unsafe_allow_html=True)