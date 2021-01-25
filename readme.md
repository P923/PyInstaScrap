<h1 align="center">
  <div ALIGN="center">
    <img alt="" src="https://raw.githubusercontent.com/P923/PyInstaScrap/master/imgs/ic.jpeg" width="300px" height="300px" />
  </div>
  <br /><br />
  InstaScrap</h1>
<p align="center">Python OSINT tool for Instagram</p>
<div align="center"><a href="https://www.python.org/"><img alt="@Python" src="https://camo.githubusercontent.com/b764d47c4b030ecf374353eddc2c5323c7e3cb45823b5f26e49b322c0fa89567/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d322e37253243253230332e352d3337373661622e7376673f6d61784167653d32353932303030" /></a>
</div><br />

### Introduction
<div>
    <p align="justify">
        InstaScrap is a scraper for Instagram. Insert a target and you will receive various information, including: page connected with Facebook, Email, Phone number (if available). In addition, you will be shown the locations used in the posts, with a map (OpenStreetMap) for an easier consultation.
        It will also generate a word cloud for hashtags and for the most used words.
        You will also visualize who has been tagged by the target in their posts.
        You can also check who has added the most likes to the target's posts.
    </p>
    <p>
        The output is given with an html file in the Output folder.
    </p>
</div>

<div align="center">
   <img alt="" src="https://raw.githubusercontent.com/P923/PyInstaScrap/master/imgs/4.jpg" width="60%" />
   <br/>
   <img alt="" src="https://raw.githubusercontent.com/P923/PyInstaScrap/master/imgs/1.png" width="60%"/>
   <br/>
   <img alt="" src="https://raw.githubusercontent.com/P923/PyInstaScrap/master/imgs/2.jpg" width="60%" />
   <br/>
   <img alt="" src="https://raw.githubusercontent.com/P923/PyInstaScrap/master/imgs/3.png" width="60%" />
</div>

### Prerequisites
```
numpy, wordcloud, dominate, ipywidgets, Pillow, tqdm
instagram-private-api @ https://git@github.com/ping/instagram_private_api
```


### Installing

```
pip install -r requirements.txt 
```


## Running
<div>
    Setup <b>USERNAME</b>, <b>PASSWORD</b> and <b>TARGET</b> in main.py. <br/>
    Setup the path of cookie in <b>DEFAULT_COOKIE_PATH</b>. <br/>
    Setup <b>LANGUAGES</b>, with the languages of the posts of TARGET. <br/>
    Set <b>CHECK_LIKERS</b> to True if you want to see all likers of TARGET. (Slow, you might be throttled) <br/><br/>
</div>

```
python main.py
```


## License
This project is licensed under the MIT License.


## Author
<a href="https://github.com/P923" title="P923">Matteo P923</a> | 2021

