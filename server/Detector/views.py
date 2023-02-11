from django.shortcuts import render,redirect
# Create your views here.
from .models import Xrays
import json

## For Prediction
import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image

model = torchvision.models.resnet152(pretrained=False)
model.fc = torch.nn.Linear(2048,4)
model.load_state_dict(torch.load('../server/xyz_epoch_1.pt',map_location ='cpu'))
model.eval()


def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'pages/homepage.html')
    else:
        return redirect('login')


def uploadXray(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'pages/uploadPrescription.html')
        elif request.method == 'POST':
            image = request.FILES['xray_image']
            # print(request.POST['toSave'])
            try : 
                toSave = request.POST['toSave']
            except:
                toSave = False
            
            print(toSave)
            obj = Xrays(uploadedBy = request.user, image = image)
            obj.result = predictXray(obj)
            if toSave : 
                obj.save()
            return redirect('singleView', xray_id=obj.id)
    else:
        return redirect('login')

def singleView(request,xray_id):
    if request.user.is_authenticated:
        context = {
            'xray': Xrays.objects.get(id=xray_id) 
        }

        return render(request, 'pages/singleView.html', context=context)
    else:
        return redirect('login')


def viewAllXrays(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            obj = Xrays.objects.all()
            context = {
                'Xrays' : obj
            }
            
            return render(request, 'pages/viewPrescription.html', context=context)
    else:
        return redirect('login')


def deleteXray(request, xray_id):
    if request.user.is_authenticated:
        xray = Xrays.objects.get(id=xray_id)
        if request.user == xray.uploadedBy:
            xray.delete()
        return redirect( "homepage")
    else:
        return redirect('login')

classes = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
def predictXray(xray):
    img = Image.open(xray.image).convert('RGB')
    trans = transforms.Compose([transforms.ToTensor()])
    transimg = trans(img)
    with torch.no_grad():
        output = model(transimg.unsqueeze(0))
    return classes[torch.argmax(output).item()]