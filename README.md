# Sentiment Analysis API with Docker

This repository contains a simple sentiment analysis API built with [FastAPI](https://fastapi.tiangolo.com/) and a frontend HTML page to interact with it. The API uses a pre-trained model from the [Hugging Face Transformers](https://huggingface.co/transformers/) library to analyze the sentiment of the provided text.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Accessing the Application](#accessing-the-application)
- [Example HTML File](#example-html-file)
- [Conclusion](#conclusion)
- [License](#license)

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- Basic knowledge of how to use Docker.

## Project Structure

- **Dockerfile**: Contains instructions to build the Docker image.
- **requirements.txt**: Lists the Python dependencies required for the application.
- **main.py**: The FastAPI application that provides the sentiment analysis API.
- **index.html**: A simple HTML file to interact with the API.

## Dependencies

Make sure to include the following libraries in your `requirements.txt`:

## Building the Docker Image

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/xEMPERORx/api_text_sentiment.git
   cd api_text_sentiment
   
```bash
   docker build -t api_text_sentiment
```
## Running the Docker Container
```bash
  docker run -p 8000:8000 sentiment-analysis-api
```

## Accessing the Application
Open the HTML File: Open the index.html file in your web browser. You can do this by double-clicking the file or dragging it into your browser.

Enter Text: In the text area provided, type the text you want to analyze for sentiment.

Submit the Request: Click the "Submit" button. This action will send a POST request to the API endpoint http://localhost:8000/analyze-sentiment with the text you entered.

View the Response: The sentiment analysis result will be displayed below the button. If the request is successful, you will see the sentiment (e.g., "POSITIVE", "NEGATIVE", etc.). If there is an error, an error message will be displayed.

## Example HTML File
Here is the content of the index.html file that you can use to interact with the API:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis</title>
    <script>
        async function analyzeSentiment() {
            const textInput = document.getElementById("textInput").value;
            const responseElement = document.getElementById("response");

            // Clear previous response
            responseElement.innerHTML = "";

            try {
                const response = await fetch("http://localhost:8000/analyze-sentiment", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ text: textInput })
                });

                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }

                const data = await response.json();
                // Display the sentiment
                responseElement.innerHTML = `Sentiment: ${data.sentiment}`;
            } catch (error) {
                responseElement.innerHTML = `Error: ${error.message}`;
            }
        }
    </script>
</head>
<body>
    <h1>Sentiment Analysis</h1>
    <textarea id="textInput" rows="4" cols="50" placeholder="Type your text here..."></textarea><br>
    <button onclick="analyzeSentiment()">Submit</button>
    <div id="response" style="margin-top: 20px; font-weight: bold;"></div>
</body>
</html>
```
## Conclusion
You now have a working sentiment analysis API running in a Docker container, along with a simple HTML interface to interact with it. Feel free to modify the code and improve the application as needed!

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/xEMPERORx/api_text_sentiment/blob/main/LICENSE) file for details.
