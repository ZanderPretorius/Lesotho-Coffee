

add_cafe = {
    "city": "Bellville",
    "country": "Sierra-Leonne",
    "google_maps_url": "https://goo.gl/maps/SXLZH6XHVvVghGJc9",
    "name": "Coffee by Enzokuhle",
    "perks": {
        "has_alcohol": True,
        "has_calls": False,
        "has_food": True,
        "has_mask": False,
        "has_pets": True,
        "has_power": False,
        "has_toilet": True,
        "has_wifi": False
    }
}


def ModelledCafe(added_cafe):

    returned_dict = {}

    name = added_cafe['name']
    country = added_cafe['country']
    city = added_cafe['city']
    google_maps_url = added_cafe['google_maps_url']
    input_perks = added_cafe['perks']

    # index_name creation
    index_name = (name.replace(" ", "_")).lower()

    # img_link_case creation
    img_link_case = (name.replace(" ", "-")).lower()

    # perks function

    output_perks = {}
    for perk in input_perks:
        perk_name = perk
        perk_value = input_perks[perk]
        if perk_name == "has_alcohol":
            if perk_value == False:
                icon_url = "no-alcohol"
            else:
                icon_url = "yes-alcohol"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_calls":
            if perk_value == False:
                icon_url = "no-calls"
            else:
                icon_url = "yes-calls"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_pets":
            if perk_value == False:
                icon_url = "no-pets"
            else:
                icon_url = "yes-pets"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_power":
            if perk_value == False:
                icon_url = "no-power"
            else:
                icon_url = "yes-power"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_toilet":
            if perk_value == False:
                icon_url = "no-toilet"
            else:
                icon_url = "yes-toilet"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_wifi":
            if perk_value == False:
                icon_url = "no-wifi"
            else:
                icon_url = "yes-wifi"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_mask":
            if perk_value == False:
                icon_url = "no-mask"
            else:
                icon_url = "yes-mask"

            output_perks[perk_name] = {
                "icon_url": icon_url,
                "value": perk_value

            }
        if perk_name == "has_food":
            if perk_value == False:
                icon_url = "no-food"
            else:
                icon_url = "yes-food"

            output_perks[perk_name] = {

                "icon_url": icon_url,
                "value": perk_value

            }

    # print(output_perks)
        # print(f"{perk_name}: {perk_value}")

    returned_dict['name'] = name
    returned_dict['country'] = country
    returned_dict['city'] = city
    returned_dict['google_maps_url'] = google_maps_url
    returned_dict['index_name'] = index_name
    returned_dict['img_link_case'] = img_link_case
    returned_dict['perks'] = output_perks
    return (returned_dict)


# x = ModelledCafe(add_cafe)
# print(x)
# print(x.return_data)
# print(add_cafe['name'])
