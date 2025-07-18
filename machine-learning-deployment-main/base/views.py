from django.shortcuts import render
import pickle
import numpy as np
from django.http import JsonResponse
import tempfile
import os

def home(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        # Load your ML model (adjust path/filename as needed)
        with open('C:\Users\DELL\Downloads\InternShip_Documentaion\Model\Finalmodel.h5', 'rb') as f:
            model = pickle.load(f)
        
        # Process uploaded audio file
        audio_file = request.FILES['audio_file']
        
        # Save temporarily (in production, use proper file handling)
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            for chunk in audio_file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name
        
        try:
            # Preprocess audio (replace with your actual preprocessing)
            # features = preprocess_audio(tmp_path)
            
            # Mock features - replace with actual feature extraction
            features = np.random.rand(1, 128)  # Example feature vector
            
            # Make prediction
            prediction = model.predict(features)
            confidence = np.max(model.predict_proba(features))
            
            # Get class names (adjust based on your model)
            class_names = ["Bewick's Wren",'Northern Mockingbird','American Robin','Song Sparrow','Northern Cardinal']  
            species = class_names[prediction[0]]
            
            # Clean up
            os.unlink(tmp_path)
            
            # Return results
            context = {
                'status': 'success',
                'species': species,
                'confidence': f"{confidence*100:.2f}%",
                'audio_file': audio_file.name
            }
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse(context)
            return render(request, 'results.html', context)
            
        except Exception as e:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            error_msg = f"Error processing audio: {str(e)}"
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': error_msg}, status=500)
            return render(request, 'home.html', {'error': error_msg})
    
    # GET request - show upload form
    return render(request, 'home.html')


# Example preprocessing function (you'll need to implement your actual audio processing)
def preprocess_audio(file_path):
    """
    Placeholder for actual audio preprocessing
    Should return feature vector compatible with your model
    """
    # This would actually extract MFCCs or other features from the audio
    return np.random.rand(1, 128)  # Replace with real feature extraction