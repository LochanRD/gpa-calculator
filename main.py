import streamlit as st
from PIL import Image

st.title("Calculate your 'What if?' GPA!")

st.subheader("Enter your current GPA and credits taken:", divider='gray')

# col1, col2 = st.columns(2)

current_gpa = None
current_credits = None

current_gpa = st.number_input("Grade", min_value=0.00, max_value=5.0, step=0.01)
current_credits = st.number_input("Credits", min_value=0.0, step=0.5)

summed_weights = current_gpa * current_credits
if current_credits >= 1:

    st.subheader("Add your 'What if?' grades and credits:", divider='gray')

    classes_to_add = st.number_input("How many classes would you like to add?", min_value=0, step=1)

    # for i in range(classes_to_add):
    #     grade = st.number_input(f"Grade {i + 1}", min_value=0.00, max_value=5.0, step=0.01)
    #     credits = st.number_input(f"Credits {i + 1}", min_value=0, step=1)
    #     summed_weights += grade * credits

    col1, col2 = st.columns(2)
    added_grades = []
    added_credits = []

    with col1:
        for i in range(classes_to_add):
            grade = st.number_input(f"Grade {i + 1}", min_value=0, max_value=5, step=1, value=4)
            added_grades.append(grade)
    with col2:
        for i in range(classes_to_add):
            credit = st.number_input(f"Credit {i + 1}", min_value=0.0, step=0.5, value=1.0)
            added_credits.append(credit)

    new_summed_weights = 0
    summed_credits = sum(added_credits)
    for i in range(len(added_grades)):
        new_summed_weights += added_grades[i] * added_credits[i]
    
    total_summed_weights = summed_weights + new_summed_weights
    new_gpa = total_summed_weights / (current_credits + summed_credits)

    out_string = f"Your new GPA is: {new_gpa:.3f}"
    st.header(out_string)
    # st.header(f"Your new total credits are: {current_credits + summed_credits}")
    # st.header(f"Your new added credits are: {summed_credits}")
    # st.header(f"Your old total grades are: {summed_weights}")
    # st.header(f"Your new total grades are: {new_summed_weights}")
    # st.header(f"Your new added grades are: {summed_grades}")