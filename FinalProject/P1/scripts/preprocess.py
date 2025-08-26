import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from scripts.load_data import load_data

logging.basicConfig(filename='training_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_data(db_path='database/DogImages.db'):
    df = load_data(db_path)
    
    if os.getenv('CI') != 'true':
        df['Image_Exists'] = df['Image_File_Path'].apply(os.path.exists)
        missing_count = len(df[~df['Image_Exists']])
        logging.info(f"Missing images: {missing_count}")
        print(f"Missing images: {missing_count}")
        df = df[df['Image_Exists']].reset_index(drop=True)
    else:
        logging.info("Skipping image existence check in CI environment")
        print("Skipping image existence check in CI environment")
    
    if df.empty:
        logging.error("DataFrame is empty after preprocessing")
        raise ValueError("DataFrame is empty after preprocessing")
    
    label_encoder = LabelEncoder()
    df['Label'] = label_encoder.fit_transform(df['Breed'])
    logging.info(f"Breed classes: {list(label_encoder.classes_)}")
    print("Breed classes:", label_encoder.classes_)
    
    train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42, stratify=df['Breed'])
    val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42, stratify=temp_df['Breed'])
    
    train_df = train_df.assign(Set='train')
    val_df = val_df.assign(Set='val')
    test_df = test_df.assign(Set='test')
    
    dataset_df = pd.concat([train_df, val_df, test_df], ignore_index=True)
    
    dataset_df.to_csv('dataset_splits.csv', index=False)
    logging.info("Dataset splits saved to dataset_splits.csv")
    print("Dataset splits saved to dataset_splits.csv")
    
    np.save('y_train.npy', train_df['Label'].values)
    np.save('y_val.npy', val_df['Label'].values)
    np.save('y_test.npy', test_df['Label'].values)
    np.save('label_classes.npy', label_encoder.classes_)
    
    summary = (f"Dataset prepared:\n"
               f"Training set: {len(train_df)} samples\n"
               f"Validation set: {len(val_df)} samples\n"
               f"Test set: {len(test_df)} samples")
    logging.info(summary)
    print(summary)

if __name__ == "__main__":
    preprocess_data()