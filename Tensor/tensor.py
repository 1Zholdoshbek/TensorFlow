#What is tensor
#Practice
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']=2
import tensorflow as tf
a=tf.constant(1,shape=(1,2))
b=tf.constant([1,2,3,4,5])
c=tf.constant([[1,2],
               [3,4],
               [5,6]],dtype=tf.float16)
print(c)
#ouput:
"""tf.Tensor(
[[1. 2.]
 [3. 4.]
 [5. 6.]], shape=(3, 2), dtype=float16)"""