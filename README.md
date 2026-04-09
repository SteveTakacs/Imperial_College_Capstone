Black-Box Optimisation (BBO) Capstone Project
1. Project Overview
This project focuses on solving a Black-Box Optimisation (BBO) challenge, where the goal is to maximise a set of unknown functions using only observed input-output pairs.

The internal structure of these functions is completely hidden. Instead of having access to gradients or equations, the optimisation process relies entirely on iteratively querying the system and learning from the responses.

The objective is to efficiently identify high-performing input regions under strict query constraints, which closely mirrors real-world machine learning problems such as:

hyperparameter tuning
A/B testing
simulation-based optimisation
decision-making under uncertainty
From a career perspective, this project strengthens key data science skills such as:

optimisation with limited data
iterative experimentation
balancing exploration vs exploitation
making decisions under uncertainty
These are highly relevant for roles in machine learning, data science, and optimisation-driven systems.

2. Inputs and Outputs
Inputs
Each function receives a vector of continuous values:

x1-x2-x3-...-xn
Where:

each value is in the range [0, 1]
each value is formatted to six decimal places
dimensionality varies per function (from 2D to 8D)
Example:

0.345678-0.123456
0.823456-0.712345-0.134567
Outputs
Each query returns:

a single scalar value
representing the performance of the input
Example:

Function output: 368.5675
Function output: -0.08109
No additional information is provided (e.g. gradients, noise level, or function form).

3. Challenge Objectives
The main objective is to:

Maximise the output of each black-box function using a limited number of queries

Key constraints:
Only one query per function per iteration
Very limited dataset (sequential learning)
Unknown function structure
High dimensionality (up to 8D)
Core challenge:
Efficiently decide where to sample next, balancing:

Exploration → testing unknown or uncertain regions
Exploitation → refining known high-performing regions
The goal is not just to find good values, but to do so efficiently and systematically.

4. Technical Approach
This project follows an iterative optimisation strategy, evolving across multiple rounds.

Week 1 – Initial Exploration
Broad sampling of the input space
Minimal assumptions about function behaviour
Goal: understand general response patterns
This stage focused on coverage rather than optimisation.

Week 2 – Local Refinement
Identified high-performing regions
Applied small perturbations around strong candidates
For example:

Function 5 showed a very high output (~368), indicating a strong peak
Function 8 showed moderate but consistent performance
This led to:

exploitation for promising functions
continued exploration for unclear ones
Week 3 – Structured Strategy with SVM Perspective
In this iteration, the approach became more structured and model-inspired.

SVM-inspired thinking
Instead of predicting exact outputs, the problem was partially reframed as:

classifying regions into high-performance vs low-performance

High outputs → “positive class”
Low outputs → “negative class”
A soft-margin SVM would be appropriate here due to:

noisy observations
imperfect separation between regions
Additionally, a kernel SVM (e.g. RBF) could capture:

non-linear boundaries
sharp peaks (e.g. Function 5)
While no explicit SVM model was trained, this perspective influenced query selection by:

focusing on regions likely to belong to the “high-performance class”
avoiding consistently poor regions
Exploration vs Exploitation Strategy
The current approach is a hybrid strategy:

Exploitation
Applied to strong signals:
Function 5 → clear peak → local refinement
Function 8 → improving trend → directional search
Exploration
Applied where signal is weak:
Functions with near-zero or inconsistent outputs
Includes:
sampling new regions
moving toward central areas
diversifying inputs
Key Strengths of the Approach
Combines data-driven insights with intuition
Adapts strategy per function, not globally
Uses implicit modelling concepts (SVM, surrogate reasoning)
Maintains a balanced exploration–exploitation trade-off
Future Improvements
Introduce Gaussian Process surrogate models
Use acquisition functions (Expected Improvement, UCB)
Combine:
regression (value prediction)
classification (region filtering via SVM)
Analyse feature importance in higher dimensions