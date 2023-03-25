import requests
import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

def get_background():
    url = "https://stablediffusionapi.com/api/v3/text2img"


    payload = {
    "key": os.environ["STABLE_DIFFUSION_KEY"],
    "prompt": "A sci-fi world beyond galaxies for computer scientist",
    "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker":"yes",
    "webhook": None,
    "track_id": None
    }

    response = requests.post(url, json=payload)

    output = json.loads(response.text)
    image_link = output["output"][0]
    print(image_link)
    print("Fetched Background Image!!")
    return image_link