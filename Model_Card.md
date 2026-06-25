# Model Card: Iterative Pattern-Based Black-Box Optimisation Strategy

## Model overview

**Model name:** Iterative Pattern-Based Black-Box Optimisation Strategy  
**Version:** 1.0  
**Developer:** Istvan Takacs  
**Project:** Imperial College BBO Capstone Project  
**Licence:** MIT licence for repository materials; educational use for course-specific data and results.

## Description

This is a human-guided optimisation strategy developed for the Imperial College Black-Box Optimisation Capstone Project. The approach uses historical input-output observations to identify promising regions of the search space and iteratively refine future candidate solutions.

The method is not a production-grade automated optimiser. It is an educational optimisation workflow combining exploration, exploitation, local refinement and surrogate-inspired reasoning.

## Intended use

### Primary task

Maximise unknown black-box objective functions under a limited query budget.

### Target users

- Students studying optimisation methods
- Researchers exploring black-box optimisation concepts
- Practitioners interested in limited-budget experimentation

### Recommended use cases

- Educational black-box optimisation exercises
- Small-scale optimisation experiments
- Demonstrations of exploration-exploitation trade-offs
- Analysis of sequential optimisation behaviour

### Not recommended for

- Safety-critical optimisation
- Industrial optimisation without further validation
- Problems requiring guaranteed convergence
- High-dimensional production optimisation without automated surrogate modelling

## Training and input data

### Data sources

The strategy uses historical query-output pairs collected during the BBO Capstone Project.

### Dataset size

Approximately 10 optimisation rounds across 8 functions.

### Data format

- Inputs: numerical vectors with values in `[0, 1]`
- Outputs: scalar objective function values

### Preprocessing

Minimal preprocessing was applied. Inputs and outputs were preserved in their original numerical format and organised by function and round.

## Evaluation

### Metrics

- Objective function value
- Improvement over previous best result
- Trend consistency across optimisation rounds
- Robustness across different function types

### Performance summary

The strategy produced strong improvements on several functions, especially Functions 4, 5, 6, 7 and 8. Function 5 showed the largest improvement, increasing from an early value of approximately `368.57` to more than `1100` in later rounds. Function 8 also improved steadily across the project.

## Ethical considerations

### Human subjects

Not applicable. The dataset contains only synthetic numerical optimisation data.

### Privacy concerns

None identified.

### Bias and limitations

The main limitation is sampling bias. Because the query budget was small, the optimisation history covers only a sparse subset of each function's search space. The strategy may over-focus on regions that performed well early and may miss better regions elsewhere.

### Risk mitigation

- Maintain a balance between exploration and exploitation.
- Track performance trends across rounds.
- Document all assumptions and limitations.
- Avoid using the method for safety-critical decisions without further validation.

## Model lifecycle

**Last updated:** 2026-06-25  
**Version control:** GitHub repository  
**Monitoring plan:** For future work, the strategy could be extended with automated surrogate models, acquisition functions and more formal evaluation across benchmark optimisation problems.
