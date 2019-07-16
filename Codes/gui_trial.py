import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
import tkinter as tk 
import statsmodels.api as sm
import sys
import os
import csv
#import InputList as il
import store_csv_read as ti
import scrape_tagify as st
import down_cloud as dc
import send_email as se
import modelling1 as md



youtube_data = pd.read_csv('F:/College_Semesters_study_Material/sem 7/Major_youtube/final/out.csv')

df = DataFrame(youtube_data,columns=['views','likes','dislikes','tag count','comment_count','Description length','title length','http count'])


#df['Description length'].fillna((df['Description length'].mean()), inplace=True)
#df['http count'].fillna((dt['http count'].mean()), inplace=True)

#df = DataFrame(youtube_data,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price']) 

prediction1 = 0

X = df[['tag count','Description length','http count','title length']].astype(float) # here we have 2 input variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['views'].astype(float) # output variable (what we are trying to predict)

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# with statsmodels
X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 


# tkinter GUI
root= tk.Tk() 
 
canvas1 = tk.Canvas(root, width = 1600, height = 1000)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(220, 310, window=label_Intercept)

# with sklearn
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(220, 280, window=label_Coefficients)

# with statsmodels
print_model = model.summary()
label_model = tk.Label(root, text=print_model, justify = 'center', relief = 'solid', bg='LightSkyBlue1')
canvas1.create_window(1000, 250, window=label_model)


# New_tag count label and input box
label12 = tk.Label(root, text=' PERSONALIZED VIDEO ASSISTANCE PROVIDER :: BY MAYUR AND VAIBHAV ')
canvas1.create_window(250, 50, window=label12)

label1 = tk.Label(root, text='Type Tag Count: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(320, 100, window=entry1)

# New_Description label and input box
label2 = tk.Label(root, text='Type Description Length: ')
canvas1.create_window(100, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(320, 120, window=entry2)

# New_link counts label and input box
label3 = tk.Label(root, text='Type link counts in description: ')
canvas1.create_window(100, 140, window=label3)

entry3 = tk.Entry (root) # create 3rd entry box
canvas1.create_window(320, 140, window=entry3)

# New_title length label and input box
label4 = tk.Label(root, text='title length: ')
canvas1.create_window(100, 160, window=label4)

entry4 = tk.Entry (root) # create 4th entry box
canvas1.create_window(320, 160, window=entry4)

label5 = tk.Label(root, text='Impact Ratio Of Tags')
canvas1.create_window(300, 360, window=label5)

label6 = tk.Label(root, text='Updated Predicted Views')
canvas1.create_window(500, 360, window=label6)

label10 = tk.Label(root, text='Trending Rate')
canvas1.create_window(1000, 800, window=label10)

label11 = tk.Label(root, text='Deacy Rate')
canvas1.create_window(1300, 800, window=label11)

# New_domain input label and input box
label7 = tk.Label(root, text='Enter Domain Name for suggestions from multiple platforms')
canvas1.create_window(190, 500, window=label7)

entry7 = tk.Entry (root) # create 7th entry box
canvas1.create_window(460, 500, window=entry7)

# New_email input label and input box
label8 = tk.Label(root, text='Enter Email ID: ')
canvas1.create_window(190, 800, window=label8)

entry8 = tk.Entry (root) # create 7th entry box
canvas1.create_window(320, 800, window=entry8)



def values(): 
    global New_tag_count #my 1st input variable
    New_tag_count = float(entry1.get()) 
    
    global New_desc_len #my 2nd input variable
    New_desc_len = float(entry2.get()) 

    global New_links #my 3rd input variable
    New_links = float(entry3.get()) 

    global New_title #my 4th input variable
    New_title = float(entry4.get()) 
    
    Prediction_result  = ('Predicted Views: ', regr.predict([[New_tag_count ,New_desc_len ,New_links ,New_title]]))
    global prediction1
    prediction1 = (Prediction_result[1].astype(int))  #integer value of predicted views
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(320, 200, window=label_Prediction)
    
    
def inplist():
    os.system('trial_call_insta_tag.py')
    tag_impact_ratio = ti.read_csv()
    global prediction1
    print(tag_impact_ratio)
    prediction1 = (prediction1*tag_impact_ratio) + prediction1
    print(prediction1)
    
    Prediction_tag_effect = tk.Label(root, text= tag_impact_ratio, bg='orange')
    canvas1.create_window(300, 400, window=Prediction_tag_effect)

    Predicted_views_tags = tk.Label(root, text= prediction1, bg='orange')
    canvas1.create_window(500, 400, window=Predicted_views_tags)
    #tag_list = il.rt_list(tag_list,2)
    #print(tag_list)

def inpdomain():
    global p_list1 
    global p_list2
    global New_enter_domain #my 7th input variable
    New_enter_domain = str(entry7.get())
    print(type(New_enter_domain))
    p_list1 = st.func1(New_enter_domain)
    p_list2 = st.func2(New_enter_domain)
    dc.cloud_fetch(New_enter_domain)

    label8 = tk.Label(root, text='Right now most popular hashtags')
    canvas1.create_window(750, 550, window=label8)
    suggested_hashtags = tk.Label(root, text= p_list1, bg='orange')
    canvas1.create_window(750, 600, window=suggested_hashtags)

    label9 = tk.Label(root, text='Top 10 trending hashtags from- FACEBOOK, TWITTER, INSTAGRAM, TUMBLR')
    canvas1.create_window(750, 670, window=label9)
    suggested_hashtags1 = tk.Label(root, text= p_list2, bg='orange')
    canvas1.create_window(750, 700, window=suggested_hashtags1)
    
def E_mail():
    global New_enter_email #my 8th input variable
    New_enter_email = str(entry8.get())
    with open('email_report.txt', 'w') as f:
        f.write("\nPredicted View counts are:")
        f.write("%s" % prediction1)
        f.write("\nMost popular hashtags:")
        for item in p_list1:
            f.write("%s" % item)
        f.write("\nTop 10 hashtags with their percentages:")
        for item in p_list2:
            f.write("%s" % item)
    se.send_it(New_enter_email)

def rac_model():
    result_value = []
    domain_name = str(entry7.get())
    result_value = md.modelling_fetch(domain_name)
    #print(result_value[0])
    modelling_alpha = tk.Label(root, text= result_value[0], bg='orange')
    canvas1.create_window(1100, 800, window=modelling_alpha)

    modelling_beta = tk.Label(root, text=result_value[1], bg='orange')
    canvas1.create_window(1400, 800, window=modelling_beta)
    
    
    

button1 = tk.Button (root, text='Predict Views',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(100, 200, window=button1)
#---------------------------
button2 = tk.Button (root, text='Enter Tag List',command=inplist, bg='orange') # button to call the 'inplist' command above 
canvas1.create_window(100, 400, window=button2)
#---------------------------
button3 = tk.Button (root, text='Recommendations',command=inpdomain, bg='orange') # button to call the 'inpdomain' command above 
canvas1.create_window(620, 500, window=button3)
#---------------------------
button4 = tk.Button (root, text='Email Me Report',command=E_mail, bg='orange') # button to call the 'E_mail' command above 
canvas1.create_window(500, 800, window=button4)
#---------------------------
button5 = tk.Button (root, text='RAC modelling',command=rac_model, bg='orange') # button to call the 'rac_model' command above 
canvas1.create_window(800, 800, window=button5)


root.mainloop()

