# Imperial College BBO Capstone Project

This repository contains my final submission for the Imperial College Professional Certificate in Machine Learning and Artificial Intelligence Black-Box Optimisation (BBO) Capstone Project.

## Project overview

The aim of this project was to maximise eight unknown black-box objective functions using only a limited number of input-output observations. The internal mathematical form of each function was hidden, so the optimisation process relied on iterative experimentation, pattern recognition and careful balancing of exploration and exploitation.

The functions varied in dimensionality from 2D to 8D. Each input value was constrained to the range `[0, 1]`, and each submitted query returned a single scalar objective value. The task was to identify high-performing regions as efficiently as possible under a restricted query budget.

## Non-technical summary

This project explores how to make good decisions when the underlying system is unknown. I tested different input combinations for eight hidden functions and used the results to decide where to search next. The strategy evolved from broad exploration to more focused refinement around promising regions. This mirrors real-world machine learning work, where teams often need to tune models, experiments or systems with limited data and limited opportunities to test new ideas.

## Repository structure

```text
.
├── README.md                  # Project overview and instructions
├── bbo_capstone.ipynb          # Main notebook presenting the approach and results
├── DataSheet.md                # Datasheet for the optimisation observations
├── Model_Card.md               # Model card for the optimisation strategy
├── Documentation.md            # Detailed project documentation
├── functions.txt               # Function descriptions and sample application contexts
├── requirements.txt            # Python dependencies
└── LICENSE                     # MIT licence
```

## Optimisation approach

The project followed an iterative optimisation workflow:

1. **Initial exploration** – sample different areas of the search space to understand broad response patterns.
2. **Local refinement** – focus on regions that produced strong results in earlier rounds.
3. **Pattern-based search** – use previous query-output pairs to infer promising directions.
4. **Exploration-exploitation balance** – avoid overfitting to one region while still exploiting strong signals.
5. **Final consolidation** – compare trends across functions and document what worked best.

The final strategy was human-guided and pattern-based rather than a fully automated Bayesian optimisation implementation. However, it used ideas from surrogate modelling, SVM-style region classification and local search to guide query selection.

## Key results

The strongest improvements were observed on several higher-dimensional functions, especially Functions 4, 5, 6, 7 and 8. Function 5 showed the clearest improvement trend, increasing from an early score of approximately `368.57` to more than `1100` in later rounds. Function 8 also improved steadily across the project.

These results suggest that iterative local refinement can be highly effective when a function has a strong directional trend or a clear promising region. More irregular or noisy functions required a more cautious balance between exploration and exploitation.

## How to run the notebook

Create a Python environment and install the required packages:

```bash
pip install -r requirements.txt
```

Then open the notebook:

```bash
jupyter notebook bbo_capstone.ipynb
```

The notebook contains the recorded optimisation history, summary tables and visualisations of score evolution across rounds.

## Limitations

- The true objective functions were unknown.
- The dataset is small because the challenge used a limited query budget.
- The approach does not guarantee convergence to a global optimum.
- Some functions may have been under-explored due to the restricted number of evaluations.

## Future work

Future improvements could include:

- Gaussian Process surrogate models
- Bayesian optimisation acquisition functions such as Expected Improvement or UCB
- Ensemble surrogate models
- Automated exploration-exploitation scheduling
- More systematic hyperparameter tuning of the optimisation strategy

## Author

Istvan Takacs

