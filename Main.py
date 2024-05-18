import streamlit as st

def calculate_gpa(total_credits, current_gpa, new_credits, new_gpa):
    total_grade_points = total_credits * current_gpa
    new_grade_points = new_credits * new_gpa
    total_credits_new = total_credits + new_credits
    overall_gpa = (total_grade_points + new_grade_points) / total_credits_new
    return overall_gpa

def main():
    st.title("GPA Calculator")

    st.header("Current GPA and Credits")
    total_credits = st.number_input("Total Completed Credits:", min_value=0, value=0)
    current_gpa = st.number_input("Current GPA:", min_value=0.0, max_value=10.0, value=0.0)

    st.header("New Semester")
    new_credits = st.number_input("New Semester Credits:", min_value=0, value=0)
    new_gpa = st.number_input("New Semester GPA:", min_value=0.0, max_value=10.0, value=0.0)

    if st.button("Calculate Overall GPA"):
        if total_credits == 0:
            st.error("Total completed credits cannot be zero.")
        else:
            overall_gpa = calculate_gpa(total_credits, current_gpa, new_credits, new_gpa)
            st.success(f"Your new overall GPA will be: {overall_gpa:.2f}")

if __name__ == "__main__":
    main()
