# Datasheet for the BBO Capstone Dataset

## 1. Motivation

### What task does this dataset help solve?

This dataset was created for the Imperial College Black-Box Optimisation (BBO) Capstone Project. It supports the optimisation of unknown objective functions under a limited query budget by recording previous query points and their corresponding objective values.

### Who created the dataset and why?

The dataset was created by Istvan Takacs during the Imperial College Professional Certificate in Machine Learning and Artificial Intelligence. It was created to document the optimisation process and support transparent reflection on the strategies used during the capstone project.

### Funding or organisational support

The dataset was generated as part of an educational capstone project. No external funding was received.

## 2. Composition

### What does the dataset contain?

The dataset contains historical optimisation observations collected during multiple rounds of the BBO challenge.

Each observation consists of:

- a function identifier, from Function 1 to Function 8
- an input vector
- a scalar output value returned by the black-box function
- the round or week in which the query was submitted

### Dimensionality

The eight functions have different input dimensionalities:

- Function 1: 2D
- Function 2: 2D
- Function 3: 3D
- Function 4: 4D
- Function 5: 4D
- Function 6: 5D
- Function 7: 6D
- Function 8: 8D

### Dataset size

The dataset contains approximately 10 rounds of observations across 8 functions, giving around 80 query-output records.

### Data format

Inputs are numerical vectors with values in the range `[0, 1]`. Outputs are scalar numerical values.

Example:

```text
Function 1 input: [0.500000, 0.500000]
Function 1 output: 2.6752879910742468e-9
```

### Missing data

No missing values are known.

### Relationships between instances

Observations belonging to the same function form a sequential optimisation history. Later queries were influenced by previous observations.

### Recommended split

No formal train-test split is defined. The dataset is primarily intended for sequential optimisation analysis rather than supervised learning.

## 3. Collection process

### How was the data collected?

The data was collected through repeated interactions with the BBO challenge platform.

During each round:

1. One candidate input was submitted for each function.
2. The platform returned a scalar output value.
3. The input-output pair was recorded.
4. The next round of inputs was selected based on previous results.

### Query generation strategy

The query generation strategy evolved over time:

- early rounds prioritised broad exploration
- later rounds used local refinement around promising regions
- some functions used more exploitation where a strong trend was visible
- other functions retained more exploration where results were noisy or unclear

### Ethical review

Not applicable. The dataset does not contain human-subject data.

### Consent requirements

Not applicable.

## 4. Preprocessing, cleaning and labelling

### Preprocessing

Minimal preprocessing was applied. Numerical values were preserved in their original format.

### Cleaning

Basic validation was performed to ensure:

- correct dimensionality
- valid numerical values
- inputs within the `[0, 1]` range

### Labelling

Each observation is labelled by:

- function identifier
- round number
- input vector
- output value

### Raw data preservation

The original query and response history is preserved in the project repository.

## 5. Uses

### Intended uses

This dataset is intended for:

- educational optimisation experiments
- analysis of black-box optimisation strategies
- exploration-exploitation trade-off analysis
- documentation of the BBO capstone workflow

### Potential risks

The dataset is sparse, especially for higher-dimensional functions. It should not be interpreted as a complete representation of the underlying objective functions.

### Not recommended for

- real-world engineering optimisation
- safety-critical decision-making
- production benchmarking
- drawing strong conclusions about global optima

## 6. Distribution

### Availability

The dataset is distributed through the public GitHub repository for the BBO Capstone Project.

### Distribution method

GitHub repository and associated documentation files.

### Licence

Repository materials are provided under the MIT licence. Course-specific data and results should be treated as educational project material.

## 7. Maintenance

### Maintainer

Istvan Takacs

### Version control

The dataset is maintained using Git and GitHub.

### Updates

The dataset reflects the final state of the capstone project. Future updates may add improved documentation, visualisations or more formal optimisation experiments.

### Long-term maintenance

The repository is intended to remain available as a portfolio-ready educational project.

## 8. Additional comments

Because the objective functions remain unknown, this dataset should be interpreted as an optimisation history rather than a complete dataset describing the functions. Its main value is to document decision-making under uncertainty and the evolution of the optimisation strategy.
