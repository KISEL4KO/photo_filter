import opennsfw2 as n2


# Function to check if a photo is NSFW (Not Safe For Work)
def nsfw_check(img_path):
    # Predict the NSFW score of the image and round it to the nearest integer
    check = round(n2.predict_image(img_path))

    # If the score is greater than 0, consider it NSFW
    if check > 0:
        return 1
    # Otherwise, consider it safe
    else:
        return 0

