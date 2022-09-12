from serpapi import GoogleSearch
import requests

params = {
    "q": "Psychologist",
    "tbm": "isch",
    "ijn": "2",
    "api_key": "2b5c2c302422947548ac1a8b232bf80219d68adf6f8d6f3d5abd37f958ef0c43"
}

search = GoogleSearch(params)
results = search.get_dict()
images_results = results["images_results"]
print(images_results[1])
print(images_results[1]['thumbnail'])


def download_image(url, file_name, headers):
    # Send GET request
    response = requests.get(url, headers=headers)
# Save the image
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


for i in (range(len(images_results))):

    if __name__ == "__main__":
        # Define HTTP Headers
        headers = {
            "User-Agent": "Chrome/51.0.2704.103",
        }
        # Define URL of an image
        # url = "https://serpapi.com/searches/631e4f40b7b1cc035b0ab748/images/05109f1d08e7880997a7d55a45910361fe68c6ecad37992ee517563067e91c80.jpeg"
        url = images_results[i]['thumbnail']
        # Define image file name
        # "Your first value is {} your second value is {}".format(
        #     amount1, amount2)
        file_name = "image {} .png".format(i + 200)
        # Download image
        download_image(url, file_name, headers)
