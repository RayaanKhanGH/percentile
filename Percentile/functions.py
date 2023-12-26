def searchWeight(gender, weight, arr):
    matches = 0

    for item in arr:
        if item["Gender"] == gender:
            if item["Weight"] == weight:
                matches += 1

    # Given values
    value = matches
    total = 500

    # Calculate the percentile
    percentile = (value / total) * 1000

    # Print the percentile
    return ({"percentile": f"{percentile:.2f}th percentile", "matches": value})


def searchHeight(gender, height, arr):
    matches = 0

    for item in arr:
        if item["Gender"] == gender:
            if item["Height"] == height:
                matches += 1

    # Given values
    value = matches
    total = 500

    # Calculate the percentile
    percentile = (value / total) * 1000

    # Print the percentile
    return ({"percentile": f"{percentile:.2f}th percentile", "matches": value})
 
