from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd

classifier=""
model = load_model('lightgbmun')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

 

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))


    st.title("Credit Card Fraud Detection App")

    if add_selectbox == 'Online':

        V1 = st.number_input('V1', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V2 = st.number_input('V2', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V3 = st.number_input('V3', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V4 = st.number_input('V4', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V5 = st.number_input('V5', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V6 = st.number_input('V6', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V7 = st.number_input('V7', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V8 = st.number_input('V8', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V9 = st.number_input('V9', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V10 = st.number_input('V10', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V11 = st.number_input('V11', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V12 = st.number_input('V12', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V13 = st.number_input('V13', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V14 = st.number_input('V14', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V15 = st.number_input('V15', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V16 = st.number_input('V16', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V17 = st.number_input('V17', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V18 = st.number_input('V18', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V19 = st.number_input('V19', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V20 = st.number_input('V20', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V21 = st.number_input('V21', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V22 = st.number_input('V22', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V23 = st.number_input('V23', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V24 = st.number_input('V24', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V25 = st.number_input('V25', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V26 = st.number_input('V26', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V27 = st.number_input('V27', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        V28 = st.number_input('V28', min_value=-1000.000000, max_value=1000.000000,step=0.000001,format="%.6f",value=0.000000)
        output=""

        input_dict = {'V1' : V1,'V2' : V2,'V3' : V3,'V4' : V4,'V5' : V5,'V6' : V6,'V7' : V7,'V8' : V8,'V9' : V9,'V10' : V10,'V11' : V11,'V12' : V12,'V13' : V13,'V14' : V14,'V15' : V15,'V16' : V16,'V17' : V17,'V18' : V18,'V19' : V19,'V20' : V20,'V21' : V21,'V22' : V22,'V23' : V23,'V24' : V24,'V25' : V25,'V26' : V26,'V27' : V27,'V28' : V28 }
        input_df = pd.DataFrame([input_dict])


        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)

        st.success('The output is {}'.format(output))
        
    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
    if st.sidebar.checkbox('Visualize the results of different models'):
    
        alg=['Extra Trees','Random Forest','k Nearest Neighbor','Support Vector Machine','Logistic Regression','Xgboost','LDA','QDA','NB','Ada','Lightgbm']
        classifier = st.sidebar.selectbox('Which algorithm?', alg)
        rectifier=['SMOTE','Undersampling']
        imb_rect = st.sidebar.selectbox('Which imbalanced class rectifier?', rectifier) 
    
    if classifier=='Logistic Regression':
        
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
    
        
    elif classifier == 'k Nearest Neighbor':
        
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
            
    
    elif classifier == 'Support Vector Machine':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')   
        
    elif classifier == 'Random Forest':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg') 
            
    elif classifier == 'Extra Trees':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')                  
    elif classifier == 'Xgboost':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
    elif classifier == 'QDA':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
    elif classifier == 'LDA':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
    elif classifier == 'Lightgbm':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
    elif classifier == 'NB':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
    elif classifier == 'Ada':
        if imb_rect=='SMOTE':
            st.image('./hospital.jpg')
        
        elif imb_rect=='Undersampling':
            st.image('./hospital.jpg')
if __name__ == '__main__':
    run()