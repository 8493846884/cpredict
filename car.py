from email.mime import image
import pickle

import streamlit as st

model = pickle.load(open('RF_price_predicting_model.pkl','rb'))

def main():
    string = "Car Price Predictor"
    st.set_page_config(page_title=string, ) 
    st.title("Car Price Predictor ")
    
    st.image(
            "https://th.bing.com/th/id/R.b4fd39c2ef7e0c4d3f5ff0eef93c35cd?rik=549Dl62U54j0Jg&riu=http%3a%2f%2fwallup.net%2fwp-content%2fuploads%2f2017%2f03%2f28%2f439209-vehicle-sports_car-German_cars-car-Mercedes-Benz.jpg&ehk=98%2fU11o1wXs2B1%2bsqpOtHbHgRpRCPTcYE135vC7Dr1A%3d&risl=&pid=ImgRaw&r=0",
            width=400, # Manually Adjust the width of the image as per requirement
        )
  
    
    st.write('')
    st.write('')
    years = st.number_input('In which year car was purchased ?',1990, 2021, step=1, key ='year')
    Years_old = 2021-years

    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

    Owner = st.radio("The number of owners the car had previously ?", (0, 1,2, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0	

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    main()
