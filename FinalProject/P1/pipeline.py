import subprocess
import logging
import os
import sys

logging.basicConfig(filename='training_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    python_exe = sys.executable
    if not os.path.exists(python_exe):
        logging.error(f"Python executable not found: {python_exe}")
        raise FileNotFoundError(f"Python executable not found: {python_exe}")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts = [
        os.path.join(base_dir, 'scripts', 'load_data.py'),
        os.path.join(base_dir, 'scripts', 'preprocess.py'),
        os.path.join(base_dir, 'scripts', 'feature_engineering.py')
    ]
    
    for script in scripts:
        if not os.path.exists(script):
            logging.error(f"Script not found: {script}")
            raise FileNotFoundError(f"Script not found: {script}")
        
        logging.info(f"Running {script}")
        print(f"Running {script}")
        try:
            result = subprocess.run([python_exe, script], check=True)
            logging.info(f"Successfully executed {script}")
            print(f"Successfully executed {script}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to execute {script}: {e}")
            print(f"Failed to execute {script}: {e}")
            raise e

if __name__ == "__main__":
    run_pipeline()