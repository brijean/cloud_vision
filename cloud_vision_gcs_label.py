#!/usr/bin/python

from google.cloud import vision
from google.cloud import storage


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    #for blob in blobs:
    #    print(blob.name)
    return blobs
        

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

def main():
  print "Enumerate Objects in Bucket"
  object_list = list_blobs("bookshelf-application-223720-vision")
  print "Labeling Images with CloudVision"
  for object in object_list:
      object = "https://storage.googleapis.com/bookshelf-application-223720-vision/" + object.name
      print "Object: " + object
      detect_labels_uri(object)
  
if __name__== "__main__":
  main()
