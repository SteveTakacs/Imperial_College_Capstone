Model overview
Model name: Iterative Pattern-Based Black-Box Optimisation Strategy
Version: 1.0
Developer(s): Istvan Takacs
Contact information: GitHub repository
Licence: Educational use only

Description:

Human-guided optimisation strategy developed for the Imperial College Black-Box Optimisation (BBO) Capstone Project. The approach uses historical query-output pairs to identify promising regions of the search space and iteratively refine candidate solutions.

Intended use

Primary task:

Optimisation of unknown black-box objective functions under a limited query budget.

Target users:

Students, researchers and practitioners studying optimisation methods.

Recommended use cases:

Educational optimisation exercises
Black-box optimisation problems with small evaluation budgets
Exploratory analysis of unknown functions

Not recommended for:

Safety-critical optimisation
High-dimensional industrial optimisation without additional surrogate models
Problems requiring guaranteed convergence
Training data

Data sources:

Historical query-output pairs collected during the BBO Capstone Project.

Size of dataset:

Approximately 10 rounds × 8 functions.

Languages or modalities:

Numerical vectors and scalar objective values.

Preprocessing steps:

No major preprocessing applied.
Inputs maintained in original numerical format.
Historical observations organised by function and round.
Evaluation metrics

Metrics used:

Objective function value
Improvement over previous best result
Trend consistency across optimisation rounds

Performance results:

Strong improvements were observed for Functions 4, 5, 6, 7 and 8 through iterative refinement. Function 5 achieved the largest improvement, increasing from approximately 369 in early rounds to over 900 in later rounds.

Fairness or bias checks:

Not applicable because the optimisation problem does not involve human subjects or demographic data.

Ethical considerations

Potential biases or risks:

Sampling bias toward previously successful regions
Risk of converging to local optima
Under-exploration of large areas of the search space

Mitigation strategies:

Combination of exploration and exploitation
Periodic return to historically successful regions
Transparent documentation of query history

Privacy concerns:

None. The dataset contains only synthetic numerical optimisation data.

Model life cycle

Date of last update:

2026-06-04

Version control or repository:

GitHub repository associated with the BBO Capstone Project.

Monitoring plan:

The strategy is updated after each optimisation round using newly observed query-output pairs. Future updates would incorporate additional observations and potentially more advanced surrogate modelling techniques.