import streamlit as st

st.title("登录")
username = st.text_input("用户名")
password = st.text_input("密码", type="password")
if st.button("登录"):
    if username == "admin" and password == "123456":
        st.success("登录成功！")
    else:
        st.error("用户名或密码错误！")