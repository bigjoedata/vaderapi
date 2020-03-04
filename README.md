# vaderapi

A simple [Python](https://www.python.org/) API for [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)<br>
<br>
Other key tools used include:<br>
[FAST API](https://github.com/tiangolo/fastapi)<br>
[Docker](https://www.docker.com/)<br>
[Pydantic](https://pydantic-docs.helpmanual.io/)<br>
[Loguru](https://github.com/Delgan/loguru)<br>
[Gunicorn](https://gunicorn.org/)<br>
[Requests](https://requests.readthedocs.io/en/master/)<br>
<br>
<b>To build Dockerimage, clone this repository, [install Docker](https://docs.docker.com/install/), then run the following:</b><br>
`docker build --file Dockerfile --tag simplevader .`<br>
<br>
<b>Then you can run with</b><br>
`docker run -p 24601:24601 vader`<br>
<br>
Visit http://127.0.0.1/docs to view documentation and test your API.<br>
<br>
#Inspired by <br>
https://fastapi.tiangolo.com/tutorial/testing/#testing-extended-example<br>
https://spectrum.chat/zeit/now/any-examples-of-using-python-fastapi-with-zeit-now-v2~c3c3c44b-4d75-4417-9ec4-1d00f6db9163
https://towardsdatascience.com/how-to-properly-ship-and-deploy-your-machine-learning-model-8a8664b763c4<br>
https://github.com/saasify-sh/saasify<br>
