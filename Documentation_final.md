# BBO Capstone Project Documentation

## 1. Project context

This project was completed as part of the Imperial College Professional Certificate in Machine Learning and Artificial Intelligence. The capstone task focused on Black-Box Optimisation (BBO), where the goal was to maximise a set of unknown functions using only observed input-output pairs.

In a black-box setting, the internal structure of the objective function is unavailable. There are no gradients, equations or direct explanations of why a given input produces a given output. This makes the task similar to many real-world machine learning and engineering problems where experimentation is expensive and decisions must be made under uncertainty.

## 2. Problem definition

The project involved eight functions with different input dimensionalities:

- Function 1: 2 dimensions
- Function 2: 2 dimensions
- Function 3: 3 dimensions
- Function 4: 4 dimensions
- Function 5: 4 dimensions
- Function 6: 5 dimensions
- Function 7: 6 dimensions
- Function 8: 8 dimensions

Each input value was constrained to the range `[0, 1]`. Each query returned one scalar output value. The optimisation goal was to maximise the output of each function while using a limited number of queries.

## 3. Technical approach

The project used an iterative, pattern-based optimisation process. Rather than applying a single fixed algorithm, the strategy evolved as more observations became available.

### Initial exploration

The early rounds focused on broad sampling. The goal was to understand the approximate behaviour of each function and identify whether any region of the search space appeared promising.

### Local refinement

Once high-performing regions were identified, the strategy shifted toward local refinement. Small perturbations were applied around strong candidate inputs to test whether the output improved or deteriorated.

### Surrogate-inspired reasoning

Although the final implementation was not a fully automated Bayesian optimiser, the decision process was influenced by surrogate modelling concepts. Historical observations were used to infer which regions were likely to be high-performing. In particular, SVM-style thinking helped reframe the task as identifying promising versus poor regions rather than predicting exact output values.

### Exploration and exploitation

A key challenge was balancing exploration and exploitation:

- Exploration helped discover new areas of the search space.
- Exploitation helped refine already promising regions.

The best results came from adapting this balance per function rather than applying the same strategy globally.

## 4. Results summary

The strongest improvements were seen in Functions 4, 5, 6, 7 and 8. Function 5 showed a particularly clear improvement trend, rising from early scores around 368 to later scores above 1000. Function 8 improved steadily over multiple rounds, suggesting that directional refinement was effective.

Not all functions behaved the same way. Some functions benefited from local search, while others required broader exploration due to noise, flat regions or possible local optima.

## 5. Lessons learned

The most important lesson from the project was that successful optimisation depends on systematic experimentation rather than a single algorithmic trick. Small, well-measured changes often produced more reliable improvements than large untested changes.

The project also reinforced that optimisation strategies must be adapted to the problem structure. A method that works well for a smooth or unimodal function may not work well for a noisy or highly multimodal function.

## 6. Real-world relevance

The methods and trade-offs in this project are directly relevant to professional ML and AI projects, including:

- hyperparameter optimisation
- model selection
- A/B testing
- resource allocation
- simulation-based optimisation
- decision-making under uncertainty

In production ML systems, teams often have limited time, limited compute and imperfect feedback. The structured experimentation approach used in this project is therefore highly transferable to real-world AI development.
