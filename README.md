# Number Plate Recognition System

Welcome to the **Number Plate Recognition System**! This is a console-based application that leverages machine learning to detect and analyze vehicle number plates from images. The system can identify number plates, extract details, and perform analysis in an easy-to-use interface built with Python.

## Overview

The **Number Plate Recognition System** enables you to extract and analyze number plate information from vehicle images. It uses computer vision and Optical Character Recognition (OCR) techniques to identify text from the number plate in real-time.

### Features

- **Image Upload**: Upload vehicle images for number plate detection.
- **Number Plate Detection**: Automatically detects the number plate from the image.
- **OCR for Text Extraction**: Uses Optical Character Recognition (OCR) to extract the number plate text.
- **Analysis and Validation**: Validate the extracted number plate against pre-defined formats or databases.
- **User-Friendly Console Interface**: Navigate through the application with a simple menu system.
  
## Getting Started

### Prerequisites

- Python 3.x: Make sure Python is installed. You can download it [here](https://www.python.org/downloads/).
- Libraries: This system requires some additional Python libraries. You can install them via pip:

```bash
pip install opencv-python pytesseract numpy imutils
```

### Installation

1. Clone the repository (if applicable) or download the project files.
2. Navigate to the project directory.

### How to Run

You can start the application in two ways:

#### Debug Mode (F5):
- If you're using an IDE like VS Code, press F5 to launch the application in debug mode.

#### Terminal Execution:
- Open a terminal by navigating to `View > Terminal` (or use your preferred terminal).
- Run the following command to start the application:
  
  ```bash
  python src/main.py
  ```

## Usage

Once the application starts, you will see a menu with options to:

1. **Upload an image**: Choose an image file containing a vehicle to analyze.
2. **Detect number plate**: Automatically detect the number plate from the image.
3. **Extract number plate details**: Extract and display the number plate text.
4. **Validate number plate**: Check if the extracted number plate matches a specific format or exists in a predefined database.
5. **Exit the application**: Quit the program.

Simply enter the number corresponding to the action you want to perform.

## Future Enhancements

This number plate recognition system could be extended with additional features, such as:

- **Vehicle Make and Model Detection**: Enhance the system to identify the vehicle make and model.
- **Real-time Video Processing**: Enable the system to process video feeds for real-time number plate recognition.
- **Database Integration**: Link the system to a database for tracking vehicles and related information.
- **Cloud Deployment**: Deploy the system to the cloud to enable access and integration from remote locations.

## License

This project is licensed under the **MIT License**.

Happy coding!
