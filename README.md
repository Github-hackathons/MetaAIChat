# TeamTitans MetaAIChat

## Overview
TeamTitans MetaAIChat is a Flask web application that allows users to interact with a chatbot powered by an Azure OpenAI model. This chatbot is a part of the sales and grievences team to analyze customer interactions. It's task will be to identify the interactions by their 'Review Type', as good review, bad review or a quotation. it is only allowed to generate keywords or metadata from that particular review including product name, issues that the customers face, qualities that they like or dislike in case of a review and technical specifications that they specified in their quotations.

## Features
- **Chat Interface**: Users can type prompts or questions in a text area and submit them to the chatbot.
- **Real-time Responses**: The chatbot provides real-time responses to user inputs without requiring a page refresh.
- **Message Formatting**: User messages and chatbot responses are displayed in a visually appealing chat bubble format.
- **Response Categorization**: The chatbot categorizes responses into different types (e.g., good reviews, bad reviews, quotations) and formats them accordingly.

## Technologies Used
### Framework
- Flask: Backend web framework for handling HTTP requests and responses.
### Frontend
- Jinja2: Templating engine for rendering dynamic content in HTML templates.
- JavaScript/jQuery: Frontend scripting language for handling user interactions and AJAX requests.
- Bootstrap: Frontend CSS framework for styling the user interface.
### Backend
- Python : version 3.7
- AI Model (Azure OpenAI Services): Powers the chatbot's responses based on the user input.
    - Embedding Model (text_embedding_ada_002) : Conversion of user prompt and document to embedding.
    - AI Search : Search through the document using user input prompt
    - Azure Blob : Storing useful documents related to the chatbots knowledge.
    - OpenAI Model (gpt-35-turbo) : Generate responses based on embeddings from documents and user prompt.

## Installation
1. Clone the repository: `git clone https://github.com/Github-hackathons/MetaAIChat.git`
2. Navigate to the project directory: `cd MetaAIChat`
3. Install dependencies: `pip install flask openai requests dotenv`
4. Setting Azure OpenAI Environments required by the application, please refer to the [Environment Variables](#environment-variables) section.
4. Run the Flask application: `python app.py`
5. Access the application in your web browser at `http://localhost:5000`

## Environment Variables

Create an `.env` file and store the following variables.
Below are the environment variables required for the TeamTitans MetaAIChat project:

| Variable Name             | Description                            |
|-----------------------    |----------------------------------------|
| `AZURE_ENDPOINT`          | The endpoint for Azure services.       |
| `OPENAI_API_KEY`          | API key for accessing OpenAI services. |
| `API_VERSION`             | Version of the API being used.         |
| `DEPLOYMENTID`            | ID for the deployment.                 |
| `AZURE_SEARCH_ENDPOINT`   | The endpoint for Azure Search service. |
| `AZURE_SEARCH_KEY`        | API key for accessing Azure Search.    |
| `AZURE_SEARCH_INDEX_NAME` | Name of the search index.              |

## Usage
1. Open the application in your web browser.
2. Type your prompt or question in the text area provided.
3. Press the "Submit" button or hit Enter to send your message to the chatbot.
4. View the chatbot's response displayed in the chat interface.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them to your branch.
5. Push your changes to your fork on GitHub.
6. Submit a pull request to the main repository's `main` branch.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Inspiration: Creddit goes to Azure OpenAI for this wonderful oppurtunity. Thank you to the team TeamTitans members:
    [Sriram, Vijaya Kumar](mailto:vijaya-kumar.sriram@capgemini.com)
    [Kotal, Soumya Kanti](mailto:soumya-kanti.kotal@capgemini.com)
    [Asthana, Poorna](mailto:poorna.asthana@capgemini.com)
    [Mahapatra, Biraja Rani](mailto:biraja-rani.mahapatra@capgemini.com)

## Contact
For questions or inquiries, please contact [Ankur Sarkar](mailto:ankur.sarkar@capgemini.com).
