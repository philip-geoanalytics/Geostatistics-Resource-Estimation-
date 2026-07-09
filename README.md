Geostatistical Resource Estimation and Block Modelling Using Python

Overview

This project demonstrates a complete geostatistical workflow for estimating gold grades within a hypothetical mineral deposit using Python. The workflow follows industry-standard resource estimation practices by analyzing drillhole assay data, modelling spatial continuity through variogram analysis, and applying Ordinary Kriging to estimate grades within a block model.

Objectives

- Import and preprocess drillhole assay data.
- Perform exploratory data analysis (EDA).
- Visualize the spatial distribution of gold grades.
- Calculate and model experimental variograms.
- Estimate block grades using Ordinary Kriging.
- Generate a block model and grade distribution maps.
- Calculate mineral resources, including tonnage, average grade, and contained gold.
- Classify resources based on estimation confidence.

Workflow

1. Import and clean drillhole assay data.
2. Perform exploratory data analysis.
3. Visualize drillhole locations in 3D.
4. Model spatial continuity using variograms.
5. Create a block model.
6. Estimate grades using Ordinary Kriging.
7. Generate grade contour maps.
8. Calculate tonnage, average grade, and contained gold.
9. Classify resources into Measured, Indicated, and Inferred categories.

Key Features

- Exploratory Data Analysis (EDA)
- 3D Drillhole Visualization
- Experimental Variogram Modelling
- Ordinary Kriging Interpolation
- Block Model Generation
- Resource Estimation
- Resource Classification
- Grade Contour Mapping

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- PyKrige
- SciKit-GStat

Project Structure

Geostatistical_Resource_Estimation/
│
├── data/
│   └── drillholes.csv
├── outputs/
│   ├── dashboard.png
│   ├── variogram.png
│   ├── grade_map.png
│   └── block_model.csv
├── src/
│   ├── data_processing.py
│   ├── variogram.py
│   ├── kriging.py
│   └── resource_calculation.py
├── main.py
├── requirements.txt
└── README.md

Sample Outputs

- Gold grade distribution histogram
- 3D drillhole visualization
- Experimental variogram with fitted model
- Ordinary Kriging grade estimation map
- Resource estimation summary
- Resource classification results
  <img width="1366" height="705" alt="Resource Estimation Workflow" src="https://github.com/user-attachments/assets/0b34e3c2-6a6c-41ef-814d-5625591d05f0" />


Skills Demonstrated

- Geostatistics
- Mineral Resource Estimation
- Mining Geology
- Spatial Data Analysis
- Python Programming
- Scientific Computing
- Data Visualization

Future Improvements

- Support for multiple variogram models (Spherical, Exponential, Gaussian)
- Cross-validation of kriging estimates
- Directional variogram analysis for anisotropy
- 3D block model visualization using PyVista
- Interactive dashboards with Plotly
- Automated resource reporting

Author

Philip Oppong Frimpong

Geological Engineering | Geostatistics | Mining Geology | Python | GIS | Mineral Resource Estimation

---

Disclaimer: This project is intended for educational and portfolio purposes and uses a hypothetical mineral deposit to demonstrate geostatistical resource estimation techniques commonly applied in the mining industry.
