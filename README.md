# tennisball-tracker

using Matterport Mask R-CNN balloon sample and bits of code from shapes sample to try to achieve transfer learning on tennis 
match video frames to track a ball.  

If using VGG Annotator, be sure to use version 1 as version 2 is incompatible with Matterport out-of-box.  

I did make some changes to use circle annotation shape rather than polygon.  Probably go with rectangle as circle's mask is 
inaccurate right now but think there may have been a skimage circle perimeter to get x,y of circle perimeter.  
