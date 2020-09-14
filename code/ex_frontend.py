from sqlalchemy.orm import sessionmaker
from project_orm import UserInput,Prediction
from sqlalchemy import create_engine
import streamlit as st

engine = create_engine('sqlite:///project_db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title("Using database with sqlalchemy")

area = st.number_input('enter house area in sqft',
                        max_value=1000,
                        min_value=100,
                        value=400)

rooms = st.number_input('enter house area in sqft',
                        max_value=50,
                        min_value=1,
                        value=3)

age = st.number_input('enter house area in sqft',
                        max_value=50,
                        min_value=0,
                        value=1)

location = st.text_area('enter location address')

submit = st.button('make predictions')

if submit and location:
    #st.write('we got input')
    try:
        entry = UserInput(house_area=area, 
                         no_of_rooms=rooms,
                         age=age,
                         location=location)

        sess.add(entry)
        sess.commit()
        st.success('data added to database')

    except Exception as e:
        st.error('something is wrong : {e}')


if st.checkbox('view data'):
    results = sess.query(UserInput).all()
    for item in results:
        st.write(item.location)
        st.write(item.house_area)
        st.write(item.age)
        st.write(item.no_of_rooms)