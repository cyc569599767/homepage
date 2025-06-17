import streamlit as st

st.set_page_config(layout="wide", page_title="统一管理平台",
                   page_icon=":material/toys:",)


login_page = st.Page("login.py", title="Log in",
                     icon=":material/login:")

                     
# 创建一个登录界面
def login():
    st.title("登录")
    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")
    if st.button("登录"):
        if username == "admin" and password == "123456":
            st.success("登录成功！")
            return True
        else:
            st.error("用户名或密码错误！")
            return False


# 不需要注册界面

# 创建一个主界面
def main():
    st.title("主界面")
    st.write("欢迎使用本系统！")


# 主函数
def main1():
    if login():
        main()


if __name__ == '__main__':
    main1()