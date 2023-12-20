 
# import requests
# from bs4 import BeautifulSoup

# url = "https://ddd-practitioners.com/home/glossary/"
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     html_content = response.content

#     # Parse the HTML content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Extract text and links
#     entries = soup.find_all('a')
#     for entry in entries:
#         text = entry.get_text(strip=True)
#         link = entry['href']
#         print(f"Text: {text}\nLink: {link}\n")
# else:
#     print(f"Failed to retrieve content. Status Code: {response.status_code}")


import requests
from bs4 import BeautifulSoup

url = "https://ddd-practitioners.com/home/glossary/"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <p> tags with text containing *
    target_p_tags = soup.find_all('p', text=lambda text: text and '*' in text)

    if target_p_tags:
        # Extract and print the HTML content of each matching <p> tag
        for p_tag in target_p_tags:
            result_html = str(p_tag)
            print(result_html)
    else:
        print("No <p> tags with '*' in the text were found.")
else:
    print(f"Failed to retrieve content. Status Code: {response.status_code}")
