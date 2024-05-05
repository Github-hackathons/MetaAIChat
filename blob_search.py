import openai, os, requests
from dotenv import load_dotenv
# from openai import AzureOpenAI

load_dotenv()

openai.api_type = "azure"
openai.api_version = os.getenv("API_VERSION")

# Azure OpenAI setup
openai.api_base = os.getenv("AZURE_ENDPOINT") # Add your endpoint here
openai.api_key = os.getenv("OPENAI_API_KEY") # Add your OpenAI API key here
deployment_id = os.getenv("DEPLOYMENTID") # Add your deployment ID here

use_azure_active_directory = False 

from azure.identity import DefaultAzureCredential, get_bearer_token_provider

if use_azure_active_directory:
    endpoint = os.environ["AZURE_ENDPOINT"]
    api_key = os.environ["OPENAI_API_KEY"]
    # set the deployment name for the model we want to use
    deployment = deployment_id

    client = openai.AzureOpenAI(
        base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
        azure_ad_token_provider=get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"),
        api_version="2023-09-01-preview"
    )

if not use_azure_active_directory:
    endpoint = os.environ["AZURE_ENDPOINT"]
    api_key = os.environ["OPENAI_API_KEY"]
    # set the deployment name for the model we want to use
    deployment = deployment_id

    client = openai.AzureOpenAI(
        base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
        api_key=api_key,
        api_version="2023-09-01-preview"
    )

print(">>>>", f"{endpoint}/openai/deployments/{deployment}/extensions")
# Azure AI Search setup
search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT") # Add your Azure AI Search endpoint here
search_key = os.getenv("AZURE_SEARCH_KEY") # Add your Azure AI Search admin key here
search_index_name = os.getenv("AZURE_SEARCH_INDEX_NAME") # Add your Azure AI Search index name here

def setup_byod(deployment_id: str) -> None:
    """Sets up the OpenAI Python SDK to use your own data for the chat endpoint.

    :param deployment_id: The deployment ID for the model to use with your own data.

    To remove this configuration, simply set openai.requestssession to None.
    """

    class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):

        def send(self, request, **kwargs):
            request.url = f"{openai.api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version={openai.api_version}"
            return super().send(request, **kwargs)

    session = requests.Session()

    # Mount a custom adapter which will use the extensions endpoint for any call using the given `deployment_id`
    session.mount(
        prefix=f"{openai.api_base}/openai/deployments/{deployment_id}",
        adapter=BringYourOwnDataAdapter()
    )

    openai.requestssession = session

# setup_byod(deployment_id)


message_text = [{"role": "user", "content": "What are the differences between Azure Machine Learning and Azure AI services?"}]

def ask_openai_blob(user_input):    
    message_text = [{"role": "user", "content": user_input}]

    #Get some Error like Resource not found, Etc.etc....
    completion = client.chat.completions.create(
        messages=message_text,
        model = deployment,
        extra_body={
            "data_sources":[  # camelCase is intentional, as this is the format the API expects
                {
            "type": "azure_search",
            "parameters": {
                "endpoint": search_endpoint,
                "index_name": search_index_name,
                "semantic_configuration": "default",
                "query_type": "vector",
                "fields_mapping": {},
                "in_scope": True,
                "role_information": "you are an ai assistant. As a part of the sales and grievances team you will get customer interactions. \
                                    Your task will be to identify the interactions by their 'Review Type', as good review, bad review or a quotation. \
                                    You only need to generate keywords or metadata from that particular interaction including product name, issues that they face, \
                                    qualities that they like or dislike in case of a review and technical specifications that they specified in their quotations, \
                                    will be generated from the interaction. Below is the list of all products manufactured by the company. In case of quotations, \
                                    suggestions of the products are to be strictly made among these products. ",
                "filter": None,
                "strictness": 3,
                "top_n_documents": 5,
                "authentication": {
                "type": "api_key",
                "key": search_key
                },
                "embedding_dependency": {
                "type": "deployment_name",
                "deployment_name": "titan_embedding_365"
                },
                "key": search_key,
                "indexName": search_index_name
    }
    }
        ]},
        temperature=0.15,
        top_p=1,
        max_tokens=200,
        stop=None
    )
    print(completion)
    return completion