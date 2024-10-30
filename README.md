# Curioo Member Segmentation

This project aims to segment Curioo members into different groups based on demographic and behavioral data. The segmentation process helps us better understand our customer base and allows Curioo to tailor its services to meet the specific needs of each group.

## Objectives
- **Segment members** to identify distinct customer groups.
- **Improve service offerings** by understanding the demographics and preferences of each segment.
- **Utilize insights** for targeted marketing and customer relationship management.

## Project Overview
The segmentation process uses machine learning to group similar members together. This grouping allows us to identify patterns and characteristics within each segment, ultimately helping Curioo personalize its approach to different types of members.

### Key Steps in Segmentation
1. **Data Preparation**: 
   - Load and clean the data from `member-demo-data.xlsx`.
   - Standardize column names by removing spaces, special characters, and converting them to lowercase.

2. **Preprocessing**: 
   - Handle missing data by removing empty columns and rows.
   - Split the data into **numerical** and **categorical** types.
   - Encode categorical columns for use in machine learning.
   - Standardize numerical values to ensure all data scales similarly.

3. **Clustering**:
   - Use the **K-Means clustering algorithm** to segment members based on preprocessed data.
   - Use the **Elbow method** to find the optimal number of clusters.
   - Assign each member to a cluster and save the results for further analysis.

4. **Evaluation**:
   - Use the **Silhouette Score** to measure the quality of clustering. This score ranges from -1 to 1, with higher scores indicating well-defined clusters.

### Outputs
- **Segmented Data**: The final data with assigned cluster labels is saved as `segmented_customers.xlsx` and `segmented_customers.csv` in the `output` folder. These files can be reviewed and analyzed to understand the unique characteristics of each segment.

## File Structure
- `data/member-demo-data.xlsx`: Original input file containing Curioo member demographic data.
- `output/segmented_customers.xlsx`: Output file with added cluster labels.
- `output/segmented_customers.csv`: CSV version of the output file.

## Key Concepts Explained
- **Clustering**: A way to group similar data points together. In this project, K-Means clustering groups members with similar characteristics.
- **One-Hot Encoding**: Converts categorical data into a numerical format suitable for machine learning.
- **Standard Scaling**: Ensures all features contribute equally to the clustering process by standardizing them on a similar scale.

### Note on Methodology
The **Elbow Method** helps determine the best number of clusters by calculating the variance in each cluster as clusters are added. The **Silhouette Score** gives an overall score to see how well each point fits within its assigned cluster.

## Segmentation Results

Based on the clustering, three distinct member personas emerged:

### Persona 1: The Supportive Guardian
These parents have moderate expectations and adopt a relaxed approach, prioritizing their child’s happiness and allowing for natural exploration of interests.

Key Traits:
- Limited focus on extracurricular activities.
- Moderate engagement in child development.
- Emphasis on emotional well-being and social skills.

### Persona 2: The Growth Seeker
Proactive yet balanced, these parents encourage extracurricular participation while focusing on responsibility, confidence, and social skills.

Key Traits:
- Moderate involvement in sports and language activities.
- Strong focus on developing social skills and responsibility.

### Persona 3: The Ambitious Achiever
Highly engaged parents who enroll their children in a variety of activities, with high expectations for growth, intelligence, and creativity geared towards long-term success.

Key Traits:
- Emphasis on academic skills.
- High involvement in diverse extracurriculars, especially STEM.
- Strong focus on intelligence and career-oriented skills.

## Glossary
- **K-Means**: A clustering algorithm that groups data into a predetermined number of clusters.
- **Elbow Method**: A technique to determine the ideal number of clusters by looking for the "elbow" in a plot of variance vs. the number of clusters.
- **Silhouette Score**: A metric to evaluate the compactness and separation of clusters.