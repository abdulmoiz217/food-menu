import streamlit as st

st.title("Food Menu and Price App")
st.subheader("made by moiz s/o shabbir hussain")
st.text("Welcome to my mini food world!")

options = st.sidebar.radio("Options", ["home", "menu", "contact"])

if options == "home":
    st.image("https://up.yimg.com/ib/th/id/OIP.z_ilCv9sIs4AnOpF_9GB5AHaEo?pid=Api&rs=1&c=1&qlt=95&w=154&h=96", width=500)
    st.text("Price: 1100")
    st.image("https://up.yimg.com/ib/th/id/OIP.uPJNhmsCGP72JL72DmMLfwHaE8?pid=Api&rs=1&c=1&qlt=95&w=182&h=121", width=500)
    st.text("Price: 599")
    st.image("https://up.yimg.com/ib/th/id/OIP.OuaoiMa79RwKFM9HajdagwHaFP?pid=Api&rs=1&c=1&qlt=95&w=145&h=103", width=500)
    st.text("Price: 700")
    st.text("Go to menu option to order these items")

elif options == "menu":
    pizza, burger, sandwich = st.columns(3)

    with pizza:
        st.image("https://up.yimg.com/ib/th/id/OIP.z_ilCv9sIs4AnOpF_9GB5AHaEo?pid=Api&rs=1&c=1&qlt=95&w=154&h=96")
        st.text("Item name: Pizza")
        st.text("Item price: 1200")
        pizza_cart = st.button("Add to Cart", key="pizza_cart")
        if pizza_cart:
            st.success("You successfully added Pizza to your cart!")

    with burger:
        st.image("https://up.yimg.com/ib/th/id/OIP.uPJNhmsCGP72JL72DmMLfwHaE8?pid=Api&rs=1&c=1&qlt=95&w=182&h=121")
        st.text("Item name: Burger")
        st.text("Item price: 600")
        burger_cart = st.button("Add to Cart", key="burger_cart")
        if burger_cart:
            st.success("You successfully added Burger to your cart!")

    with sandwich:
        st.image("https://up.yimg.com/ib/th/id/OIP.OuaoiMa79RwKFM9HajdagwHaFP?pid=Api&rs=1&c=1&qlt=95&w=145&h=103")
        st.text("Item name: Sandwich")
        st.text("Item price: 700")
        sandwich_cart = st.button("Add to Cart", key="sandwich_cart")
        if sandwich_cart:
            st.success("You successfully added Sandwich to your cart!")
elif options == "contact":
    st.text_input("enter your name here")
    st.text_input("enter your number")
    submit_button = st.button("submit")
    if submit_button:
        st.success("we contact you soon!")
    