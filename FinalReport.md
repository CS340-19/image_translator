# Image Translator
## Team Members: Andy Liu(team manager), Yucheng Ma, Yiming Sun, Dakota Williams 

### 1: Introduction
<p>   Our idea is to create a computer application that will recognize words in a picture, from many different alphabets, and translate it to English or other languages. Yucheng and Yiming are international students and they come from China. They can fluently communicate with everyone in English. But in the classroom, they are still struggling in many professional vocabulary. That's why we have this idea about our project.</p>
<p> We hope that this will make it easier for tourists and students to communicate and take notes. Sometimes professors talk/write too fast, and the only option left for these students is to take pictures. This is where our program will come in. With our program, students can easily translate their pictures they take in classes and explain it to languages they are comfortable in. Also, for tourists, when people go to foreign countries, it is hard to go anywhere. You will not be able to communicate with others (unless they know English or you know other languages) or understand their written language.</p>
<p> It might be easy to translate language such as Spanish where you can type the word into your mobile translator. However, for a language such as Chinese or Japanese, there no way foreigners will know how to type the word into the translator. Our program can help with that. Just take a picture and have those foreign words translated for you. </p>
<p> Generally, our project is basically the same as described by proposal. we finished the basic functions we proposed. We done the ocr and trasnlation part, and the GUI is finished very well.</p>
 
### 2: Customer Value

<p> Our primary customers will be international students. It's hard for some students to read/take notes especially if the class is not taught in their native tongue. With our application a student will be able to upload a picture of whatever the teacher has written, their notes, or even power-point slides and have them translated into their native language. Students can spend more take thinking instead of trying to understand what certain words mean while class is still in session. </p>
<p> There are many translators out there, but not many of them can credibly translate words in an image. We will create an easy to use, and reliable program that can do accurate translation. While machine translation is relatively easy. the probelm with translating things that you see is that unless you are a native, you probably dont have that ability to type that alphabet into whatever device you are using. There will be no hassle when using our program, and it will truly help our customers. Our program can help our customers translate any languages for them. It will save them when traveling or help international students translate their photos. </p>
<p> People are no longer as wiling to wait, on the fly-translation will be essential in future communications networks.  If we can create a tool that will allow people from different nations to talk to one another, with only a slight delay - like the delay you would get between e-mails/texting - then I think we will all be better off. It will help students in the classroom and travelers face to face. </p>
<p> Our most important measure of success will be, how well the translation actually worked. We will verify this constantly throughout our development. Another important factor will be how often the user actually uses the program. If they try it out once and never use it again, we obviously haven't built a useful application.


### 3: Proposed Solution & Technology
<p> For this program, we are going to use python. Most of us have never used python before, but the reason we chose python is because the APIs that we are going to use fits well with python - and it's easy for us to learn. We will rely on the Google Cloud Platform and use their API. GCP is a cloud computing service that provides by google, it provides numerous APIs and has its own Software Development Kit.</p>
<p> Optical character recognition (also optical character reader, OCR) is the mechanical or electronic conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo (for example the text on signs and billboards in a landscape photo) or from subtitle text superimposed on an image (for example from a television broadcast). For now, we have choose to use Google vision for the OCR part of our application.</p>
<p> We will try using the build in GUI framework that comes with python, TkInter. We feel that it will have the best documented code, and the most examples since it is the de-facto standard. One of the other reasons is that it can produce applications that can run on Windows, Mac OSX, and even Linux. There are plenty of tutorials that should help us get what we want out of our GUI.</p>
<p> Another API we will use is the cloud translation. This API can translate the text that we extract from image to other languages, it can also auto detect the language of the input texts. We chose this because of its speed, accuracy, and usability. Since none of us have any machine learning experience, instead of spending a lot of time trying to get that expertise this API does most of the machine learning on its own. </p>
 
<p> So for the start, we have to be fimilar with python and Google cloud platform. We need to learn the way of using Google vision and test if it works. After our program can accuratly detect the text from image, we will move to the translation part. The main working process is pretty straight forward. You can use this program to open the file with .jpg and . png. Then the API will detect the text from the image. You can choose the language you want translate to, and the translation API will handle it. </p>
<p> After we finished viable system, we were trying to make translation more accurate. We ran the test about upload a image and translate it to the different languages. We also tried different type of images, like the screenshots from articles, game posters, advertisement, and the photo of handwriting.This program can successfully identify well formatted pictures. However for some images, like advertisement and handwriting, it can have identification error and returns wrong result.</p>

![flowchart](https://github.com/CS340-19/image_translator/blob/master/CS340.png)

### 4: Team
<p>Nobody on the team has developed anything like this before, but Wiliiams have two years experience of using Python. Other teammates have learned C++ and C, but are interested in learning Python.None of us have used the Google APIs before. We hope to use this as a learning experience to better our development skills. </p>

Liu，Andy：
Familiar with C and C++, but have no expericence with python

Williams，Dakota：
Proficient in Python, SQL, and web basics. Familiar with c++. Back-End developer. 
Currently working for Network Services at OIT. I have written many python scripts that the network administrators can use.

Ma，Yucheng：
Familiar with C++ and C. Interested in python but do not have experiende with it. Like teamwork project. 

Sun，Yiming：
Familiar with C and C++,but don't have experience of developing python program.
Implement the basic functions of ocr and translation by using Python and GCP. Made a little help on GUI part and come up with some ideas and advices to the existng issue of project.



### 5: Project Management
#### Schedule:
  
<p>We will meet every weeks and discuss milestone and help each other with issues. First we will try to do some researches about image recognition. Afterward, we will do some researches regarding how to use google API in our code. This will probably take a week or two. The code will be split among us and we will split the works after doing our researches. Then we will spend time test image recognition. This probably going to take awhile since we never done it before. Then we going incorporates google API, and work the translation. Lastly, we will do some testing and debugging.</p>

#### Timeline:
  
  | Date Issued | Date for Completion | Task |
  | :---: | :---: | --- |
  | 2/4/19 | 2/18/19 | Create a base platform that we can upload images to. |
  | 2/18/19 | 2/25/19 | Bug fixing initial build |
  | 2/25/19 | 3/4/19 | Merge our OCR and base application |
  | 3/4/19 | 3/11/19 | See what kind of improvements we can make |
  | 3/11/19 | 3/18/19 | Get application ready for translator |
  | 3/18/19 | 3/25/19 | Tie in translator to our application |
  | 3/25/19 | 4/1/19 | Beta Tests and brainstorming for new ideas. |
  | 4/1/19 | 4/8/19 | Bug fixes and major improvements |
  | 4/8/19 | 4/15/19 | Final bug testing and minor improvements |
  | 4/15/19 | 4/22/19 | Project Completion |

#### Setback and Bugs:
<p>We spent a lot of time on building google environment which is out of the schedule. Becuase most of us don't have experience of using GCP, so we need time read documentation. Another part that out of schedule is building GUI, since none of us used Qt before, we spent some time to figure out the error we met. For example, we are trying to figure out put a output window on the mainwindow, somehow our plan is not working. We finally solve this issue by using widget, but it spent several days to come up this idea. Also, our translation is not 100% accurate, but it is pretty close. Our program does not create a new line, so all the translation(words) are on a single line. There a bug with our UI we are hoping to fix. Another issue we ran into is that there will be a weird symbol after our translation sometime. Lastly, our program cannot detect handwritten text, so we hope to fix that too. </p>

#### Reflection:
<p>Overall, we think our program is working pretty well even with bugs. The program is functioning fine, and doing what it is supposed to do. We need to fix some different bugs, and I think it will be perfect. The thing we will try to do differently is using a different widget for our UI since it will be easier creating our UI if we implement a different widget. We have fun making this program, and Yiming, Andy, and Yucheng learned a little python while doing this project. Also, I think using Github for our project will help us in the long run, because, eventually, we will need to do something similar in our future career. So getting early exposure to using Github will prepare us for it.</p>

#### Resources: 
https://cloud.google.com/vision/docs/ <br/> 
https://cloud.google.com/translate/docs/

