#!/usr/bin/python

import sys
from google.cloud import vision
from google.cloud import storage


def validate_input():
    if len(sys.argv) != 2:
        print "Proper syntax is:", sys.argv[0], "<google-cloud-storage-bucket>\n"
        bucket = raw_input("Enter GCS Bucket name:")
    else:
        bucket = sys.argv[1]
    return bucket
    
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
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
  bucket = validate_input()
  object_list = list_blobs(bucket)
  print "Labeling Images with CloudVision"
  for object in object_list:
      object = "https://storage.googleapis.com/" + bucket + "/" + object.name
      print "Object: " + object
      detect_labels_uri(object)
  
if __name__== "__main__":
  main()
