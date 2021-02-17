# Python-flask push to heroku

如果你想要建一個小小的網站，可以使用heroku，他與github的差別在於，github是架設一個靜態網站，heroku是可以做動態的網站，所以你是想作聊天機器人或機器學習的都可以用heroku做部屬。

---
本篇的檔案([傳送門](https://github.com/yoyoisaboy/heroku_demo.git))

試做一個這個([傳送門](https://machine-learning-python.kspax.io/datasets/ex4_plot_random_multilabel_dataset))，是關於樣本分布的視覺圖呈現，我希望按下按鈕可將圖片放到網站上。

## 結果
![](https://i.imgur.com/tLQXroy.png)

關於本片將注重在python-flask 到 heroku的流程上。程式碼可自行到我的[github](https://github.com/yoyoisaboy/heroku_demo)看看。


---
## 需要的檔案
將你測試完你的flask程式後，我建議把程式檔和資料做一些規劃，像是把需要安裝的套件、環境放在外面，裡面再放程式檔，圖片或音檔再開資料夾放，以我的例子,
我把app外放安裝的環境，app內放程式檔，圖片放static裡，總之別把全部的東西都放在同一個路徑。

在上傳之前有幾個重要的檔案必須加進去。
1. Procfile
2. requirements.txt
3. runtime.txt

以我的例子:
1. Procfile
```
web gunicorn run:app
```
![](https://i.imgur.com/tzUQk6W.png)
* gunicorn([傳送門](https://gunicorn.org/))是一個Python Web的HTTP接口服務器([介紹](https://en.wikipedia.org/wiki/Gunicorn))。
* 一開始先從run執行app的程式(也就是app = Flask(\_\_name\_\_)這行)，run.py是你網站一開始的進入點。

2. requirements.txt
大家都很熟悉的，是安裝的套件有哪些。
```
flask
flask-Cors
requests
gunicorn
pandas
matplotlib
```
請注意，要用heroku必須要加gunicorn，不然Procfile到時會裝不了。

3. runtime.txt
```
python-3.9.0
```
你python的版本，heroku會幫你裝起來。

## 到平台申請專案
---
到github New一個專案
![](https://i.imgur.com/hrHOvgN.png)


---

接著都設定好後，去安裝git([傳送門](https://git-scm.com/))我們用指令的方式把檔案上傳到github上，heroku可以和github作聯動，比較方便。

安裝完後到那個資料夾，按右鍵把git叫出來
![](https://i.imgur.com/RgIOXbN.png)

接著打:
```
git init
git clone "your github HTTPS"
git status
git add .
git commit -m "first push"
git push
```
完成後到github重新整理看看上傳了沒。


---

接著到heroku，申請完後按New -> Create new app。
![](https://i.imgur.com/LKYjE0h.png)

點Deploy，找聯動github。
![](https://i.imgur.com/EHbQeM7.png)


依序把
1. 你github的專案找到。
2. 點Disable Automatic Deloys，去自動更新你github專案的檔案。
3. 按Deploy Brach 去安裝你的程式。
![](https://i.imgur.com/Z6t4Khf.png)


---
好了之後，按Settings找Domains。
![](https://i.imgur.com/dniebwI.png)

你會發現給你一串網址，那就是你部屬好的網站了。


## BUG
假如過程中有問題你可以到More -> View logs，看出現什麼問題。
![](https://i.imgur.com/VTDVHTx.png)

---

## 限制

畢竟是免費的，所以會有些限制
:::danger
每個專案的限制是100MB，資料庫的部份，每個專案的資料庫大小限制則是5MB，而且有SQLite、MySQL、PostgreSQL可以選用。

Heroku的1個dyno(Heroku的計價單位)差不多是可以處理10~50 request/second。如果覺得不夠用，也可以考慮它的付費方案來增加dyno數，更詳細付費方案([傳送門](https://www.heroku.com/pricing))
:::


ξ( ✿＞◡❛)/
謀阿~~
