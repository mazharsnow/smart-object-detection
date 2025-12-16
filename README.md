# Object-Detection-and-Distance-Measurement

This repository contains object_detection in python which is able to perform the following task -

    - Object detection from live video frame or in a image
    - Counting the number of objects in a frame and segmentation
    - Measuring the distance of object using depth information

For object detection YOLO-V3 has been used which is able to detect 80 different objects. Some of those are-

    - person
    - car
    - bus
    - stop sign
    - bench
    - dog
    - bear
    - backpack and so on.

## Theory

In a traditional image classification approach for object detection there are two well-known strategies.

For single object in a image there are two scenarios.

    1. Classification
    2. Localization

For multiple objects in a image there are two scenarios.

    1. Object detection and localization
    2. Object segmentation
    
## How the object detection works?
From the initial part we understood that, to measure distance from an image we to localize it first to get the depth        information. Now, how actually localization works?

### Localize objects with regression
Regression is about returning a number istead of a class. The number can be represented as (x0,y0,width,height) which are related to a bounding box. In the images illustrated above for single object if you want to only classify the object type then we don't need to draw the bounding box around that object that's why this part is known as Classification . However, if we are interested to know where does this object locates in the image then we need to know that 4 numbers that a regreesion layer will return. As you can see there is a black rectangle shape box in the image of white dog which was drawn using the regression layer. What happens here is that after the final convolutional layer + Fully connected layers instead of asking for class scores to compare with some offsets a regression layer is introduced. Regression layer is nothing but some rectangular box which represents individual objects. For every frame/image to detect objects the following things happens.
    
    
## References
1. https://sci-hub.tw/10.1109/SAS.2010.5439423
2. http://emaraic.com/blog/distance-measurement
3. https://www.pyimagesearch.com/2016/04/04/measuring-distance-between-objects-in-an-image-with-opencv/
4. https://www.khanacademy.org/science/physics/geometric-optics/lenses/v/object-image-and-focal-distance-relationship-proof-of-          formula
5. https://www.khanacademy.org/science/ap-physics-1/ap-centripetal-force-and-gravitation/introduction-to-uniform-circular-motion-ap/v/distance-or-arc-length-from-angular-displacement




