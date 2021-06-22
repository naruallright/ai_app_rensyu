from django.shortcuts import render

# Create your views here.

from django.http  import HttpResponse
import pandas as pd
import pickle

category_data = pd.read_csv('catelist.csv')
idx2category = {row.key: row.cate_name for idx, row in category_data.iterrows()}

with open('ai_app.pickle', mode='rb') as f:
    model = pickle.load(f)

def index(request):
    if request.method == 'GET':
       return render(
        request,
        'nlp/home.html'
        )
    else:
        title = [request.POST['title']]
        print(title)
        result = model.predict(title)[0]
        print(result)
        pred = idx2category[result]
        return render(
            request,
            'nlp/home.html',
            {'title' : pred}
    )