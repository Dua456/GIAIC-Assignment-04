import streamlit as st
import pandas as pd
from io import BytesIO

# Sample data with additional columns
data = {
    "Test Case ID": [1, 2, 3, 4, 5],
    "Description": [
        "Optimized images to reduce load time",
        "Reduce unused JavaScript",
        "Improve Largest Contentful Paint",
        "Eliminate render-blocking resources",
        "Avoid large layout shifts"
    ],
    "Steps": [
        "Analyze image size in Lighthouse",
        "Analyze JavaScript usage",
        "Analyze LCP and optimize accordingly",
        "Review Lighthouse diagnostics",
        "Check Cumulative Layout Shift metrics"
    ],
    "Expected Results": [
        "Image size < 100KB",
        "Minimal unused JavaScript",
        "LCP under 2.5s",
        "No render-blocking resources",
        "CLS < 0.1"
    ],
    "Actual Results": [
        "Image size = 103KB",
        "Potential savings of 2095 bytes",
        "LCP measured at 3.5s",
        "Savings of 60ms observed",
        "CLS recorded at 0.242"
    ],
    "Status": ["Passed", "Failed", "Passed", "Passed", "Passed"],
    # Additional columns
    "Priority": ["High", "Medium", "High", "Low", "Medium"],
    "Module": ["UI", "Backend", "Performance", "UX", "Layout"],
    "Assigned To": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Environment": ["Production", "Staging", "Production", "Development", "Production"],
    "Created Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
    "Comments": [
        "Review needed for optimization",
        "Bug identified in script",
        "Further testing required",
        "Minor issue observed",
        "All checks passed"
    ]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame in the app
st.write("### Sample Data Preview")
st.dataframe(df)

# -----------------------------
# Convert DataFrame to CSV in Memory
# -----------------------------
csv_data = df.to_csv(index=False)
csv_buffer = BytesIO(csv_data.encode('utf-8'))

# -----------------------------
# Provide a Download Button
# -----------------------------
st.download_button(
    label="Download Sample CSV",
    data=csv_buffer,
    file_name="test_cases.csv",
    mime="text/csv"
)