import datetime

import cv2
import numpy as np
import time
import sys
import firebase
import firebase_admin
from firebase_admin import credentials , storage, db, firestore

cred = credentials.Certificate("./key.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'hackathon-6cc53.appspot.com', }, name='storage')
bucket = storage.bucket(app=app)
cred1= credentials.Certificate("./key1.json")
app1 = firebase_admin.initialize_app(cred1)

def val():

    labels = ['Fire','Fire','Road','Road','Water','Water']

    # Initialize the app with a service account, granting admin privileges

    blobs = bucket.list_blobs()
    issue = []
    for blob in blobs :
        # print(blob.name)
        issue.append(blob.name)

    temp = issue[-7]


    blob = bucket.blob(temp)
    arr = np.frombuffer(blob.download_as_string(),np.int8)
    img = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)

    blob1 = bucket.blob("test_1.jpg")
    arr = np.frombuffer(blob1.download_as_string(),np.int8)
    img1 = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)

    blob2 = bucket.blob("test_2.jpg")
    arr = np.frombuffer(blob2.download_as_string(),np.int8)
    img2 = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)
    #
    blob3 = bucket.blob("test_3.jpg")
    arr = np.frombuffer(blob3.download_as_string(),np.int8)
    img3 = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)
    #
    blob4 = bucket.blob("test_4.jpg")
    arr = np.frombuffer(blob4.download_as_string(),np.int8)
    img4 = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)
    #
    blob5 = bucket.blob("test_5.jpg")
    arr = np.frombuffer(blob5.download_as_string(),np.int8)
    img5 = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)
    #
    blob6 = bucket.blob("test_6.jpg")
    arr = np.frombuffer(blob6.download_as_string(),np.int8)
    img6 = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)

    train = [img1,img2,img3,img4,img5,img6]


    def mse(img1, img2):
       diff = cv2.subtract(img1, img2)
       return diff

    #im_lb = 'Unclassified'

    for i in range(len(train)):
        img_temp = train[i]
        diff = mse(img,img_temp)
        res = not np.any(diff)
        #print(res)

        if res is True :
            x= i
            y = x*-1 + 1
            #print(x)
            im_lb = labels[y]
        else :
            im_lb = 'Unclassified'
    return temp,im_lb


def rename(temp,im_lb) :
    db = firestore.client()
    doc_ref = db.collection('complain').document(temp)
    doc_ref.update({
        "label" : im_lb
    })
