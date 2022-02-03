def display_winner_string():
    image = "    \\o/ \n" \
            "     |  \n" \
            "    / \\"
    print(image)


def display_loser_string(image_index):
    image = [
        "  | \n",
        "  \\o \n",
        "  /|\\ \n",
        "  // \n",
        "  \\\\,"
    ]
    if image_index == 0:
        print(image[0])
    elif image_index == 1:
        print(image[0] + image[1])
    elif image_index == 2:
        print(image[0] + image[1] + image[2])
    elif image_index == 3:
        print(image[0] + image[1] + image[2] + image[3] + image[4])
