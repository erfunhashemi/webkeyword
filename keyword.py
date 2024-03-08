import requests

def search_keyword_in_url(url, keyword):
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error
        content = response.text
        
        # Check if the keyword exists in the content
        if keyword in content:
            print(f"Keyword '{keyword}' found in the URL: {url}")
        else:
            print(f"Keyword '{keyword}' not found in the URL: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = input("Enter the URL: ")
keyword = input("Enter the keyword to search for: ")

search_keyword_in_url(url, keyword)
