# -*- coding: utf-8 -*-
import streamlit as st 
import pickle
import pandas as pd

st.markdown(
   f'<p style="color:{"#4285F4"}; font-size:40px;"><strong>FLIGHT PRICE PREDICTOR</strong></p>',

   unsafe_allow_html=True)

#st.header("Flight price Predictor")
import datetime
cont1 = st.container()
curr_data = datetime.datetime.today()
year1 = curr_data.year
m1 = curr_data.month
d1= curr_data.day
cont1.header("Departure Date")
start_date = cont1.date_input('')

Journey_day = start_date.strftime("%d")
Journey_month = start_date.strftime("%m")
year2 = start_date.strftime("%Y")


if year1==int(year2):
    if int(Journey_month)<m1:
        st.error("Please Enter Future Date")
        exit(0)
    if int(Journey_month)==m1:
        if d1>int(Journey_day):
            st.error("Please Enter Future Date")
            exit(0)
elif year1>int(year2):
     st.error("Please Enter Future Date")
     exit(0)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
st.header("Departure Time")
col1,col2 = st.columns(2)
Dep_hour = col1.selectbox("Departure Hour",[i for i in range(0,24)])

Dep_min = col2.selectbox("Departure Minute",[i for i in range(0,60)])
if Dep_hour>=12:
    s = "Departure time is "+str(Dep_hour-12)+":"+str(Dep_min)+" P.M."
    st.info(s)
else:
    s = "Departure time is "+str(Dep_hour)+":"+str(Dep_min)+" A.M."
    st.info(s)
st.header("Arrival date")
arr_date = st.date_input(' ')

Journey_day1 = arr_date.strftime("%d")
Journey_month1 = arr_date.strftime("%m")
year3 = arr_date.strftime("%Y")
if int(year3)==int(year2):
    if int(Journey_month)>int(Journey_month1):
        st.error("Please Enter Future Date")
        exit(0)
    if int(Journey_month)==int(Journey_month1):
        if int(Journey_day1)<int(Journey_day):
            st.error("Please Enter Future Date")
            exit(0)
elif int(year3)<int(year2):
     st.error("Please Enter Future Date")
     exit(0)


        # Arrival
st.header("Arrival Time")
c1,c2=st.columns(2)
Arrival_hour = c1.selectbox("Arrival Hour",[i for i in range(0,24)])

Arrival_min = c2.selectbox("Arrival Minute",[i for i in range(0,60)])

if Arrival_hour>=12:
    s = "Arrival time is "+str(Arrival_hour-12)+":"+str(Arrival_min)+" P.M."
    st.info(s)
else:
    s = "Arrival time is "+str(Arrival_hour)+":"+str(Arrival_min)+" A.M."
    st.info(s)
        # print("Arrival : ", Arrival_hour, Arrival_min)
        # Duration
time = arr_date-start_date

sec = time.seconds
hours = sec/3600
minutes= sec/60

dur_hour = hours+abs(Arrival_hour%12 - Dep_hour%12)
dur_min = minutes+abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
st.header("Stops")
Total_stops = st.selectbox("",[0,1,2,3,4])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
st.header("Airways")
airline=st.selectbox("",['Choose','Jet Airways','Indigo','Air India','Multiple carriers','SpiceJet','Vistara','GoAir','Multiple carriers Premium economy','Jet Airways Business','Vistara Premium economy','Trujet','Air Asia'])
if(airline=='Jet Airways'):
    Jet_Airways = 1
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 

elif (airline=='IndiGo'):
    Jet_Airways = 0
    IndiGo = 1
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 

elif (airline=='Air India'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 1
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 
            
elif (airline=='Multiple carriers'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 1
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 
            
elif (airline=='SpiceJet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 1
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0 
            
elif (airline=='Vistara'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 1
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='GoAir'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 1
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='Multiple carriers Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 1
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='Jet Airways Business'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 1
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline=='Vistara Premium economy'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 1
    Trujet = 0
            
elif (airline=='Trujet'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 1

else:
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 0
    GoAir =0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
st.header("Departure City")
Source = st.selectbox("",['Choose','Delhi','Kolkata','Mumbai','Chennai','Bangalore'])
if (Source == 'Delhi'):
    s_Delhi = 1
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0

elif (Source == 'Kolkata'):
    s_Delhi = 0
    s_Kolkata = 1
    s_Mumbai = 0
    s_Chennai = 0

elif (Source == 'Mumbai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 1
    s_Chennai = 0

elif (Source == 'Chennai'):
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 1

else:
    s_Delhi = 0
    s_Kolkata = 0
    s_Mumbai = 0
    s_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
st.header("Destination")
Source = st.selectbox("",['Choose','Cochin','Delhi','Chennai','Hyderabad','Kolkata','Bangalore'])
if (Source == 'Cochin'):
    d_Cochin = 1
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0
        
elif (Source == 'Delhi'):
    d_Cochin = 0
    d_Delhi = 1
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Source == 'Chennai'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 1
    d_Hyderabad = 0
    d_Kolkata = 0

elif (Source == 'Hyderabad'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 1
    d_Kolkata = 0

elif (Source == 'Kolkata'):
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 1

else:
    d_Cochin = 0
    d_Delhi = 0
    d_New_Delhi = 0
    d_Hyderabad = 0
    d_Kolkata = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
    
p=0
model = open('flight_rf(1).pkl','rb')
forest = pickle.load(model)
prediction=forest.predict([[
    Total_stops,
    Journey_day,
    Journey_month,
    Dep_hour,
    Dep_min,
    Arrival_hour,
    Arrival_min,
    dur_hour,
    dur_min,
    Air_India,
    GoAir,
    IndiGo,
    Jet_Airways,
    Jet_Airways_Business,
    Multiple_carriers,
    Multiple_carriers_Premium_economy,
    SpiceJet,
    Trujet,
    Vistara,
    Vistara_Premium_economy,
    s_Chennai,
    s_Delhi,
    s_Kolkata,
    s_Mumbai,
    d_Cochin,
    d_Delhi,
    d_Hyderabad,
    d_Kolkata,
    d_New_Delhi
     ]])
p = prediction[0]
s = "Price of your flight is "+str(round(p,2));
st.success(s)
