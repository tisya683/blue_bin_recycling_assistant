# SG blue bin recycling assistant

<img width="830" height="469" alt="image" src="https://github.com/user-attachments/assets/71ce8dec-c246-434e-bedf-ad6e0e223e3e" />

I started this project because I'm always second-guessing what actually goes into the blue commingled recycling bins found around across all housing estates Singapore. Unlike countries where recyclables are separated by material, these blue bins allow you to throw paper, plastic, glass, and metal into the same bin. However, there are quite a few exceptions that make things confusing.

For example, even though plastics are generally recyclable, small plastic items like straws and flimsy plastics like plastic bags can't be placed in the blue recycling bin. Because different materials are collected in the same bin, you have to remember the recycling rules for paper, plastic, glass, and metal all at once, including the exceptions for each material. I often found myself checking the recycling guidelines just to figure out whether something could be recycled before throwing it in and the guidelines pasted on the blue bins aren't comprehensive enough.

To make this process easier, I built this simple Gradio demo app. Users can upload a picture of an item using either their webcam or a local image. The app first identifies the item using a convolutional neural network before passing the prediction through a rule-based engine containing the exceptions specific to Singapore's blue recycling bins.It then tells you if you can or cannot recycle it in the blue bins.

## Table of Contents
- Dataset Used
- Installation
- How to Use
- Overview of Project
- Areas for Improvement
- Tech Stack 

## Dataset Used

I used the Recylcable and Household Waste Classification Dataset on Kaggle: https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification

It contains 15,00 recyclable and household waste images across 6 categories and 30 distinct subcategories.Each subcategory has 500 images and its split into 250 images for studio quality and 250 images for default quality.

These are following waste categories and subcategories it covers:
Plastic: water bottles, soda bottles, detergent bottles, shopping bags, trash bags, food containers, disposable cutlery, straws, cup lids
Paper and Cardboard: newspaper, office paper, magazines, cardboard boxes, cardboard packaging
Glass: beverage bottles, food jars, cosmetic containers
Metal: aluminum soda cans, aluminum food cans, steel food cans, aerosol cans
Organic Waste: food waste (fruit peels, vegetable scraps), eggshells, coffee grounds, tea bags
Textiles: clothing, shoes

## Installation
1. Clone this Repo
2. Install requirements.txt
3. Run app.py
4. Open the Gradio URL displayed in your terminal to start using the app

## How to Use
1. Upload an image of the item you want to recycle using either your webcam or a local image
2. Click the checkboxes to answer the questions based on the item's condition (clean,dry,rigid)
3. Click the orange 'Classify' button
4. The app will identify the item's subcategory,category and whether its recyclable or not based on the built-in rule engine.

## Overview of Project

I first started out with building a custom CNN from scratch using TensorFlow and Keras to classify the 30 household items. 


<img width="579" height="439" alt="image" src="https://github.com/user-attachments/assets/29a3366e-1eb7-41a6-a036-e2aaef27ac09" />

<img width="832" height="403" alt="image" src="https://github.com/user-attachments/assets/24dfdc7f-02c4-4eb9-a383-d1e998a8eb65" />


However it only had an accuracy of 52% which makes it comparable to random guessing. However,this can be attributed to insufficient labeled data. 
Each category (e.g., plastic bottle) has only 500 images, which is not enough for a deep learning network to make accurate predictions. 
Transfer learning models are a suitable alternative, as they perform better on smaller labeled datasets.

In the next part, MobileNetV2 was selected because it providees a good balance between computational efficiency and predictive performance. 
Compared with training a CNN from scratch, MobileNetV2 leverages features learned from the large-scale ImageNet dataset, allowing it to achieve higher accuracy with less training data.

<img width="564" height="437" alt="image" src="https://github.com/user-attachments/assets/569a241b-6004-49d9-9bbf-ac2d774ead3b" />


<img width="824" height="367" alt="image" src="https://github.com/user-attachments/assets/d14d825f-42bf-421f-9346-c9b6fc026e42" />



After training, the MobileNetV2 model was evaluated on the test set, achieving a test accuracy of 71.29%. The model and evaluation metrics were logged using MLflow to facilitate experiment tracking and model comparison.
The best-performing model was then deployed in the Gradio application.

Next would be creating the rule engine. I referred to this article (https://www.channelnewsasia.com/singapore/what-can-be-recycled-plastic-paper-glass-metal-recycling-bin-box-tips-nea-3100521) and streamlined
the rules to just 3:
1. Is it clean?
2. Is it dry?
3. Is it rigid?

These three conditions allow the rule engine to determine whether a predicted item should be placed in Singapore's blue recycling bin while accounting for common exceptions. 
Finally, I used the Gradio documentation to build a simple interface that allows users to upload an image via webcam or file upload and receive an instant recycling recommendation.

## Areas for Improvement


<img width="2143" height="1093" alt="image" src="https://github.com/user-attachments/assets/6e5ad20e-21f8-474f-bf92-01dbb930bf78" />


One limitation of the application is the limited number of object categories in the training dataset. For instance, because the dataset does not contain a plastic cup class, the model predicts the closest available class (plastic cup lid), which is subsequently classified as non-recyclable by the rule engine. Increasing the diversity and number of training categories would enable the model to better distinguish between visually similar objects and improve the accuracy of recycling decisions.



## Tech Stack
- **Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **Computer Vision:** MobileNetV2, OpenCV
- **Experiment Tracking:** MLflow
- **Data Processing:** Pandas, NumPy
- **Image Processing:** Pillow
- **Machine Learning:** Scikit-learn
- **Frontend:** Gradio
- **Version Control:** Git, GitHub



























