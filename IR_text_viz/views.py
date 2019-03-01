from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from IR_text_viz.prep import *
def predictAndVisualize():
    # get the file name and save it somewhere
    # use the prev functions and predict
    # merge with raw text inp file
    pass

def upload(request):
    folder = 'input/'
    # process data
    p = preprocess('input')
    p.process_raw()
    p.getTestData()

    # predict
    testob = Classifier_LSTM('test_data.h5')
    df = testob.predict()
    grouped = df.groupby(['line'])
    data = []
    for l, group in grouped:
        line = {}
        for i, row in group.iterrows():
            line[i] = {
                "class" : row['predict'],
                "text" : row['text_x']
            }
        data.append(line)

    context = {'data': data }
    return render(request, "textViewer.html", context)



    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)


        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')