# DataView - Advanced Data Analysis and Visualization

## Overview

**DataView** is a user-friendly web application built using **Streamlit**, **Pandas**, **Seaborn**, and **Matplotlib** for advanced data analysis and visualization. The app allows users to upload a dataset (CSV or Excel), visualize it in various chart types (e.g., bar charts, pie charts, histograms), and download the generated charts in multiple formats (PNG, PDF). The app also stores a history of previously generated charts.

## Key Features

- **Dataset Upload**: Upload CSV or Excel files.
- **Data Visualization**: Create various types of charts including bar charts, pie charts, line charts, scatter plots, heatmaps, and more.
- **Chart Customization**: Users can select different columns for X and Y axes based on the chart type.
- **Chart History**: Store and view previously generated charts.
- **Chart Download**: Download generated charts as PNG or PDF.
- **Data Insights**: Provides basic insights and summaries of the data, including mean, median, and mode.

## Functionality Breakdown

### 1. Dataset Upload

- Users can upload datasets in **CSV** or **Excel** format using the file uploader.
- The app automatically detects the file type (CSV or Excel) and loads it into a Pandas DataFrame.
- A preview of the uploaded data (first 5 rows) is displayed to give users an idea of the data they are working with.

### 2. Data Visualization

The app allows users to select from multiple chart types, each of which can be customized based on the selected columns from the uploaded dataset. Below is a breakdown of the available chart types:

#### Chart Types:

- **Bar Chart**: Visualizes data with bars; requires both X and Y axes.
- **Pie Chart**: Displays the distribution of values in a categorical column.
- **Line Chart**: Plots data points as a line; requires both X and Y axes.
- **Scatter Plot**: Plots data points as dots; requires both X and Y axes.
- **Histogram**: Plots the distribution of a numerical column.
- **Box Plot**: Displays the distribution of a numerical column with quartiles and outliers.
- **Heatmap**: Shows correlations between numerical columns.
- **Area Chart**: Visualizes data in a cumulative area plot.
- **Stacked Bar Chart**: Stacked bar chart for categorical columns.
- **Violin Plot**: Displays the distribution of a numerical column similar to a box plot but with more detailed information.

### 3. Chart Download

Once a chart is generated, users have the option to download it in **PNG** or **PDF** format. This is implemented using the download button, allowing the user to download the visualizations.

### 4. Chart History

The app stores the previously generated charts in the session state and allows users to view them again. This functionality is helpful if users want to compare or revisit past charts.

### 5. Error Handling

The app includes error handling to manage issues that may arise with data types or chart generation. For instance, if a heatmap is requested but not enough numeric columns are available, the app will show an error message.

### 6. Data Insights

Although not implemented in the current version of the app, you could easily extend this app to include basic data analysis insights such as:

- **Mean**: Average value of a numeric column.
- **Median**: Middle value of a numeric column.
- **Mode**: Most frequent value(s) of a categorical or numeric column.

---

## Detailed Documentation on Chart Types

### Bar Chart
A bar chart is used to compare values across different categories. The height of the bars represents the value of each category.
- **X-axis**: The categorical variable (e.g., "Name", "Age", etc.).
- **Y-axis**: The numeric variable (e.g., "Salary", "Height", etc.).

### Pie Chart
A pie chart shows the proportion of each category within a whole. It's useful for showing how different segments contribute to a total.
- **X-axis**: The categorical variable.

### Line Chart
A line chart is used to show trends over time (or other ordered categories). It connects individual data points with a line.
- **X-axis**: The independent variable (e.g., "Date").
- **Y-axis**: The dependent variable (e.g., "Price").

### Scatter Plot
A scatter plot visualizes the relationship between two numerical variables by plotting data points on a two-dimensional graph.
- **X-axis**: The independent numerical variable.
- **Y-axis**: The dependent numerical variable.

### Histogram
A histogram displays the frequency distribution of a numeric column by dividing the data into bins and plotting the number of data points in each bin.
- **X-axis**: The numeric variable.

### Box Plot
A box plot summarizes the distribution of a numeric column through its quartiles, with the "box" showing the interquartile range and "whiskers" showing the range of the data.
- **X-axis**: The categorical variable.
  
### Heatmap
A heatmap displays the correlation between numeric variables, with colors indicating the strength of the correlation.
- **X-axis and Y-axis**: Numeric variables.

### Area Chart
An area chart is a variation of the line chart where the area under the line is filled with color to emphasize the magnitude of change over time.
- **X-axis**: The categorical or time-based variable.
- **Y-axis**: The numeric variable.

### Stacked Bar Chart
A stacked bar chart represents multiple data series stacked on top of each other, which helps visualize the part-to-whole relationship.
- **X-axis**: The categorical variable.
- **Y-axis**: Numeric values of different categories stacked on top of each other.

### Violin Plot
A violin plot is similar to a box plot, but it also shows the distribution density of the data. It is particularly useful for visualizing the distribution of numeric variables across different categories.
- **X-axis**: The categorical variable.
- **Y-axis**: The numeric variable.

---


## Project Structure
- DataView/
- ├── app.py                  # Main Streamlit app file
- ├── requirements.txt        # List of dependencies
- ├── README.md               # Documentation


## Conclusion

This app serves as a powerful tool for **data analysis and visualization** by enabling users to upload datasets, explore the data through various chart types, and gain insights into the data. The app is flexible and can handle both categorical and numeric data types, providing visualizations like bar charts, histograms, heatmaps, and more. The inclusion of chart download options and the history of previous charts makes this app an excellent tool for interactive data exploration.
