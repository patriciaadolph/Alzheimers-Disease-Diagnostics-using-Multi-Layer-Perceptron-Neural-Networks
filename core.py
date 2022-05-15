import pickle
import os
import numpy as np
import random
from sklearn.neural_network import MLPClassifier
# from sklearn.preprocessing import normalize
# import matplotlib.pyplot as plt
import cv2

def preprocess_img(img):
	image_size = (224,224)
	def image_resize(img,image_size):
		img = np.resize(img,image_size)
		return img
	def normalize(img):
		img = img / 255
		return img
	def reshape(img):
		img = np.reshape(img,(50176))
		return img

	img = image_resize(img,image_size)
	img = normalize(img)
	img = reshape(img)
	return img

def load_pickle(file_name):
	file = open(file_name,"rb")
	data = pickle.load(file)
	file.close()
	return data

def prepare_training_set():
	dataset = load_pickle("core/dataset.pickle")
	AD = dataset['AD']
	HC = dataset["HC"]
	dataset = []
	i = 0
	for person in HC:
		for j in range(33,86,1):
			scan_image = person[j]
			dataset.append((preprocess_img(scan_image), [1,0]))
		i += 1

	for person in AD :
		for j in range(33,86,1):
			scan_image = person[j]
			dataset.append((preprocess_img(scan_image),[0,1]))
		i -= 1
		if i == 0:
			break


	random.shuffle(dataset)
	training_input = dataset[0:int(len(dataset) * .75)]
	testing_set = dataset[int(len(dataset) * .75):len(dataset)]
	tr_input = []
	tr_output = []
	for i in training_input:
		tr_input.append(i[0])
		tr_output.append(i[1])
	ts_input = []
	ts_output = []
	for i in testing_set:
		ts_input.append(i[0])
		ts_output.append(i[1])
	tr_input = np.array(tr_input)
	tr_output = np.array(tr_output)
	ts_input = np.array(ts_input)
	ts_output = np.array(ts_output)
	return tr_input,tr_output,ts_input,ts_output

def create_model():
	clf = MLPClassifier(

		hidden_layer_sizes=(100,),
	 	activation='relu',
	 	solver='adam',
	 	alpha=0.0001,
	 	batch_size='auto',
	 	learning_rate='constant',
	 	learning_rate_init=0.001,
	 	power_t=0.5,
	 	max_iter=200,
	 	shuffle=True,
	 	random_state=None,
	 	tol=0.0001,
	 	verbose=False,
	 	warm_start=False,
	 	momentum=0.9,
	 	nesterovs_momentum=True,
	 	early_stopping=False,
	 	validation_fraction=0.1,
	 	beta_1=0.9,
	 	beta_2=0.999,
	 	epsilon=1e-08
	 )

	return clf

def train(mlp,X_train,y_train,X_test,y_test,file_name):
    N_TRAIN_SAMPLES = X_train.shape[0]
    N_EPOCHS = 125
    N_BATCH = 128
    N_CLASSES = np.unique(y_train)
    scores_train = []
    scores_test = []
    epoch = 0
    while epoch < N_EPOCHS:
        print('epoch: ', epoch)
        random_perm = np.random.permutation(X_train.shape[0])
        mini_batch_index = 0
        while True:
            # MINI-BATCH
            indices = random_perm[mini_batch_index:mini_batch_index + N_BATCH]
            mlp.partial_fit(X_train[indices], y_train[indices], classes=N_CLASSES)
            mini_batch_index += N_BATCH
            if mini_batch_index >= N_TRAIN_SAMPLES:
                break
        scores_train.append(mlp.score(X_train, y_train))
        score = mlp.score(X_test, y_test)
        print(score)
        file = open(file_name,"wb")
        pickle.dump(mlp,file)
        file.close()

        # SCORE TEST
        scores_test.append(score)
        file = open("core/score.pickle", "wb")
        pickle.dump(scores_test, file)
        file.close()
        epoch += 1


def get_model_score():
    scores = load_pickle("core/score.pickle")
    return scores[-1]

def get_ad_detection(path):
    classifier = load_pickle("core/classifier.pickle")
    if os.path.exists(path):
        img = preprocess_img(cv2.imread(path,0))
        result = classifier.predict([img])
        prob_result = classifier.predict_proba([img])
        print(prob_result)
    return prob_result[0]

def train_model():
    tr_input, tr_output, ts_input, ts_output = prepare_training_set()
    train(create_model(),tr_input,tr_output,ts_input,ts_output,"core/classifier.pickle")

#train_model()