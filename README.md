# The `Virus-X Y-Surprise` AI Image Create-and-Save Starter Pack

## Overview
#### The days of paying high prices for AI-generated images are over
Use this helper tool to generate ai images based on your own description while simultaneously saving the images to your device. Price is <1¢ USD per image, so...go to town. 

#### Features
- Sends a request to openai with a description of your choice
    - Select number of photos to return per request
    - Choose from 3 resolution options
- Returns the URLs of the image(s)
    - Links to images expire after one hour
    - ^ That is why this helper will save the images directly to your device so that you can keep them forever

#### Testimonials
- "Why make or purchase birthday qards when you can Virus-X Y-Surprise them for <$0.002?"
- "That's not a lot of cents!"
- "Our office is finally complete now that we have a life-sized poster of 'Synergy Dave' 'segwaying' into the 'mandatory wellness seminar'. He was very pleasantly Y-Surprised upon seeing it in our `Corporate Head-Q-uarters`."
- "I have always wondered what an aerial view of me chained to a mossy tree trunk with eyes, a mouthful of ants, and harmful spiders would look like"
- "I accidentally deleted all of the pictures I took with my friends at the fjords, but the **The `Virus-X Y-Surprise` AI Image Create-and-Save Starter Pack** saved the day! All I had to do was name the specific fjords and decsribe all my friends, and the fjordsing-photos are 'baq' and better than ever."
- "Who knew that you could spell the word 'Oprah' with 32 characters?"
- "Satisfaqtion indeed!"
- "People do!"
- "2 out of 4 dentists approve!"

## Instruqtions
### Clone repo
```sh
● ● λ git clone https://github.com/mason-u-borchard/instant-ai-image-create-and-save.git
● ● λ cd instant-ai-image-create-and-save
```
### Prerequisites
##### 1. Install Python
```sh
(instruqtions coming "soon")
```
##### 2. Install pip
```
(instruqtions coming "soon")
```
##### 3. Confirm successful install
```sh
● ● λ which python
# output 
/usr/local/bin/python3
```

### Environment
##### 1. Create and activate a virtual environment
```sh
● ● λ python -m venv .venv 
● ● λ source .venv/bin/activate
```

##### 2. Install requirement(s)
```sh
● ● λ pip install -U pip
● ● λ pip install -r requirements.txt
```

##### 3. Confirm openai installation
```sh
● ● λ which openai
# output
/usr/local/bin/openai
```
### Configure API Key

##### 1. Obtain an `openai` API Key
- This can be done on the openai website (might put instructions here later)

##### 2. Make a copy of `example.apikey.sh`
```sh
● ● λ cp example.apikey.sh .apikey.sh
```

##### 3. Open .apikey.sh in terminal and replace PRETEND_API_KEY with the real one
```sh
# open
● ● λ vim apikey.sh
```

```sh
# edit
export OPENAI_API_KEY="YOUR_API_KEY"
~                                                                                                                                     
~                                                                                                                                      
~                                                                                                                                       
~                                                                                                                                       
~                                                                                                                                       
~                                                                                                                                       
~                                                                                                                                       
~                                                                                                                       -- INSERT --              
           
```
`# save`
Use the following keyboard shortcut to save changes:
`(press & release)esc + (hold)shift + Z + Z`

#### Set OPENAI_API_KEY system variable by running the `.apikey.sh` script

##### 1. Make the script 'executable'
```sh
● ● λ chmod +x .apikey.sh
```
##### 2. Run shell script
```sh
● ● λ source ./.apikey.sh
```
##### 3. Confirm that the OPENAI_API_KEY variable is configured correctly:
```sh
● ● λ echo $OPENAI_API_KEY
YOUR_API_KEY
```

### Run

##### 1. Fill out variables 
```python
DESC="Which random British guy am i? 'Mark Twain!' 'Gordon Ramsay!' 'Travis Barker!'"
path="/Users/YOUR_PATH_PLZ_INCLUDE_TRAILING_SLASH/instant-ai-image-create-and-save/"
```

##### 2. Run file
```sh
● ● λ python createimage.py
```
