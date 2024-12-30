import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
             
# Set the title of the app
st.title("DataView - Advanced Data Analysis and Visualization")
  
# Upload the dataset
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

# Initialize a session state to store history if it doesn't exist
if 'history' not in st.session_state:
    st.session_state.history = []
    
def save_plot(fig, format='png'):
    buf = BytesIO()
    fig.savefig(buf, format=format)
    buf.seek(0)
    return buf

if uploaded_file is not None:
    try:
        # Check if the uploaded file is a CSV or Excel file
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("## Dataset")
        st.write(df.head())

        # Dropdown for selecting the type of chart
        chart_type = st.selectbox("Select the type of chart", [
            "Bar Chart",
            "Pie Chart",
            "Line Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Heatmap",
            "Area Chart",
            "Stacked Bar Chart",
            "Violin Plot"
        ])

        # Select columns for the X and Y axis where applicable
        columns = df.columns.tolist()
        x_column = st.selectbox("Select the X-axis column", columns)
        y_column = None
        if chart_type not in ["Pie Chart", "Histogram", "Box Plot", "Heatmap", "Violin Plot"]:
            y_column = st.selectbox("Select the Y-axis column", columns)

        # Generate the chart when the button is clicked
        if st.button("Generate Chart"):
            fig, ax = plt.subplots(figsize=(10, 6))

            if chart_type == "Bar Chart":
                sns.barplot(x=df[x_column], y=df[y_column], ax=ax, palette="Set2")
                ax.set_title(f"Bar Chart of {x_column} vs {y_column}")

            elif chart_type == "Pie Chart":
                colors = sns.color_palette("pastel", len(df[x_column].value_counts()))
                ax.pie(df[x_column].value_counts(), 
                       labels=df[x_column].value_counts().index, 
                       autopct='%1.1f%%', 
                       colors=colors)
                ax.set_title(f"Pie Chart of {x_column}")

            elif chart_type == "Line Chart":
                sns.lineplot(x=df[x_column], y=df[y_column], ax=ax, palette="tab10")
                ax.set_title(f"Line Chart of {x_column} vs {y_column}")

            elif chart_type == "Scatter Plot":
                sns.scatterplot(x=df[x_column], y=df[y_column], ax=ax, palette="viridis")
                ax.set_title(f"Scatter Plot of {x_column} vs {y_column}")

            elif chart_type == "Histogram":
                sns.histplot(df[x_column], kde=True, bins=30, ax=ax, color="dodgerblue")
                ax.set_title(f"Histogram of {x_column}")

            elif chart_type == "Box Plot":
                sns.boxplot(x=df[x_column], ax=ax, palette="muted")
                ax.set_title(f"Box Plot of {x_column}")

            elif chart_type == "Heatmap":
                if df.select_dtypes(include=['number']).shape[1] > 1:
                    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
                    ax.set_title("Heatmap of Correlations")
                else:
                    st.error("Heatmap requires at least two numeric columns.")

            elif chart_type == "Area Chart":
                df.groupby(x_column).sum().plot(kind='area', ax=ax, color=sns.color_palette("tab20"))
                ax.set_title(f"Area Chart of {x_column}")

            elif chart_type == "Stacked Bar Chart":
                df.groupby(x_column).sum().plot(kind='bar', stacked=True, ax=ax, color=sns.color_palette("pastel"))
                ax.set_title(f"Stacked Bar Chart of {x_column}")

            elif chart_type == "Violin Plot":
                sns.violinplot(x=df[x_column], ax=ax, palette="Set3")
                ax.set_title(f"Violin Plot of {x_column}")

            # Display the chart
            st.pyplot(fig)

            # Save the figure in history
            st.session_state.history.append(fig)

            # Download buttons
            st.write("### Download the chart")
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download as PNG",
                    data=save_plot(fig, format='png'),
                    file_name="chart.png",
                    mime="image/png"
                )
            with col2:
                st.download_button(
                    label="Download as PDF",
                    data=save_plot(fig, format='pdf'),
                    file_name="chart.pdf",
                    mime="application/pdf"
                )

        # Show history of previously generated charts
        if st.session_state.history:
            st.write("### Previously Generated Charts")
            for i, previous_fig in enumerate(st.session_state.history):
                st.write(f"Chart {i+1}")
                st.pyplot(previous_fig)

    except Exception as e:
        st.error(f"Error: {e}")
