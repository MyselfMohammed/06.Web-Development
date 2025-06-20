
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)
from django.core.files.storage import FileSystemStorage

from .import models
from .forms import *

#from topicApp.Topicfun import Topic
#from ckdApp.funckd import ckd
#from sklearn.tree import export_graphviz #plot tree
#from sklearn.metrics import roc_curve, auc #for model evaluation
#from sklearn.metrics import classification_report #for model evaluation
##from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(df2.drop('classification_yes', 1), df2['classification_yes'], test_size = .2, random_state=10)

import time
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

#from sklearn.preprocessing import StandardScaler
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2
#from sklearn.model_selection import train_test_split
#from sklearn.decomposition import PCA
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression

#import eli5 #for purmutation importance
#from eli5.sklearn import PermutationImportance
#import shap #for SHAP values
#from pdpbox import pdp, info_plots #for partial plots

np.random.seed(123) #ensure reproduc

class dataUploadView(View):
    form_class = Concrete_Application
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url = reverse_lazy('fail')
    filenot_url = reverse_lazy('filenot')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Extract data and convert to float
            try:
                data_Cement = float(request.POST.get('Cement'))
                data_Slag = float(request.POST.get('Slag'))
                data_Flyash = float(request.POST.get('Flyash'))
                data_Super_Plasticizer = float(request.POST.get('Super_Plasticizer'))
                data_Coarse_Aggregate = float(request.POST.get('Coarse_Aggregate'))
                data_Fine_Aggregate = float(request.POST.get('Fine_Aggregate'))
                data_Water = float(request.POST.get('Water'))
                data_Curing_Age_in_Days = float(request.POST.get('Curing_Age_in_Days'))
            except ValueError:
                messages.error(request, "Invalid input data type.")
                return redirect(self.failure_url)

            # ✅ Load and process dataset
            dataset = pd.read_csv("concrete.csv", index_col=None)
            indep_X = dataset.iloc[:, 0:8].values
            dep_Y = dataset.iloc[:, -1].values

            # ✅ Split & scale
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler
            X_train, X_test, Y_train, Y_test = train_test_split(indep_X, dep_Y, test_size=0.25, random_state=0)

            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            # ✅ Train model
            from sklearn.ensemble import RandomForestRegressor
            model = RandomForestRegressor(n_estimators=10, random_state=0)
            model.fit(X_train, Y_train)

            # ✅ Make prediction
            input_data = scaler.transform([[data_Cement, data_Slag, data_Flyash, data_Super_Plasticizer,
                                            data_Coarse_Aggregate, data_Fine_Aggregate, data_Water, data_Curing_Age_in_Days]])
            y_pred = model.predict(input_data)[0]  # Get scalar value

            # ✅ Render result
            return render(request, "succ_msg.html", {
                'data_Cement': data_Cement,
                'data_Slag': data_Slag,
                'data_Flyash': data_Flyash,
                'data_Super_Plasticizer': data_Super_Plasticizer,
                'data_Coarse_Aggregate': data_Coarse_Aggregate,
                'data_Fine_Aggregate': data_Fine_Aggregate,
                'data_Water': data_Water,
                'data_Curing_Age_in_Days': data_Curing_Age_in_Days,
                'y_pred': round(y_pred, 2)
            })

        else:
            return redirect(self.failure_url)
