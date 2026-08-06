import streamlit as st
from datetime import date

st.title("Student Registration Form")
name=st.text_input("Pallavi")
roll=st.text_input("1009")
college=st.text_input("S.S.Jondhale Ambernath(E)")
branch=st.selectbox("Select Branch",["Information Technology"])
year=st.selectbox("Select Year",["Third Year"])
dob=st.date_input("26/10/2005")
gender=st.radio("Select Gender",["Female"])
email=st.text_input("pallavilone62@gmail.com")
mobile=st.text_input("9702792142")
language=st.selectbox("Favourite Language",["Python","SQL","CSS"])
skills=st.multiselect("Select Skills",["Python"])
password=st.text_input("Enter Password",type="password")
submit=st.button("Submit")
if submit:

    today=date.today()
    age=today.year-dob.year

    if(today.month,today.day)<(dob.month,dob.day):
        age-=1
    st.success("Registration Successful")

    st.write("### Student Details")
    st.write("Name:",name)
    st.write("Roll Number:",roll)
    st.write("College:",college)
    st.write("Branch:",branch)
    st.write("Year:",year)
    st.write("Age:",age)
    st.write("Gender:",gender)
    st.write("Email:",email)
    st.write("Mobile:",mobile)
    st.write("Language:",language)
    st.write("Skills:",skills)

    if len(password)>=8:
        st.success("Password is valid")
    else:
        st.error("Password must be at least 8 characters")
st.download_button("Download File",
                   data="Thank You for Registration",
                   file_name="streamlit.txt",
                   mime="text/plain")



