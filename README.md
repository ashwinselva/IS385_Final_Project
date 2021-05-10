Project title : Genre Recognizer
Group member 1 : Ashwin Selvendran
Group member 2 : Kaushal Verma
Contact email : as3449@njit.edu
Course name : IS485
University name : NJIT
Professor name: Mark Cartwright

Instructions to run the program:

pip3 install python_speech_features

pip3 install scipy

pip3 install numpy

pip3 install sklearn.model_selection

pip3 install librosa


downlaod GTZAN dataset and extract it in the same directory as the python file. After you extract you would be able to see the dataset as a single folder.
To execute the program run `python3 genre_recognizer.py`

Dataset link: http://opihi.cs.uvic.ca/sound/genres.tar.gz

To change the input song change 'test1.wav' to another wav file that is in the bottom of the py file

Synopsis:

The project concept itself is interesting. Apps such as SoundCloud and Spotify make seemingly perfect playlists and we would like to see if we can at least match a songs style to another to a certain degree. People with non music backgrounds would not be able to identify a music track which would be easily solved using this program. They just have to run the program by putting in the music track file name in wav format and the program would recognize it.

The program would first read the feature vector of the song using python_speech_features and compute a matrix which consists of mean vector of the feature vector, covariance matrix of the feature vector and compare this data with the dataset where the dataset of the song is also computed in the form of feature vector like the input song. The accuracy of the dataset was tested by splitting it into train and test feature vectors and computed the accuracy by comparing both train and test data.

I did test a hiphop song which did predict as a hiphop song but sometimes predict as a country song which is also good as the feature vector is similar to a country song. The predicted accuracy for test and train data was tested to be 70% accurate.

Citations:

N. Scaringella, G. Zoia and D. Mlynek, "Automatic genre classification of music content: a survey," in IEEE Signal Processing Magazine, vol. 23, no. 2, pp. 133-141, March 2006, doi: 10.1109/MSP.2006.1598089.

G. Tzanetakis and P. Cook, "Musical genre classification of audio signals," in IEEE Transactions on Speech and Audio Processing, vol. 10, no. 5, pp. 293-302, July 2002, doi: 10.1109/TSA.2002.800560.

arXiv:1804.01149

Oramas S, Barbieri F, Nieto O, Serra X. Multimodal deep learning for music genre classification. Transactions of the International Society for Music Information Retrieval. 2018;1(1):4-21. DOI: 10.5334/tismir.10



