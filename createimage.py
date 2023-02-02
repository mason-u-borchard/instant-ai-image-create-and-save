import openai 
import os
import urllib.request
import random
import string
from datetime import datetime


openai.api_key = os.getenv("OPENAI_API_KEY")

desc="Which random British guy am i? 'Mark Twain!' 'Gordon Ramsay!' 'Travis Barker!'"
path="/Users/YOUR_PATH_PLZ_INCLUDE_TRAILING_SLASH/instant-ai-image-create-and-save/"

def get_random_string(length):
    # choose from all lowercase letters
    letters = string.ascii_lowercase
    qaracters = []
    meth = 2
    # returns a List of 2 random strings comprised of 'length' characters
    for x in range(meth):
      surprise = ''.join(random.choice(letters) for y in range(length))
      qaracters.append(surprise)
    return qaracters

def ai_generate_image(DESC, PATH):
  response = openai.Image.create(
    prompt=DESC,
    n=1, # number of pictures to generate
    size="1024x1024" # "256x256", "512x512", or "1024x1024"
  )

  y_surprise = response["data"]
  image_loqations = []
  for virus_x in y_surprise:
        ahora=datetime.now()
        deight_thyme = ahora.strftime("%m-%d-%Y_%H-%M-%S")
        qaracters = get_random_string(1)
        image_location = "".join([PATH, "%s__%s-virus_%s-surprise.jpg" % (deight_thyme, qaracters[0], qaracters[1])])
        urllib.request.urlretrieve(virus_x["url"], image_location)
        image_loqations.append(image_location)
  enhanced_response = response
  enhanced_response["files"] = image_loqations
  print(enhanced_response) 



ai_generate_image(DESC=desc, PATH=path)
