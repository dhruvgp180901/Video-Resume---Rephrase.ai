import requests
import os
import sys
import json

def get_background():
    url = "https://stablediffusionapi.com/api/v3/text2img"


    payload = {
    "key": "8rnBHqLarshCwcwjJtFnY6EIWdry5fmgDZ85vkv4OVP1PD2kwIWHgpHbifYM",
    "prompt": "Hi, my name is [Your Name], and I am a computer vision and image processing engineer. One of the tools I use frequently in my work is Stable Diffusion API. By combining this powerful API with state-of-the-art image generation techniques, I have been able to create stunning and realistic background images for a wide range of applications. If you are looking for a skilled and experienced image processing engineer who can leverage Stable Diffusion API to help you achieve your goals, I would be thrilled to hear from you. Thank you for considering my application",
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