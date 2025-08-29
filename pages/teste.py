import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Problem Logger", layout="centered")

# ---- Config ----
ISSUES = [
    "Unrealistic morphological features",
    "Unrealistic pathological findings",
    "Inadequate image quality characteristics",
    "Does not match assigned diagnosis",
    "Edge cases under-represented",
    "Low diversity",
    "Other",
]

# Example image IDs; replace with yours
IMAGE_IDS = ["image #1", "image #2", "image #3"]

# ---- State ----
if "records" not in st.session_state:
    st.session_state.records = []

st.title("Register problems")

with st.form("issue_form", clear_on_submit=True):
    img_id = st.selectbox("Image", IMAGE_IDS)
    picked = st.multiselect("Problems found", ISSUES)

    other_note = ""
    if "Other" in picked:
        other_note = st.text_area("Describe 'Other'")

    notes = st.text_area("Notes (optional)")

    submitted = st.form_submit_button("Save")
    if submitted:
        st.session_state.records.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "image": img_id,
            "issues": ", ".join(picked) if picked else "(none)",
            "other_details": other_note.strip(),
            "notes": notes.strip(),
        })
        st.success("Saved!")

st.subheader("Logged entries")
if st.session_state.records:
    st.dataframe(st.session_state.records, use_container_width=True)
else:
    st.caption("No entries yet.")

# ---- Optional: export buttons ----
import pandas as pd
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    st.download_button(
        "Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="problem_log.csv",
        mime="text/csv",
    )

    