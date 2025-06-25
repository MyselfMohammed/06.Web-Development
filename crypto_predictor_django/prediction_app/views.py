from django.shortcuts import render
from .forms import CryptoForm
from .predictor import predict_crypto

def index(request):
    prediction = None
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data
            raw_prediction = predict_crypto(input_data)

            # Customize the display message
            if raw_prediction:
                prediction = "📈 Wow !!... Your Returns Will Create a Positive Impact 😎🚀"
            else:
                prediction = "📉 Sooo Sad ... Your Returns Will Create a Negative Impact 😕🔻"
    else:
        form = CryptoForm()
        
    return render(request, 'prediction_app/index.html', {'form': form, 'prediction': prediction})
