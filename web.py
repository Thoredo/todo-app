import streamlit as st
import functions

todo_list = functions.get_todo_list()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="Enter a new todo:", placeholder="Enter a new todo...")