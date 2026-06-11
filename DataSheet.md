# Datasheet for the BBO Capstone Dataset

## 1. Motivation

### What task does this dataset help to solve?

This dataset was created as part of the Black-Box Optimisation (BBO) Capstone Project. Its purpose is to support the optimisation of unknown objective functions under a limited query budget. The dataset records historical query points and their corresponding function evaluations, allowing optimisation strategies to learn from previous observations.

### Who created it and why?

The dataset was created by the project participant during the Imperial College Professional Certificate in Machine Learning and Artificial Intelligence programme.

### Funding or organisational support

The dataset was generated as part of an educational capstone project provided by Imperial College London. No external funding was received.

---

## 2. Composition

### What does the dataset contain?

The dataset contains historical optimisation observations collected during multiple rounds of the BBO challenge.

Each observation consists of:

* A function identifier (Function 1–8)
* An input vector with dimensionality between 2 and 8
* A corresponding scalar output value returned by the optimisation portal

### Dataset size

At the time of writing, the dataset contains approximately:

* 10 optimisation rounds
* 8 functions
* Approximately 80 query-output observations

### Data format

Inputs are stored as numerical vectors with values between 0 and 1.

Example:

Input:
[0.500000, 0.500000]

Output:
2.6752879910742468e-9

### Missing data

No missing values are known.

### Relationships between instances

Observations belonging to the same function form a sequential optimisation history.

### Recommended split

No formal train/test split is defined because the dataset is primarily intended for iterative optimisation rather than supervised learning.

---

## 3. Collection Process

### How was the data collected?

The data was collected through repeated interactions with the BBO challenge platform.

During each round:

1. A query point was submitted for each function.
2. The platform evaluated the unknown function.
3. The resulting output value was recorded.

### Query generation strategy

The strategy evolved over time:

* Early rounds focused on exploration of the search space.
* Later rounds increasingly focused on exploitation of promising regions identified from previous results.

### Collection timeframe

The dataset was collected throughout the duration of the BBO Capstone Project over multiple weeks.

### Ethical review

Not applicable.

### Consent requirements

Not applicable because no human participants were involved.

---

## 4. Preprocessing / Cleaning / Labelling

### Preprocessing

Minimal preprocessing was applied.

The original numerical values were preserved.

### Cleaning

Basic validation was performed to ensure:

* Correct dimensionality
* Numerical formatting
* Valid input ranges

### Labelling

Each observation is labelled by:

* Function identifier
* Round number

### Raw data preservation

The original query and response history is preserved.

---

## 5. Uses

### Intended uses

This dataset is intended for:

* Educational optimisation experiments
* Black-box optimisation research
* Analysis of exploration versus exploitation strategies
* Evaluation of optimisation heuristics

### Potential risks

The dataset provides sparse coverage of higher-dimensional search spaces and may therefore produce misleading conclusions if treated as a comprehensive representation of the underlying functions.

### Not recommended for

* Real-world engineering optimisation
* Safety-critical applications
* Benchmarking production optimisation systems

---

## 6. Distribution

### Availability

The dataset is distributed through the project's public GitHub repository.

### Distribution method

GitHub repository and associated documentation.

### Licence

Educational use only.

### Restrictions

The dataset should be used only for educational and research purposes associated with optimisation methods.

---

## 7. Maintenance

### Maintainer

Istvan Takacs

### Version control

The dataset is maintained using Git and GitHub version control.

### Updates

New observations are added after each optimisation round.

### Long-term maintenance

The dataset will remain available as part of the BBO Capstone Project repository.

### Additional comments

Because the underlying objective functions remain unknown, the dataset should be interpreted as an optimisation history rather than as a complete representation of the search space.





Function 1:	[0.732451, 0.184562]
Function 2:	[0.281943, 0.907512]
Function 3:	[0.512374, 0.223145, 0.781256]
Function 4:	[0.134567, 0.845231, 0.672314, 0.298765]
Function 5:	[0.923145, 0.114578, 0.556782, 0.778234]
Function 6:	[0.345612, 0.789123, 0.234567, 0.901245, 0.567812]
Function 7:	[0.112345, 0.667890, 0.445566, 0.998877, 0.223344, 0.556677]
Function 8:	[0.345678, 0.123456, 0.789012, 0.456789, 0.234567, 0.890123, 0.567890, 0.678901]
This week's output values:

Function 1:	-6.23129247271054e-107
Function 2:	0.05602055724992106
Function 3:	-0.11153462988907648
Function 4:	-18.2832699220106
Function 5:	368.56750032579504
Function 6:	-1.513563053237219
Function 7:	0.017163199718945744
Function 8:	7.898208282889399


This week's input values:

Function 1:	[0.213456, 0.823456]
Function 2:	[0.812345, 0.123456]
Function 3:	[0.823456, 0.712345, 0.134567]
Function 4:	[0.712345, 0.123456, 0.845678, 0.934567]
Function 5:	[0.903145, 0.134578, 0.576782, 0.758234]
Function 6:	[0.823456, 0.234567, 0.912345, 0.123456, 0.678901]
Function 7:	[0.623456, 0.112345, 0.823456, 0.234567, 0.934567, 0.345678]
Function 8:	[0.365678, 0.143456, 0.769012, 0.436789, 0.254567, 0.870123, 0.547890, 0.698901]
This week's output values:

Function 1:	1.8459222090344106e-143
Function 2:	-0.007836911068078937
Function 3:	-0.0810921906536616
Function 4:	-28.804736647133904
Function 5:	290.83891562489106
Function 6:	-2.0835369587552997
Function 7:	0.015127937689235213
Function 8:	8.0227579788894



This week's input values:

Function 1:	[0.500000, 0.500000]
Function 2:	[0.200000, 0.800000]
Function 3:	[0.200000, 0.800000, 0.600000]
Function 4:	[0.300000, 0.700000, 0.200000, 0.800000]
Function 5:	[0.933145, 0.104578, 0.566782, 0.788234]
Function 6:	[0.600000, 0.400000, 0.700000, 0.300000, 0.800000]
Function 7:	[0.500000, 0.500000, 0.500000, 0.500000, 0.500000, 0.500000]
Function 8:	[0.385678, 0.163456, 0.749012, 0.416789, 0.274567, 0.850123, 0.527890, 0.718901]
This week's output values:

Function 1:	2.6752879910742468e-9
Function 2:	-0.11622767767250802
Function 3:	-0.07853432775618217
Function 4:	-15.300482957509526
Function 5:	429.6249049021148
Function 6:	-1.4444485674971963
Function 7:	0.5053149917022333
Function 8:	8.1388276748894



This week's input values:

Function 1:	[0.480000, 0.520000]
Function 2:	[0.300000, 0.950000]
Function 3:	[0.150000, 0.850000, 0.650000]
Function 4:	[0.250000, 0.750000, 0.150000, 0.850000]
Function 5:	[0.943145, 0.094578, 0.571782, 0.798234]
Function 6:	[0.650000, 0.350000, 0.750000, 0.250000, 0.850000]
Function 7:	[0.520000, 0.480000, 0.520000, 0.480000, 0.520000, 0.480000]
Function 8:	[0.405678, 0.183456, 0.729012, 0.396789, 0.294567, 0.830123, 0.507890, 0.738901]
This week's output values:

Function 1:	3.610551873256356e-10
Function 2:	0.061427339097219244
Function 3:	-0.11754957298088232
Function 4:	-19.2908006782375
Function 5:	493.33385699255996
Function 6:	-1.465266041558761
Function 7:	0.4622180614928867
Function 8:	8.2464173708894


Function 1:	[0.480000, 0.520000]
Function 2:	[0.300000, 0.950000]
Function 3:	[0.150000, 0.850000, 0.650000]
Function 4:	[0.250000, 0.750000, 0.150000, 0.850000]
Function 5:	[0.943145, 0.094578, 0.571782, 0.798234]
Function 6:	[0.650000, 0.350000, 0.750000, 0.250000, 0.850000]
Function 7:	[0.520000, 0.480000, 0.520000, 0.480000, 0.520000, 0.480000]
Function 8:	[0.405678, 0.183456, 0.729012, 0.396789, 0.294567, 0.830123, 0.507890, 0.738901]
This week's output values:

Function 1:	3.610551873256356e-10
Function 2:	0.061427339097219244
Function 3:	-0.11754957298088232
Function 4:	-19.2908006782375
Function 5:	493.33385699255996
Function 6:	-1.465266041558761
Function 7:	0.4622180614928867
Function 8:	8.2464173708894



Function 1:	[0.500000, 0.500000]
Function 2:	[0.280000, 0.980000]
Function 3:	[0.180000, 0.820000, 0.620000]
Function 4:	[0.280000, 0.720000, 0.180000, 0.820000]
Function 5:	[0.953145, 0.084578, 0.576782, 0.808234]
Function 6:	[0.620000, 0.380000, 0.720000, 0.280000, 0.820000]
Function 7:	[0.510000, 0.490000, 0.510000, 0.490000, 0.510000, 0.490000]
Function 8:	[0.425678, 0.203456, 0.709012, 0.376789, 0.314567, 0.810123, 0.487890, 0.758901]
This week's output values:

Function 1:	2.6752879910742468e-9
Function 2:	0.12055643886992715
Function 3:	-0.0925094902972774
Function 4:	-16.733968498081293
Function 5:	563.827849085295
Function 6:	-1.570007733817707
Function 7:	0.48528833849678643
Function 8:	8.3455270668894



This week's input values:

Function 1:	[0.502000, 0.498000]
Function 2:	[0.260000, 0.990000]
Function 3:	[0.170000, 0.830000, 0.640000]
Function 4:	[0.270000, 0.730000, 0.170000, 0.830000]
Function 5:	[0.963145, 0.074578, 0.581782, 0.818234]
Function 6:	[0.640000, 0.360000, 0.740000, 0.260000, 0.840000]
Function 7:	[0.500000, 0.500000, 0.500000, 0.500000, 0.500000, 0.500000]
Function 8:	[0.445678, 0.223456, 0.689012, 0.356789, 0.334567, 0.790123, 0.467890, 0.778901]
This week's output values:

Function 1:	2.6243944833566956e-9
Function 2:	0.1223429113632693
Function 3:	-0.10173915255267799
Function 4:	-17.537636124233952
Function 5:	641.621898334627
Function 6:	-1.5327605434852412
Function 7:	0.5053149917022333
Function 8:	8.4361567628894


This week's input values:

Function 1:	[0.501000, 0.499000]
Function 2:	[0.250000, 0.995000]
Function 3:	[0.190000, 0.810000, 0.610000]
Function 4:	[0.320000, 0.680000, 0.220000, 0.780000]
Function 5:	[0.973145, 0.054578, 0.586782, 0.828234]
Function 6:	[0.580000, 0.420000, 0.680000, 0.320000, 0.780000]
Function 7:	[0.495000, 0.505000, 0.495000, 0.505000, 0.495000, 0.505000]
Function 8:	[0.465678, 0.243456, 0.669012, 0.336789, 0.354567, 0.770123, 0.447890, 0.798901]
This week's output values:

Function 1:	2.662476242307926e-9
Function 2:	0.05866829169156555
Function 3:	-0.0770403198439556
Function 4:	-13.97343533647997
Function 5:	727.2324220118297
Function 6:	-1.4326720688563317
Function 7:	0.5140397204538378
Function 8:	8.5183064588894



This week's input values:

Function 1:	[0.499000, 0.501000]
Function 2:	[0.255000, 0.993000]
Function 3:	[0.185000, 0.815000, 0.615000]
Function 4:	[0.340000, 0.660000, 0.240000, 0.760000]
Function 5:	[0.993145, 0.024578, 0.596782, 0.848234]
Function 6:	[0.550000, 0.450000, 0.650000, 0.350000, 0.750000]
Function 7:	[0.488000, 0.512000, 0.488000, 0.512000, 0.488000, 0.512000]
Function 8:	[0.495678, 0.273456, 0.639012, 0.306789, 0.384567, 0.740123, 0.417890, 0.828901]
This week's output values:

Function 1:	2.662476242307926e-9
Function 2:	-0.004922273917338543
Function 3:	-0.10437374437597904
Function 4:	-12.570714782541781
Function 5:	924.3877721924916
Function 6:	-1.2910571082837123
Function 7:	0.524682306096945
Function 8:	8.6256310028894

This week's input values:

Function 1:	[0.500500, 0.499500]
Function 2:	[0.262000, 0.988000]
Function 3:	[0.205000, 0.795000, 0.595000]
Function 4:	[0.380000, 0.620000, 0.280000, 0.720000]
Function 5:	[0.998145, 0.014578, 0.601782, 0.858234]
Function 6:	[0.500000, 0.500000, 0.600000, 0.400000, 0.700000]
Function 7:	[0.485000, 0.515000, 0.485000, 0.515000, 0.485000, 0.515000]
Function 8:	[0.515678, 0.293456, 0.619012, 0.286789, 0.404567, 0.720123, 0.397890, 0.848901]
This week's output values:

Function 1:	2.672079499659047e-9
Function 2:	0.02321244292782419
Function 3:	-0.0565654583219134
Function 4:	-10.004838381941735
Function 5:	1003.876452155842
Function 6:	-1.2955387147441206
Function 7:	0.5286542591237683
Function 8:	8.6865806988894