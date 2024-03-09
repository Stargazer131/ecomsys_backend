import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from keras.applications.vgg16 import preprocess_input
from django.core.files.uploadedfile import InMemoryUploadedFile
from keras.applications import VGG16
import pickle
from product.models import Product


def load_and_preprocess_image(image_data):
    if isinstance(image_data, InMemoryUploadedFile):
        image_array = np.frombuffer(image_data.read(), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)       
    
    else:
        image_array = np.fromfile(image_data, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    
    
    image = cv2.resize(image, (224, 224))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    image = preprocess_input(image)  # Normalize pixel values
    return image


def feature_extractor(image_data):
    # Load the pre-trained VGG16 model with weights from ImageNet dataset
    model = VGG16(weights='imagenet', include_top=False)
    preprocessed_image = load_and_preprocess_image(image_data)
    features = model.predict(np.expand_dims(preprocessed_image, axis=0))
    
    # The model (detective) outputs the features (analysis of the image)
    # These features are activations from the convolutional layers
    # They capture the essential visual characteristics learned by VGG16
    return features[0]  # This will show a shape like (1, 7, 7, 512)
    
    
def get_image_features_list(update=False):
    if update:
        image_features = []
        products = Product.objects.all()
        for product in products:
            id = product.id
            image_path = product.image.url
            extracted_features = feature_extractor(image_path[1:])
            image_features.append({
                "id": id,
                "features": extracted_features
            })
        
        with open('search/image_features.pkl', 'wb') as file:
            pickle.dump(image_features, file)
        
    else:
        with open('search/image_features.pkl', 'rb') as file:
            data = pickle.load(file)
        return data


def predict_similar_image(uploaded_image, top_k_neighbors=5):
    knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
    data = get_image_features_list()
    product_features = np.array([item['features'].flatten() for item in data])
    uploaded_features = feature_extractor(uploaded_image)
    
    knn.fit(product_features, np.arange(len(product_features)))
    distances, indexs = knn.kneighbors(uploaded_features.reshape(1, -1), n_neighbors=top_k_neighbors)
    id_list = [data[int(index)]['id'] for index in indexs[0]]
    
    return id_list
