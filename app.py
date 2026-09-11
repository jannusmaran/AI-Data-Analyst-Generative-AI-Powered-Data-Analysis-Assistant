import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

from utils.data_analysis import (
    get_dataset_info,
    get_statistics,
    get_missing_values,
    get_categorical_summary
)

from utils.ai_assistant import ask_ai


# Configure Streamlit page
st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)


# Application title
st.title("🤖 AI Data Analyst")

st.write(
    "Upload a CSV or Excel dataset and analyze it using Python and Generative AI."
)


# File uploader
uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)


# Check whether a file was uploaded
if uploaded_file is not None:

    try:

        # Load dataset
        df = load_data(uploaded_file)


        # Display success message
        st.success("Dataset uploaded successfully!")


        # --------------------------------------------------
        # DATASET PREVIEW
        # --------------------------------------------------

        st.header("📄 Dataset Preview")

        st.dataframe(df.head(10))


        # --------------------------------------------------
        # DATASET INFORMATION
        # --------------------------------------------------

        st.header("ℹ️ Dataset Information")

        info = get_dataset_info(df)

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Number of Rows",
                info["Number of Rows"]
            )

        with col2:

            st.metric(
                "Number of Columns",
                info["Number of Columns"]
            )


        st.subheader("Column Names")

        st.write(info["Column Names"])


        st.subheader("Data Types")

        st.json(info["Data Types"])


        # --------------------------------------------------
        # MISSING VALUES
        # --------------------------------------------------

        st.header("🔍 Missing Value Analysis")

        missing_values = get_missing_values(df)

        st.dataframe(
            missing_values.rename(
                "Missing Values"
            )
        )


        # --------------------------------------------------
        # STATISTICS
        # --------------------------------------------------

        st.header("📊 Statistical Summary")

        statistics = get_statistics(df)

        if statistics is not None:

            st.dataframe(statistics)

        else:

            st.info(
                "No numerical columns are available."
            )


        # --------------------------------------------------
        # CATEGORICAL DATA
        # --------------------------------------------------

        st.header("📝 Categorical Data Summary")

        categorical_summary = get_categorical_summary(df)

        if categorical_summary:

            st.json(categorical_summary)

        else:

            st.info(
                "No categorical columns are available."
            )


        # --------------------------------------------------
        # DATA VISUALIZATION
        # --------------------------------------------------

        st.header("📈 Data Visualization")

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()


        categorical_columns = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()


        chart_type = st.selectbox(
            "Select Chart Type",
            [
                "Bar Chart",
                "Line Chart",
                "Scatter Plot",
                "Histogram"
            ]
        )


        if numeric_columns:

            if chart_type == "Histogram":

                selected_column = st.selectbox(
                    "Select Numerical Column",
                    numeric_columns
                )

                fig = px.histogram(
                    df,
                    x=selected_column,
                    title=f"Distribution of {selected_column}"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            elif chart_type == "Scatter Plot":

                x_column = st.selectbox(
                    "Select X-axis",
                    numeric_columns,
                    key="scatter_x"
                )

                y_column = st.selectbox(
                    "Select Y-axis",
                    numeric_columns,
                    key="scatter_y"
                )

                fig = px.scatter(
                    df,
                    x=x_column,
                    y=y_column,
                    title=f"{x_column} vs {y_column}"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            elif chart_type == "Line Chart":

                x_column = st.selectbox(
                    "Select X-axis",
                    df.columns.tolist(),
                    key="line_x"
                )

                y_column = st.selectbox(
                    "Select Y-axis",
                    numeric_columns,
                    key="line_y"
                )

                fig = px.line(
                    df,
                    x=x_column,
                    y=y_column,
                    title=f"{y_column} Trend"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            elif chart_type == "Bar Chart":

                if categorical_columns:

                    x_column = st.selectbox(
                        "Select Category",
                        categorical_columns
                    )

                    y_column = st.selectbox(
                        "Select Numerical Value",
                        numeric_columns
                    )

                    grouped_data = (
                        df.groupby(x_column)[y_column]
                        .mean()
                        .reset_index()
                    )

                    fig = px.bar(
                        grouped_data,
                        x=x_column,
                        y=y_column,
                        title=f"Average {y_column} by {x_column}"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "Bar chart requires categorical columns."
                    )


        # --------------------------------------------------
        # GENERATIVE AI SECTION
        # --------------------------------------------------

        st.header("🤖 Ask AI About Your Data")

        question = st.text_area(
            "Ask any question about your dataset",
            placeholder="Example: Give me the most important insights from this dataset."
        )


        if st.button("Ask AI"):

            if question:

                with st.spinner(
                    "AI is analyzing your dataset..."
                ):

                    answer = ask_ai(
                        df,
                        question
                    )


                st.subheader("💡 AI Analysis")

                st.write(answer)

            else:

                st.warning(
                    "Please enter a question."
                )


    except Exception as e:

        st.error(
            f"An error occurred: {str(e)}"
        )


else:

    st.info(
        "Please upload a CSV or Excel file to start analyzing."
    )