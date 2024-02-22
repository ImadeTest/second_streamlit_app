import streamlit
import snowflake.connector 
import pandas 

streamlit.title('Zena s Amazing Athleisure Catalog')


#connexion à snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#selctionner un tablea de la base de données et la mettre dans une variable nommée ici "my_catalog"
my_cur.execute("SELECT color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

#mettre les données dans un dataframe 
df = pandas.Dataframe(my_catalog)

#ecriture des données pour voir avec quoi je travaille 
streamlit.write(df)

#mettre la premiere colonne dans une liste
color_list = df[0].values.tolist()


option = streamlit.selectbox('Pick a sweatsuit color or stylr:' , list(color_list))

product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where
color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption= product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])

