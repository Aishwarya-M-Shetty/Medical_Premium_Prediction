from insurance_predictor.pipeline.batch_prediction import start_batch_prediction
from insurance_predictor.pipeline.training_pipeline import start_training_pipeline

file_path=r"/Users/aishwaryashetty/Desktop/Study/Deep_Learning_Module/Medical_Premium_Prediction/insurance.csv"
print(__name__)
if __name__=="__main__":
    try:
        #output_file = start_batch_prediction(input_file_path=file_path)
        output_file = start_training_pipeline()
        print(output_file)
    except Exception as e:
        print(e)