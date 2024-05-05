import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# print(">> API KEY ", os.getenv('API_KEY'))
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_ENDPOINT"), 
  api_key=os.getenv("OPENAI_API_KEY"),  
  api_version=os.getenv("API_VERSION")
)

system_content = "you are an ai assistant. As a part of the sales and grievences team you will get customer interactions. Your task will be to identify the interactions by their 'Review Type', as good review, bad review or a quotation. You only need to generate keywords or metadata from that particular review including product name, issues that they face, qualities that they like or dislike in case of a review and technical specifications that they specified in their quotations, will be generated from the interaction. Below is the list of all products manufactured by the company. In case of quotations, suggestions of the products is to be strictly made among these products. \
\
Product Documentation \
 \
1. Phone - Model X1 \
 \
Technical Specifications: \
 \
Processor: Octa-core Snapdragon 888 \
RAM: 8GB \
Storage: 128GB / 256GB / 512GB (Expandable) \
Display: 6.5-inch Super AMOLED, 120Hz refresh rate \
Camera: Quad-camera setup (108MP main, 12MP ultrawide, 8MP telephoto, 5MP depth sensor) \
Battery: 5000mAh, 65W fast charging \
Operating System: Android 12 \
Connectivity: 5G, Wi-Fi 6E, Bluetooth 5.2 \
Security: In-display fingerprint scanner, Face recognition \
Additional Features: IP68 water and dust resistance, NFC, USB Type-C \
2. Laptop - Model ZBook Pro \
 \
Technical Specifications: \
 \
Processor: Intel Core i9-11980HK \
RAM: 32GB DDR4 \
Storage: 1TB NVMe SSD \
Display: 15.6-inch 4K OLED \
Graphics: NVIDIA RTX 3080 \
Battery: 92Whr, 230W AC Adapter \
Operating System: Windows 11 Pro \
Connectivity: Wi-Fi 6E, Bluetooth 5.2 \
Ports: Thunderbolt 4, USB-C, HDMI, SD Card Reader \
Security: Fingerprint Reader, TPM 2.0 \
Weight: 4.5 lbs (2.04 kg) \
3. Smart Watch - Model S3 \
 \
Technical Specifications: \
 \
Processor: Dual-core Apple S7 \
RAM: 1GB \
Storage: 32GB \
Display: 1.78-inch LTPO OLED \
Sensors: Heart rate monitor, ECG, Blood oxygen, Accelerometer, Gyroscope \
Connectivity: Bluetooth 5.0, Wi-Fi \
Battery Life: Up to 18 hours \
Water Resistance: 50 meters \
Operating System: watchOS 8 \
Additional Features: Built-in GPS, NFC for Apple Pay, Siri integration \
4. Desktop - Model Horizon 5000 \
 \
Technical Specifications: \
 \
Processor: AMD Ryzen 9 5900X \
RAM: 64GB DDR4\
Storage: 2TB NVMe SSD + 4TB HDD\
Graphics: NVIDIA RTX 3090\
Power Supply: 1000W\
Operating System: Windows 11 Pro\
Connectivity: Wi-Fi 6, Bluetooth 5.2\
Ports: USB-C, USB 3.2, HDMI, DisplayPort\
Cooling: Liquid cooling system\
Case: Tempered glass side panel, RGB lighting\
5. Server - Model Titan S500\
\
Technical Specifications: \
 \
Processor: Dual Intel Xeon Gold 6258R \
RAM: 256GB DDR4 ECC Registered \
Storage: 12TB SSD (RAID 5) \
Networking: Dual 10 Gigabit Ethernet \
Expansion: PCIe 4.0 slots for additional cards \
Power Supply: Redundant 1200W \
Operating System: Linux CentOS 8 \
Management: IPMI 2.0, BMC\
Security: TPM 2.0, Secure Boot\
Form Factor: Rack-mountable 2U\
\
\
Few examples:\
User : I'm experiencing frequent app crashes on my Phone X1. It's becoming frustrating to use.\
Bad Review, Product Name: Phone X1, Issue : Frequent app crashes | frustration with usage \
\
User : I need a laptop with 32GB RAM, 1TB NVMe SSD, and Windows 11 Pro OS.\
Quotation, Product Name: Laptop, Technical Specifications: 32GB RAM | 1TB NVMe SSD | Windows 11 Pro OS\
\
User : The S3 smartwatch has been a game-changer for my fitness journey. The heart rate monitor is accurate, and I love how it tracks my workouts and provides insightful data. The battery life is impressive, lasting me through long runs and workouts without needing a recharge. Plus, the sleek design looks great on my wrist. I highly recommend the S3 to anyone looking for a reliable fitness companion.\
Good Review, Product Name: S3 Smartwatch, Qualities Liked: Accurate heart rate monitor | Tracks workouts and provides insightful data | Impressive battery life | Sleek design"
message_text = [{"role":"system","content":system_content}
                # {"role": "user", "content": "Really comfy summer slides. Fit is a bit bigger than expected - Length & Width both. With socks on - perfect fit. Barefooted they make the a foot fart/squeek sound!! Oh well,\
                #  just wearing around the house anyway. Not sure about poolside, wet feet. May be slippery? Got the khaki color. Maybe choose a different color & size if I could do over. \
                #  Not sure of durability yet, only a week old. Support would be better if fit were better. Overall good choice for price."},
                # {"role": "assistant", "content": "very comfortable, summer slides, footware, good product, product review"},
                # {"role": "user", "content": "i have many-to-many relationship between Movie and Person through Cast. I use CastSerializer to create post method to create new movie and new cast relationship, but when call post method,\
                #  response return AttributeError"},
                # {"role": "assistant", "content": "python, django, database, doubt"},
                # {"role": "user", "content":"This was a LOV disaster! Tennis themed but really a tryst instead of a serve. Playing doubles??? The film really was not something I felt was worthy of producing, \
                # but Zendaya used her power and money to produce it - and star in it - etc.. Sometimes, when a person tries too hard to have a winner, alas, they have a loser! \
                # It was more a game of minds being manipulated than scoring on the court.."},
                # {"role": "assistant", "content": "Challengers, starring Zendaya, disastrous, bad review"}

                ]

def ask_openai(user_input):    
    message_text.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="titans-gpt-35-turbo", # model = "deployment_name"
        messages = message_text,
        temperature=0.2,
        max_tokens=50,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    out_data = completion.choices[0].message.content
    print(f"Completions > {type(out_data)} -- {out_data}")
    return out_data