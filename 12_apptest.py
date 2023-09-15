import streamlit as st
import pandas as pd
import datetime

# Set page configuration
st.set_page_config(layout="wide")

# Create exercise log dataframe
exercise_log = pd.DataFrame(columns=["Date", "Exercise", "Duration (minutes)", "Calories Burned"])

# Create goals dictionary
goals = {
    "Steps": 10000,
    "Calories": 2000,
    "Water": 8
}

# Title and sidebar
st.title("Health and Fitness Tracker")

st.sidebar.header("Set Goals")
goal_steps = st.sidebar.number_input("Daily Steps Goal", value=goals["Steps"])
goal_calories = st.sidebar.number_input("Daily Calories Goal", value=goals["Calories"])
goal_water = st.sidebar.number_input("Daily Water Intake Goal (in cups)", value=goals["Water"])

# Add exercise log
st.header("Exercise Log")

exercise_date = st.date_input("Date", datetime.date.today())
exercise_name = st.text_input("Exercise")
exercise_duration = st.number_input("Duration (minutes)")
exercise_calories = st.number_input("Calories Burned")

if st.button("Add Exercise"):
    new_entry = pd.DataFrame({
        "Date": [exercise_date],
        "Exercise": [exercise_name],
        "Duration (minutes)": [exercise_duration],
        "Calories Burned": [exercise_calories]
    })
    exercise_log = pd.concat([exercise_log, new_entry], ignore_index=True)
    st.success("Exercise added successfully!")

st.dataframe(exercise_log)

# Calculate total calories burned
total_calories_burned = exercise_log["Calories Burned"].sum()

# Calculate progress toward goals
progress_steps = 0  # Placeholder value for steps progress
progress_calories = total_calories_burned / goal_calories * 100
progress_water = 0  # Placeholder value for water intake progress

# Display progress
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Steps", f"{progress_steps:.0f}%", f"{total_calories_burned}/{goal_steps}")
with col2:
    st.metric("Calories", f"{progress_calories:.0f}%", f"{total_calories_burned}/{goal_calories}")
with col3:
    st.metric("Water Intake", f"{progress_water:.0f}%", f"0/{goal_water}")

# Show exercise log chart
st.header("Exercise Log Chart")
exercise_chart = exercise_log.set_index("Date")
st.line_chart(exercise_chart["Duration (minutes)"])

# Nutritional Information
st.header("Nutritional Information")

# Example code to display a sample nutritional table
nutritional_data = {
    "Food": ["Apple", "Banana", "Chicken Breast"],
    "Calories": [52, 96, 165],
    "Protein (g)": [0.3, 1.1, 31],
    "Carbs (g)": [14, 23, 0],
    "Fat (g)": [0.2, 0.3, 3.6]
}

nutritional_df = pd.DataFrame(nutritional_data)
st.dataframe(nutritional_df)

# Reminders
st.header("Reminders")

# Example code to display reminders
st.subheader("Drink Water")
st.write("Remember to stay hydrated and drink enough water throughout the day.")

st.subheader("Stretch Breaks")
st.write("Take regular breaks to stretch and move around, especially if you have a sedentary lifestyle.")