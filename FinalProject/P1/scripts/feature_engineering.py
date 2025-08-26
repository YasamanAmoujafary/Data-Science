import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tensorflow.keras.preprocessing.image import ImageDataGenerator
import logging

logging.basicConfig(filename='training_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def configure_data_augmentation():
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    config = {
        'rotation_range': 20,
        'width_shift_range': 0.2,
        'height_shift_range': 0.2,
        'shear_range': 0.2,
        'zoom_range': 0.2,
        'horizontal_flip': True,
        'fill_mode': 'nearest'
    }
    with open('augmentation_config.txt', 'w') as f:
        for key, value in config.items():
            f.write(f"{key}: {value}\n")
    logging.info("Data augmentation configured and saved to augmentation_config.txt")
    print("Data augmentation configured and saved to augmentation_config.txt")

if __name__ == "__main__":
    configure_data_augmentation()