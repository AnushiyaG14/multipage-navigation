import streamlit as st

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Top Selling Products", "Year over Year sales Analysis", "Product Performance","Regional Sales Analysis","Discount Analysis"])

# Main App Logic
if page == "Home":
    st.title("Welcome")
    st.write("Business insights of Retail Order Data Analysis  !")
    
elif page == "Top Selling Products":
    st.title("Top Selling Products")
    st.image("/workspaces/multipage-navigation/images/Capture1.PNG","Caption = Top 10 Revenue generating products")
elif page == "Year over Year sales Analysis":
    st.title("Year over Year sales Analysis")
    st.image("/workspaces/multipage-navigation/images/capture2.png", "Caption = Yearly Sales Analysis")
    st.image("/workspaces/multipage-navigation/images/Capture2.PNG","Caption = Monthly sales Analysis ")
elif page == "Product Performance":
    st.title("Product Performance")
    st.image("/workspaces/multipage-navigation/images/Capture1.PNG", "caption = Product rank by Revenue basis")
    st.image()
elif page == "Regional Sales Analysis":
    st.title("Regional Sales Analysis")
    st.image("/workspaces/multipage-navigation/images/Capture3.png","Caption =Regional Sales Analysis ")
elif page == "Discount Analysis":
    st.title("Discount Analysis")
    st.image("/workspaces/multipage-navigation/images/Capture5.PNG","caption = Product with greater than 20 % disscount ")
