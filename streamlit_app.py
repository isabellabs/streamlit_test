import streamlit as st
import pandas as pd

Col1, Col2 = st.columns([2, 1])
with Col1:
    st.title("Dataset name")
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
    | Data size            | <ul><li>Total number of images: 88,702</li><li>Diabetic Retinopathy images: 88,702</li><li>Glaucoma images: 24,366</li></ul> |
    | Target disease(s)    | <ul><li>Diabetic retinopathy: severity from 0 (healthy) to 4 (proliferative)</li><li>Glaucoma: referable (glaucomatous) and no referable glaucoma (healthy)</li></ul> |
    | Data annotation      | Human annotation: <ul><li>Diabetic Retinopathy: 0-4</li><li>Glaucoma presence: 0-1</li><li>Subjective quality annotation: 0-2</li></ul> | 
    | Spatial coverage     | <ul><li>USA (patients with different ethnic backgrounds, i.e., African descent, Caucasian, Asian, Latin American and Native American individuals)</li><li>Indian Subcontinent (unspecified regions)</li></ul> |                
    | Limitations          | <ul><li>Great variance in image characteristics, which might hamper model performance or usability.</li><li>Annotation by different specialists might produce inappropriate class label classifications.</li><li>Some images are unusable due to poor acquisition conditions.</li><li>Glaucoma images might not reflect real world scenarios, as images were acquired in the frame of diabetic retinopathy screening programs.</li><li>No additional information of patients’ age, sex, comorbidities or other factors that might influence the diagnosis.</li></ul> |
    | Biases               | <ul><li>Ungradable images were excluded from the final datasets.</li><li>Annotations may be biased because they were annotated and disagreements were resolved by several specialists.</li></ul> | 
    """

    st.markdown(real_dataset, unsafe_allow_html=True)

    st.header("Generative model used", help="The generative model used to create the synthetic data")

    generative_model = """
    | Title                        | SD20 ZSNR |
    |------------------------------|-----------|
    | Description                  | Multipurpose Stable Diffusion model trained on Retinal Fundus Images for Diabetic Retinopathy Grading and Glaucoma Classification. |
    | Generation options available | <ul><li>Disease Intensity (one of):<ul><li>mild/moderate/severe/proliferative diabetic retinopathy</li><li>glaucomatous/healthy</li><li>no diabetic retinopathy</li></ul></li><br><li>Quality Attributes (all):<ul><li>contrast (low/medium/high)</li><li>brightness (dark/medium/bright)</li><li>color (colorless/medium/colorful)</li><li>sharpness (blurred/medium/sharp)</li><li>perceptual quality (low/medium/high)</li></ul></li><br><li>Prompt examples:<ul><li>“retinal fundus image, high contrast, colorful, sharp”</li><li>“moderate diabetic retinopathy retinal fundus image, blurred, bright”</li><li>“glaucomatous retinal fundus image, high perceptual quality, normal”</li></ul></li></ul> |
    | Limitations                  | <ul><li>Some image quality descriptions conflict with each other during training.</li><li>Asking the model to generate images with specific quality characteristics might lead to unwanted behavior.</li><li>Model was trained on a large-scale image dataset which is severely unbalanced.</li><li>Images with high diabetic retinopathy levels may not be realistic.</li><li>Model only accepts English prompts with a fixed structure.</li></ul> |
    | Biases                       | <ul><li>Model is biased to the specifications/models of the machines used to acquire the images.</li><li>Model is biased to the population of the acquired images.</li><li>In some cases, image characteristics may not be aligned with real world scenarios.</li></ul> |
    """

    st.markdown(generative_model, unsafe_allow_html=True)

# -- Medical data representativeness form--
with Col2:
    with st.container(border=True):
        st.header("Medical data representativeness")
        st.write("How representative is the medical data used for the generation purposes?")
        representativesness = st.radio(
            "Medical data representativeness:",
            ["Extremely representative", "Quite representative", "Somewhat representative", "Slightly representative", "Not representative"], label_visibility="collapsed"
        )
        st.text_area("Comments (optional):", placeholder="Add comments here...")
        st.button("Submit", type="primary", use_container_width=True)