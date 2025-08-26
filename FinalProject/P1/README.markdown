# Dog Breed Classification Data Pipeline

## Overview
This project implements a data pipeline for processing dog breed image metadata (Dalmatian, Golden Retriever, Pug, Rottweiler) stored in an SQLite database (`DogImages.db`). The pipeline loads data, preprocesses it, and configures data augmentation settings for machine learning tasks. The project is developed as part of the Data Science course (Semester 8) by students with IDs 810100207, 810100247, and 810102480.

## Project Structure
- **database/**: Contains the SQLite database (`DogImages.db`).
- **scripts/**: Python scripts for the pipeline.
  - `database_connection.py`: Connects to the SQLite database and loads metadata.
  - `load_data.py`: Queries the database and saves raw data to `raw_data.csv`.
  - `preprocess.py`: Preprocesses data (handles missing images, encodes labels, splits dataset) and saves to `dataset_splits.csv` and `.npy` files.
  - `feature_engineering.py`: Configures data augmentation and saves settings to `augmentation_config.txt`.
  - `import_to_db.py`: Imports data into the SQLite database (used for setup).
- `pipeline.py`: Main script that sequentially executes `load_data.py`, `preprocess.py`, and `feature_engineering.py`.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.
- **Output Files** (generated after running `pipeline.py`):
  - `raw_data.csv`: Raw metadata from the database.
  - `dataset_splits.csv`: Preprocessed dataset with train/val/test splits.
  - `y_train.npy`, `y_val.npy`, `y_test.npy`: Encoded labels for train/val/test sets.
  - `label_classes.npy`: Breed class names.
  - `augmentation_config.txt`: Data augmentation settings.
  - `training_log.log`: Execution logs.

## Prerequisites
- Python 3.10
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```
  Required packages (from `requirements.txt`):
  - pandas==2.2.3
  - numpy==1.26.4
  - scikit-learn==1.5.2
  - tensorflow==2.17.0
  - opencv-python==4.10.0.84

## Setup
1. Clone the repository or unzip the project to a local directory.
2. Ensure `DogImages.db` is in the `database` folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup
- If `DogImages.db` is not provided or needs to be recreated, run:
  ```bash
  python scripts\import_to_db.py
  ```
  This script imports metadata into `DogImages.db` in the `database` folder.

## Running the Pipeline
Execute the data pipeline using:
```bash
python pipeline.py
```

### Expected Output
- **Console**:
  - Messages indicating the execution of each script:
    ```
    Running scripts\load_data.py
    Data loaded from database\DogImages.db with 2000 records
    Raw data saved to raw_data.csv
    Successfully executed scripts\load_data.py
    Running scripts\preprocess.py
    Missing images: 0
    Breed classes: ['Dalmatian' 'Golden Retriever' 'Pug' 'Rottweiler']
    Dataset splits saved to dataset_splits.csv
    Dataset prepared:
    Training set: 1400 samples
    Validation set: 300 samples
    Test set: 300 samples
    Successfully executed scripts\preprocess.py
    Running scripts\feature_engineering.py
    Data augmentation configured and saved to augmentation_config.txt
    Successfully executed scripts\feature_engineering.py
    ```
- **Files**:
  - `raw_data.csv`: Raw metadata (Breed, Image_File_Path).
  - `dataset_splits.csv`: Preprocessed dataset with columns `Breed`, `Image_File_Path`, `Label`, `Set`.
  - `y_train.npy`, `y_val.npy`, `y_test.npy`: Encoded labels.
  - `label_classes.npy`: Breed classes (e.g., `['Dalmatian', 'Golden Retriever', 'Pug', 'Rottweiler']`).
  - `augmentation_config.txt`: Data augmentation settings.
  - `training_log.log`: Execution logs.

## Authors
- Student IDs: 810100207, 810100247, 810102480
- Course: Data Science, Semester 8
- Date: May 2025