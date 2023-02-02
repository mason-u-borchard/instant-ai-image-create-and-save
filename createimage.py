import openai 
import os
import urllib.request
import random
import string
from datetime import date


openai.api_key = os.getenv("OPENAI_API_KEY")

DESC="Which random British guy am i? 'Mark Twain!' 'Gordon Ramsay!' 'Travis Barker!'"
path="/Users/YOUR_PATH_PLZ_INCLUDE_TRAILING_SLASH/instant-ai-image-create-and-save/"

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    qaracters = []
    meth = 2
    # returns a List of 2 random strings comprised of 'length' characters
    for x in range(meth):
      surprise = ''.join(random.choice(letters) for y in range(length))
      qaracters.append(surprise)
    return qaracters

def ai_generate_image(desc, path):
  response = openai.Image.create(
    prompt=desc,
    n=1, # number of pictures to generate
    size="1024x1024" # "256x256", "512x512", or "1024x1024"
  )

  y_surprise = response["data"]

  for virus_x in y_surprise:
        deight=date.today()
        qaracters = get_random_string(1)
        image_location = "".join([path, "%s-virus_%s-surprise_%s.jpg" % (qaracters[0], qaracters[1], str(deight))])
        urllib.request.urlretrieve(virus_x["url"], image_location)
  enhanced_response = response
  enhanced_response["file"] = image_location
  print(enhanced_response) 

ai_generate_image(desc=DESC, path=path)