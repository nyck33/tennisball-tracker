# tennisball-tracker

using Matterport Mask R-CNN balloon sample and bits of code from shapes sample to try to achieve transfer learning on tennis 
match video frames to track a ball.  

If using VGG Annotator, be sure to use version 1 as version 2 is incompatible with Matterport out-of-box.  

ipynb notebook with name ending in perimeter uses `skimage.draw.circle_perimeter` vs. other one uses just `skimage.draw.circle`
