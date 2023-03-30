#!/usr/bin/env python3

from flask import Flask, request, Response
import requests
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
file_handler = logging.FileHandler('underlying-prompts.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def handle_request(path):
    if request.method == 'POST':
        headers = {
            "Content-Type": request.headers["Content-Type"],
            "Authorization": request.headers["Authorization"]
        }
        json_data = request.get_json()
        logger.info(f"OpenAI Request: {json_data}")

        url = f"https://api.openai.com/{path}"

        if "stream" in json_data and json_data["stream"] == True:
            logger.error("Stream mode is not supported yet")
            return "Stream mode is not supported yet"
            """
            response = requests.post(
                url,
                headers=headers,
                json=json_data, 
                stream=True
            )
            def generate():
                for chunk in response.iter_content(chunk_size=1024):
                    response = requests.post(
                        url,
                        headers=headers,
                        json=json_data, 
                        data=chunk
                    )
                    yield chunk
            return_response =  Response(generate(), content_type='application/octet-stream')
            """
        else:
            response = requests.post(
                url,
                headers=headers,
                json=json_data
            )
            return_response =  response.json()

        logger.info(f"OpenAI Response: {response.json()}")
        return return_response


def main():    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8888
    debug = False
    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == '__main__':
    main()