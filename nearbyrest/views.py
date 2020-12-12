from django.shortcuts import render
from restaurant.models import Restaurant,User
import requests,json,geocoder

# current location of user
def Get_Current_Location():
    g = geocoder.ip('me')
    lat=g.lat
    lng=g.lng
    return lat,lng
lat,lng=Get_Current_Location()


#string to string matching restaurants here name =restaurant name
def search(name,near_rest):
    temp=[]
    for val in near_rest:
        if name==val.Restaurant_Name:
            temp.append(val)
    return temp


#using api distance between user and restaurant is caluculated
#returns distances between two co-ordinates in kms.
def get_distances(lon_src,lat_src,lon_dest,lat_dest):
    Authorization="fqhg277wu2l7eije11m79736gbiz5xuv"
    src=str(lon_src)+","+str(lat_src)
    dest=str(lon_dest)+","+str(lat_dest)
    base_url="https://apis.mapmyindia.com/advancedmaps/v1/"+Authorization+"/distance_matrix/driving/"+src+";"+dest+"?"
    val=requests.get(base_url)
    val=val.json()
    dist=val['results']['distances'][0][1]
    return dist/10**3


#limits restaurant range to 5km 
def range_limit(arr):
    temp=[]
    rest_names=[]
    arr=sorted(arr,key=lambda x: x[0])
    for val in arr:
        if val[0]<=15:
            temp.append(val)
            rest_names.append(val[2])
    return temp,rest_names


def NearByRestaurants(request):
    data=Restaurant.objects.all()#gets objects from data base
    temp=[]
    near_rest=[]
    lat,lng=Get_Current_Location()
    if request.method=='GET':
        if request.GET.get('submit')=='mylocation':
            lat=request.GET.get('lat')
            lng=request.GET.get('lon')
   
    for val in data:
        dist=get_distances(lng,lat,val.lon,val.lat)
        temp.append([dist,val.user,val.Restaurant_Name])
    new_data,rest_names=range_limit(temp)

    for val in new_data:
        temp=Restaurant.objects.get(user=val[1])
        near_rest.append(temp)
        

    if request.method=='GET':
        x=request.GET.get('lat')
        y=request.GET.get('lon')
        print(x,y)
        name=request.GET.get('query')
        result=search(name,near_rest)
        if result:
            return render(request,'nearbyrest/nearbyrest.html',context={'data':result,'name_res':rest_names})
        else:
            return render(request,'nearbyrest/nearbyrest.html',context={'data':near_rest,'name_res':rest_names})

    return render(request,'nearbyrest/nearbyrest.html',context={'data':near_rest,'name_res':rest_names})


# this would redirect to the res pages
def lister(request,restid):
    obj=User.objects.get(username=restid)
    data=Restaurant.objects.get(user=obj)
    return render(request,'nearbyrest/rest_list.html',context={'data':data})

