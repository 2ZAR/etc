#Practice#
#MNIST#

mkdir MNIST_data
cd MNIST_data

from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("Mnist_data/", one_hot=True)

import deepchem as dc
import tensorflow as tf
import deepchem.models.tensorgraph.layers as layers

train_dataset = dc.data.NumpyDataset(mnist.train.images, mnist.train.labels)
test_dataset = dc.data.NumpyDataset(mnist.test.images, mnist.test.labels)

model=dc.models.tensorgraph(model_dir='mnist')

isintrance(model, dc.models.Model)

feature=layers.Feature(shape=(None,784))
label=layers.Label(shape=(None,10))

make_image=layers.Reshape(shape=(None,28,28), in_layers=feature)

conv2d_1=layers.Conv2D(num_outputs=32, activation_fn=tf.nn.relu, in_layers=make_image)
conv2d_2=layers.ConV2D(num_outputs=64, activation_fn=tf.nn.relu, in_layers=conv2d_1)

flatten=layers.Flatten(in_layers=conv2d_2)
dense1=layers.Dense(out_channels=1024, activation_fn=tf.nn.relu, in_layers=flatten)
dense2=layers.Dense(out_channels=10, activation_fn=None, in_layers=dense1)

smce=layers.SoftMaxCrossEntropy(in_layers=[label, dense2]
loss=layers.ReduceMean(in_layers=smce)
model.set_loss(loss)

output=layers.SoftMax(in_layers=dense2)
model.add_output(output)

model.fit(train_dataset, nb_epoch=10)

metric=dc.metrics.Metric(dc.metrics.accuracy_score)

train_scores = model.evaluate(train_dataset, [metric])
test_scores = model.evaluate(test_dataset, [metric])

