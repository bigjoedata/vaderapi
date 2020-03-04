# vaderapi

A simple API for [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) by [cjhutto](https://github.com/cjhutto).

To build Dockerimage, use
docker build --file Dockerfile --tag simplevader .

Then you can run with
docker run -p 24601:24601 vader

Visit http://127.0.0.1/docs to view documentation and test your API.

#Inspired by 
https://fastapi.tiangolo.com/tutorial/testing/#testing-extended-example<br>
https://spectrum.chat/zeit/now/any-examples-of-using-python-fastapi-with-zeit-now-v2~c3c3c44b-4d75-4417-9ec4-1d00f6db9163
https://towardsdatascience.com/how-to-properly-ship-and-deploy-your-machine-learning-model-8a8664b763c4<br>
https://github.com/saasify-sh/saasify<br>
