# Student Score Analysis | Big Data Analytics with Hadoop and Apache Spark

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Objectives](#objectives)
- [Technologies Used](#technologies-used)
- [Analysis Performed](#analysis-performed)
- [Key Findings](#key-findings)
- [Conclusion](#conclusion)
- [License](#license)
- [Author](#author)

## Project Overview

This project demonstrates the use of **Apache Spark and PySpark** for analyzing student academic performance data.

The project analyzes class scores and test scores across different subjects and students. The analysis includes data loading, schema inspection, descriptive statistics, subject-wise analysis, student-wise analysis, score comparisons, and performance categorization.

The project was developed using **Databricks** with PySpark.

## Dataset

The dataset is stored in CSV format and contains **40 student score records**.

### Dataset Columns

| Column | Description |
|---|---|
| Student | Name of the student |
| Subject | Subject name |
| Class Score | Score obtained in class |
| Test Score | Score obtained in test |

The dataset contains four subjects:

- Math
- Chemistry
- Physics
- Biology

There are **10 students** and **40 total records**.

## Objectives

The main objectives of this project are:

- Load and analyze a CSV dataset using PySpark.
- Inspect the dataset schema and statistics.
- Calculate subject-wise average scores.
- Calculate student-wise average scores.
- Identify students with the highest and lowest average test scores.
- Compare class scores with test scores.
- Calculate score gaps between class and test performance.
- Categorize subject performance based on average test scores.
- Present the analysis using Databricks visualizations.

## Technologies Used

- **Python**
- **PySpark**
- **Apache Spark**
- **Databricks**
- **CSV**
- **GitHub**

## Analysis Performed

The following analyses were performed using PySpark.

### 1. Data Loading

The CSV dataset was loaded into a Spark DataFrame using:

- Header detection
- Automatic schema inference

### 2. Schema Analysis

The dataset schema was inspected to identify the column names and data types.

The dataset contains:

- Student – String
- Subject – String
- Class Score – Integer
- Test Score – Double

### 3. Descriptive Statistics

Overall descriptive statistics were calculated, including:

- Number of records
- Mean
- Standard deviation
- Minimum value
- Maximum value

### 4. Subject-wise Analysis

Average class and test scores were calculated for each subject.

| Subject | Average Class Score | Average Test Score |
|---|---:|---:|
| Biology | 52.80 | 62.02 |
| Chemistry | 56.60 | 38.28 |
| Math | 47.20 | 54.65 |
| Physics | 59.80 | 61.36 |

### 5. Student-wise Analysis

Average class and test scores were calculated for each student.

The highest average test score was recorded by **Elvis**, with an average test score of **65.11**.

The lowest average test score was recorded by **Roby**, with an average test score of **44.98**.

### 6. Score Gap Analysis

The difference between average class score and average test score was calculated.

| Subject | Score Gap |
|---|---:|
| Biology | -9.22 |
| Chemistry | 18.32 |
| Math | -7.45 |
| Physics | -1.56 |

A positive value indicates that the average class score was higher than the average test score, while a negative value indicates that the average test score was higher.

### 7. Performance Categorization

Subjects were categorized according to their average test score:

- **High:** Average Test Score ≥ 60
- **Medium:** Average Test Score ≥ 50 and < 60
- **Low:** Average Test Score < 50

The resulting categories were:

| Subject | Performance |
|---|---|
| Biology | High |
| Physics | High |
| Math | Medium |
| Chemistry | Low |

### 8. Overall Performance

The overall results were:

| Metric | Result |
|---|---:|
| Total Records | 40 |
| Overall Class Average | 54.10 |
| Overall Test Average | 54.08 |

A bar chart was also created in Databricks to visualize the average test scores by subject.

## Key Findings

- **40** student score records were analyzed.
- The overall class average was **54.10**.
- The overall test average was **54.08**.
- **Biology** had the highest average test score at **62.02**.
- **Chemistry** had the lowest average test score at **38.28**.
- **Elvis** had the highest average test score among students at **65.11**.
- **Roby** had the lowest average test score among students at **44.98**.
- Two subjects were categorized as **High** performance.
- One subject was categorized as **Medium** performance.
- One subject was categorized as **Low** performance.

## Conclusion

This project demonstrates how **PySpark and Apache Spark** can be used to process and analyze structured student performance data.

The analysis provides insights into student-wise and subject-wise performance, compares class and test scores, and identifies differences in academic performance.

Although the dataset used in this project is relatively small, the same Spark-based data processing approach can be applied to larger datasets in Big Data environments.

## License

Distributed under the MIT License. See the `LICENSE` file for more information.

## Author

**Shobitha**