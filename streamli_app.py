import streamlit 
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗kale, spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# import pandas
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# #fruits_to_show = my_fruit_list.loc[fruits_selected]
# #my_fruit_list = my_fruit_list.set_index('Fruit')
# # Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
# streamlit.dataframe('my_fruit_list')
# # Display the table on the page.
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
streamlit.write('thanks for adding', add_my_fruit)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values (from streamlit')")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains")
streamlit.dataframe(my_data_rows)
















streamlit.text(my_data_row)
