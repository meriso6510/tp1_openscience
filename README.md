# TP1 - Open Science (Windows)

## Objective
This project is part of the TP1 practical work to learn **Open Science**. Its goals are to:
- Install and use **Git and GitHub**
- Create a **reproducible scientific project**
- Use **Jupyter Notebook** on Windows
- Analyze simple data using **NumPy and Pandas**
- Document a complete scientific workflow

## Project Contents
- `README.md` : This file, explaining the project
- `data.csv` : The dataset used for analysis
- `analysis.ipynb` : Jupyter Notebook for data analysis and visualization

## Steps to Run
1. Install Git and GitHub Desktop on Windows
2. Create a local repository and link it to GitHub
3. Create project files (`README.md`, `data.csv`, `analysis.ipynb`)
4. Analyze data in Jupyter Notebook:
   - Read data from `data.csv`
   - Compute mean and standard deviation
   - Plot a bar chart for the values
5. Push all files to GitHub for sharing and version control

## Notes
- Ensure `data.csv` and `analysis.ipynb` are in the same folder
- If you encounter issues reading `data.csv`, specify encoding:
```python
pd.read_csv("data.csv", encoding="latin1")
