import os
import requests
import sys
from dotenv import load_dotenv
from Stable_Diffusion import get_background
from Extract_Pdf import get_content
from Text_Summarization import summarize_resume

load_dotenv()
bearer_token = os.environ["REPHRASE_API_KEY"]

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

resume_content = get_content(sys.argv[1])
summarized_content = summarize_resume(resume_content)
background_image = get_background()

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": background_image,
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": f"<speak>{summarized_content}</speak>",
                            "transcript_type": "ssml_limited",
                        },
                    },
                },
            ]
        },
    ],
    "title": "Video Resume by Dhruv Gupta",
    "thumbnailUrl": background_image,
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(f"CAMPAIGN_ID= {response.text}")