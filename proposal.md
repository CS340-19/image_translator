# Image Translator
## Team Members: Andy Liu(team manager), Yucheng Ma, Yiming Sun, Dakota Williams 

### 1: Intro
<p>   Our idea is to create a computer application that will recognize words in a picture, from many different alphabets, and translate it to English or other languages. Yucheng and Yiming are international students and they come from China. They can fluently communicate with everyone in English. But in the classroom, they are still struggling in many professional vocabulary. That's why we have this idea about our project. We hope that this will make it easier for tourists and students to communicate and take notes. Sometimes professors talk/write too fast, and the only option left for these students is to take pictures. This is where our program will come in. With our program, students can easily translate their pictures they take in classes and explain it to languages they are comfortable in. Also, for tourists, when people go to foreign countries, it is hard to go anywhere. You will not be able to communicate with others (unless they know English or you know other languages) or understand their written language. It might be easy to translate language such as Spanish where you can type the word into your mobile translator. However, for a language such as Chinese or Japanese, there no way foreigners will know how to type the word into the translator. Our program can help with that. Just take a picture and have those foreign words translated for you. </p>
 
### 2: Customer Value

<p> Our primary customers will be international students. It's hard for some students to read/take notes especially if the class is not in their native tongue. We hope to provide them with a solution to this by being able to translate either written or powerpoint slides. Students can spend more take thinking instead of try understand what that word mean.  </p>

<p> There exist many translators, but not many credible translator that can translate words in image. We try to create an easy to use, and reliable program that can do accurrate translation. There will be no hassle when using our program, and truly help our customers. Our program can help our customers translate any languages for them. It will save them when traveling or help international translate their photos.</p>


### 3: Proposed Solution & Technology
<p> For this program, we are going to use python. The reason we choose python is because the API we choose is good fit to python, and it's easy to learn for us. We will rely on Google cloud platform and use their API. GCP a cloud computing service that provide by google, it provides numerous of API. For now, we have choose to use Google vision, it is an API that can analyze image and extract the text from image. Another API we will use is the cloud translation. This API can translate the text that we extract from image to other language, it can also auto detect the language of the input texts. We have not determined the way to build GUI, we will decide it later. The main working process is pretty straight forward. You can use this program to open the file with .jpg and . png. Then the API will detect the text from the image. You can choose the language you want translate to, and the translation API will handle it. </p>

### 4: Team
<p>Nobody on the team has developed anything like this before, but Wiliiams have two years experience of using Python. Other teammates have learned C++ and C, but are intereseted in learning Python.None of us have used the Google APIs before. We hope to use this as a learning experience to better our development skills. </p>

Liu，Andy：

Williams，Dakota：

Ma，Yucheng：

Sun，Yiming：



### 5: Project Management
#### Schedule:
<p>We will meet every weeks and discuss milestone and help each other with issues. First we will try to do some researches about image recognition. Afterward, we will do some researches regarding how to use google API in our code. This will probably take a week or two. The code will be split among us and we will split the works after doing our researches. Then we will spend time test image recognition. This probably going to take awhile since we never done it before. Then we going incorporates google API, and work the translation. Lastly, we will do some testing and debugging.</p>


#### Resources: 
https://cloud.google.com/vision/docs/ 
https://cloud.google.com/translate/docs/

