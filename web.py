import streamlit as st
import functions as fu

todos = fu.get_todos()

def add_todo():
    #st.session_state is omdat: soort dictionay type van streamlit
    # beneden zoeken we de waarden van key new_todo.
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fu.write_todos(todos)

st.title("My Todo App")
st.write("This is my first webapp")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        fu.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a new To Do:", placeholder="Add it here",
              on_change=add_todo, key="new_todo")
