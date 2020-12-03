
"""
Model for predicion of burnout 
"""

import pickle

def prediction_f(data): 
    
    #polynomial transformation

    
    model = pickle.load(open('rf_model.pkl','rb'))
    rate = model.predict(data)
    rate = abs(round(rate[0],2))

    return rate


def message_f(rate):
    if rate < 0.4:
        prediction = 'All Great! ' 
    
    elif 0.4 <= rate <0.7:
        prediction = 'Your team-mate is working hard, time to relax!'
    
    elif 0.7 <= rate <= 1.0:
        prediction = 'Burn-out risk! Emergency action required.'
    
    else:
         prediction = 'Likely there are troubles ouside of work, talk to your team-mate!'
        
    
    return prediction 