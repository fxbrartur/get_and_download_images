import requests # To GET the image, you'll need this library.
from time import sleep # To establish a productive routine for your cloud/machines.

image_urls = ['https://i.pinimg.com/564x/2b/dd/c9/2bddc91accccb9b70178c49cf5684bed.jpg','https://i.pinimg.com/564x/67/ce/4a/67ce4a070a3bc73dd6db088a61742101.jpg'] # Enter the URLs of the images you want to download here. As I did on the list, for example, remember to use quotation marks and commas to separate each item.

not_downloaded_images = [] # In case your GET method does not have a 200 response.

# Authorization = '?????'

for img in image_urls:
    
    file_name = img.split('/')[-1] # I decided to save the image with the name found in the images' last part of URLs. If necessary, you can modify this line.
    print(f"Reaching the image: {file_name}")
    req = requests.get(img, stream=True) # If an authorization is required on the header, you can insert it here.
    
    if req.status_code == 200:
    
        with open(file_name, 'wb') as file:
            for image in req:
                file.write(image)
    else:
    
        not_downloaded_images.append(img)

    sleep(0.5)
